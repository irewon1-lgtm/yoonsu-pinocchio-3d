"""Validate the S12 V3 authoritative job IDs and bind the approved cast."""

import csv
from hashlib import file_digest
import json
from pathlib import Path

from performance import beats

REPO = Path(__file__).resolve().parents[4]
PACKAGE = Path('/workspace/scratch/s12-v3/intake/S12_FINAL_PRODUCTION_READY_V3')
HANDOFF = PACKAGE/'source/episodes/S12'
WORK = Path('/workspace/scratch/s12-v3/voice')
FINAL = REPO/'scenes/S12/v3/build/voices'
REFERENCE = Path('/workspace/scratch/s06-index-tts2')
V1 = Path('/workspace/scratch/s10-production')
REFS = V1/'voices/refs'
V2_WORKER = REPO/'scenes/S10/v2/voice'
S11_WORKER = REPO/'scenes/S11/v2/voice'
CAST = Path('/workspace/scratch/s10-v2/voice/cast-reference-proof.json')
ROLES = {'피노키오':'pinocchio', '제페토':'geppetto', '귀뚜라미':'cricket',
         '파란 요정':'fairy', '내레이션':'narrator'}

# Start with the supplied cross-cast representatives; complete the playable
# first fifteen cuts before the human-form-dependent final sequence.
FIRST = (('U005','U029','U030'), ('U009','U031','U032'),
         ('U003','U004','U011'), ('U027','U002','U018','U028','U042','U044'))
RESCUE = ('U001','N001','N002','M001','N003','N004','N005','N006','M002','N007',
          'U006','U007','U008','U010','M003','U012')


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write(path, data):
    tmp = path.with_suffix('.part')
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    tmp.replace(path)


def digest(path):
    with path.open('rb') as file:
        return file_digest(file,'sha256').hexdigest()


def approved_cast():
    previous = load(CAST)
    roles = previous['sources']
    assert set(roles) == set(ROLES.values())
    for role, proof in roles.items():
        assert digest(REFS/f'{role}.wav') == proof['verified_conditioning_sha256'] == proof['sha256']
        original = REPO/proof['source']
        if 'approved_mp3_sha256' in proof:
            attached = HANDOFF/'voice/references'/original.name
            assert digest(attached) == proof['approved_mp3_sha256']
            assert proof['attached_and_approved_pcm_match'] and proof['decode_verified_sample_identical']
        else:
            assert digest(original) == proof['sha256'] and proof['approved_pcm_bytes_match']
    write(WORK/'approved-cast.json', {'previous_voice_proof_sha256': digest(CAST), **previous})
    return roles


def schedule(rows):
    by_id = {row['id'][4:]:row for row in rows}
    assigned = set()
    balance = [0]*4
    ordered = []
    def assign(row, lane):
        row['lane'] = lane
        balance[lane] += 40*len(row['beats']) + 6*len(row['text'].split())
        ordered.append(row)
        assigned.add(row['id'])
    for lane, first in enumerate(FIRST):
        for cue in first:
            assign(by_id[cue],lane)
    for row in [*(by_id[cue] for cue in RESCUE), *rows]:
        if row['id'] not in assigned:
            assign(row, min(range(4), key=balance.__getitem__))
    return ordered


def main():
    for path in (WORK, WORK/'selected', FINAL):
        path.mkdir(exist_ok=True, parents=True)
    evidence = approved_cast()
    jobs = HANDOFF/'story/S12_VOICE_JOBS.json'
    design = HANDOFF/'story/scene_design_v2.json'
    interactions = HANDOFF/'story/interaction_map_v2.json'
    loaded = load(jobs)['jobs']
    story = [r for r in loaded if r['kind'] != 'EXTERNAL_MODEL']
    models = [r for r in loaded if r['kind'] == 'EXTERNAL_MODEL']
    assert len(loaded) == len({r['job_id'] for r in loaded}) == 81
    assert len(story) == 71 and len(models) == 10
    assert sum(row['kind']=='ORIGINAL' for row in story) == 44
    assert [(r['dialogue_id'],r['speaker'],r['spoken_text']) for r in load(design)['dialogue']] == [
        (r['job_id'],r['speaker'],r['spoken_text']) for r in story]
    assert [(r['model_job_id'],r['id'],r['cue'],r['external_model_speaker'])
            for r in load(interactions)['events']] == [
        (r['job_id'],r['event_id'],r['spoken_text'],r['speaker']) for r in models]
    with (PACKAGE/'qa/VOICE_ACTING_AUDITION_MATRIX.csv').open(encoding='utf-8-sig',newline='') as stream:
        matrix = list(csv.DictReader(stream))
    assert {row['line_id'] for row in matrix} == {f'S12-{cue}' for lane in FIRST for cue in lane}
    rows = []
    for spec in loaded:
        cue,speaker,text = spec['job_id'],spec['speaker'],spec['spoken_text']
        voice = ROLES[speaker]
        script_beats = beats(cue,text)
        assert ' '.join(piece['text'] for piece in script_beats) == text
        rows.append({'id':cue,'kind':spec['kind'],'narrative':spec['kind']!='EXTERNAL_MODEL',
                     'text':text,'speaker':speaker,'voice':voice,'reuse':False,
                     'profile_id':spec['profile_id'],'authored_direction':spec['voice_direction'],
                     'ref_sha256':evidence[voice]['sha256'],'beats':script_beats})
    ordered = schedule(rows)
    write(WORK/'stage_jobs.json',ordered)
    write(WORK/'source-proof.json', {'jobs_sha256':digest(jobs),'design_sha256':digest(design),
          'interactions_sha256':digest(interactions),'total_jobs':81,'main_jobs':71,'models':10,
          'cast_proof_sha256':digest(WORK/'approved-cast.json'),
          'audition_matrix_jobs':[row['line_id'] for row in matrix],
          'direct_listening':'NOT_RUN'})
    for lane in range(4):
        assigned=[row['id'] for row in ordered if row['lane']==lane]
        print(f'Lane {lane}: {len(assigned)}, starting {assigned[:5]}')

if __name__=='__main__':
    main()
