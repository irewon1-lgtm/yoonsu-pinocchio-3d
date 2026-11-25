"""Export the measured S12 recordings and provenance for the actual WAVs."""

import argparse
from collections import Counter
import csv
from hashlib import sha256
from pathlib import Path
import runpy
from zipfile import ZIP_DEFLATED, ZipFile

from prepare import FINAL, HANDOFF, PACKAGE, S11_WORKER, WORK, digest, load, write

MEASURE = runpy.run_path(str(S11_WORKER/'package.py'))
take = MEASURE['take']
reel = MEASURE['reel']


def archive(output, rows):
    target = output/'S12-Voice-Production.zip'
    temporary = target.with_suffix('.part')
    with ZipFile(temporary, 'w', ZIP_DEFLATED, compresslevel=4) as zipfile:
        for row in rows:
            cue = row['id']
            zipfile.write(FINAL/f'{cue}.wav', f'wav/{cue}.wav')
            zipfile.write(WORK/'selected'/f'{cue}.json', f'evidence/{cue}.json')
        for name in ('approved-cast.json','source-proof.json','stage_jobs.json','disagreement-check.json'):
            path = WORK/name
            if path.is_file():
                zipfile.write(path, f'production/{name}')
        for path in sorted(output.iterdir()):
            if path.suffix in ('.json','.mp3') and path.name != 'S12-Voice-Progress.json':
                zipfile.write(path, f'listening/{path.name}')
    with ZipFile(temporary) as zipfile:
        assert zipfile.testzip() is None
        for row in rows:
            cue = row['id']
            archived = zipfile.read(f'wav/{cue}.wav')
            assert sha256(archived).hexdigest() == load(WORK/'selected'/f'{cue}.json')['sha256']
    temporary.replace(target)
    print(f'{target} SHA256={digest(target)}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('progress','representatives','audition','models','complete'))
    mode = parser.parse_args().mode
    authored = [spec['job_id'] for spec in load(HANDOFF/'story/S12_VOICE_JOBS.json')['jobs']]
    all_rows = {row['id']:row for row in load(WORK/'stage_jobs.json')}
    assert len(authored)==81 and set(authored)==set(all_rows)
    present = [all_rows[cue] for cue in authored if (WORK/'selected'/f'{cue}.json').is_file()]
    verified = {row['id'] for row in present}
    output = WORK/'delivery'
    output.mkdir(exist_ok=True)
    if mode == 'representatives':
        cues = ('S12-U005','S12-U009','S12-U003','S12-U027','S12-U002')
        assert set(cues) <= verified
        reel(output,[all_rows[cue] for cue in cues],'S12-Voice-First-Five',.46)
        return
    if mode == 'complete':
        assert len(present)==81 and {wav.stem for wav in FINAL.glob('*.wav')}==verified
    if mode in ('audition','complete'):
        with (PACKAGE/'qa/VOICE_ACTING_AUDITION_MATRIX.csv').open(encoding='utf-8-sig',newline='') as stream:
            matrix = list(csv.DictReader(stream))
        assert len(matrix)==15 and all(entry['line_id'] in verified for entry in matrix)
        reel(output,[all_rows[entry['line_id']] for entry in matrix],'S12-Voice-Audition',.46)
    if mode in ('models','complete'):
        models = [row for row in present if not row['narrative']]
        assert len(models)==10
        reel(output,models,'S12-10-Models',.47)
    if mode == 'complete':
        story = [row for row in present if row['narrative']]
        assert len(story)==71 and story[-1]['text']=='The end.'
        reel(output,story,'S12-All-Dialogue',.42)
    signals = [take(row)[1] for row in present]
    report = {'verified_recordings':len(verified),'expected':81,
              'available_kinds':Counter(row['kind'] for row in present),
              'dual_exact_word_matches':sum(len(signal['transcript_matches'])==2 for signal in signals),
              'missing':[cue for cue in authored if cue not in verified],
              'approved_actor_references':'PASS' if signals else 'NOT_RUN',
              'direct_pronunciation_emotion_and_mix_listening':'NOT_RUN',
              'direct_listening_limit':'The environment has no assistant audio input.',
              'signals':signals}
    alternate = WORK/'disagreement-check.json'
    if alternate.is_file():
        report['independent_word_review'] = load(alternate)
    write(output/('S12-Voice-QA.json' if mode=='complete' else 'S12-Voice-Progress.json'),report)
    if mode=='complete':
        archive(output,present)
    print(f"{len(verified)}/81 staged, {report['dual_exact_word_matches']} matched both recognizers")


if __name__=='__main__':
    main()
