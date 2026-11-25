"""Resolve the N012 orthography and first-sentence ASR disagreement once."""

import argparse
from pathlib import Path
import runpy
import sys
from tempfile import TemporaryDirectory

from prepare import V2_WORKER, WORK, digest, load, write


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version', default='native')
    version = parser.parse_args().version
    cue = 'S12-N012'
    if (WORK/'selected'/f'{cue}.json').is_file():
        return
    clip = WORK/'drafts'/version/f'{cue}.wav'
    initial = WORK/'word-review'/version/f'{cue}.json'
    proof = load(initial)
    assert proof['text'] == "I'm not hurt. I'm all right!"
    assert proof['sha256'] == digest(clip)
    goal = 'i am not hurt i am all right'
    matching = []
    for model, reads in proof['transcripts'].items():
        for read in reads:
            read['normalized'] = ' '.join('all right' if word == 'alright' else word
                                          for word in read['normalized'].split())
            read['exact'] = read['normalized'] == goal
        if any(read['exact'] for read in reads):
            matching.append(model)
    if not matching:
        raise ValueError(f'{cue} has no word-level match even after correcting the spelling variant')

    report_path = WORK/'disagreement-check.json'
    report = load(report_path) if report_path.is_file() else {'files':[]}
    evidence = next((item for item in report['files'] if item['file_sha256'] == proof['sha256']),None)
    if not evidence:
        compare = runpy.run_path(str(V2_WORKER/'disagreements.py'))['main']
        compare.__globals__['FORMS'] = {cue: ("I'M NOT HURT I'M ALL RIGHT", "I'M NOT HURT I'M ALRIGHT",
                                              "I'M NOT HEARD I'M ALL RIGHT", "I'M NOT HEARD I'M ALRIGHT")}
        with TemporaryDirectory(dir=WORK,prefix='n012-ctc-') as work:
            compare.__globals__['WORK'] = Path(work)
            sys.argv = [sys.argv[0], '--cue', cue, '--wav', str(clip)]
            compare()
            measured = load(Path(work)/report_path.name)
        evidence, = measured['files']
        report.update({key:value for key,value in measured.items() if key != 'files'})
        report['files'].append(evidence)
    assert evidence['file_sha256'] == proof['sha256']
    scores = evidence['target_log_likelihoods']
    margin = max(value for key,value in scores.items() if 'HURT' in key) - max(
        value for key,value in scores.items() if 'HEARD' in key)
    evidence.update({'version':version, 'critical_consonant_ctc_margin':margin,
                     'best_target_matches_words':margin > 0,
                     'source_word_review_sha256':digest(initial),
                     'orthographic_equivalence':'alright = all right',
                     'decision':'Retake if independent ASR does not confirm hurt.'})
    write(report_path, report)
    if margin <= 0:
        raise ValueError(f'{cue} still needs a native retake, margin {margin:.3f}')

    proof.update({'matching_models':matching, 'accepted':True,
                  'independent_critical_consonant_review':evidence})
    row = next(row for row in load(WORK/'stage_jobs.json') if row['id'] == cue)
    claim = load(WORK/'checks'/version/f'{cue}.json')
    cast = load(WORK/'cast'/version/f'{cue}.json')
    runpy.run_path(str(V2_WORKER/'qualify.py'))['selection'](row, claim, proof, cast, clip)


if __name__ == '__main__':
    main()
