#!/usr/bin/env python3
"""Write playback landmarks from measured samples of the inherited S12 edit."""

import json
from pathlib import Path
from shutil import copyfile

from register_character import HERE, write

BASE = Path('/workspace/scratch/s12-full/final-edit')
ROOT = HERE.parent


def derive(target):
    target.mkdir(parents=True,exist_ok=True)
    for path in ('audio','mix.wav','subtitles.srt'):
        if not (target/path).exists():
            (target/path).symlink_to(BASE/path)
    edit = json.loads((BASE/'edit.json').read_text())
    assert edit['fps']==24 and edit['story_clock_excludes_examples_and_wait']
    talk = {line['id']:line for shot in edit['cuts'] for line in shot['audio']}
    gates = []
    for turn in edit['events']:
        q = talk[turn['question_dialogue_id']]
        reply = talk[turn['resume_dialogue_id']]
        measured = round(q['end']*24_000)
        if measured != turn['question_wav_exact_end_sample'] or measured != turn['frame']*1000:
            raise ValueError(f'The measured question end does not match the encoded boundary: {turn["id"]}')
        gate = {'id':turn['id'],'model':turn['example_text'],'question_id':q['id'],
                'question_start_sec':q['start'],'question_end_sec':measured/24_000,
                'chapter_end_frame':turn['frame'],'model_duration_sec':turn['example_duration'],
                'model_on_story_clock':False,'microphone_enable':'after actual model ended',
                'guardian_can_continue':True,'reaction_cuts':turn['reaction_shot_ids'],
                'reaction_starts_sec':turn['reaction_start'],'reaction_done_sec':turn['reaction_end'],
                'resume_id':reply['id'],'resume_sec':reply['start'],'trigger_count':'once'}
        if gate['reaction_done_sec']>gate['resume_sec']+1.0e-6:
            raise ValueError(f'Reaction overlaps its designated reply: {turn["id"]}')
        turn['actual_timing'] = gate
        gates.append(gate)
    assert len(talk)==71 and len(gates)==10
    close = talk['S12-U044']['end']
    write(ROOT/'participation-final.json',{'fps':24,'main_seconds':edit['duration'],
          'seconds_through_last_story_line':close,'model_wait_retry_seconds_in_main':0,
          'question_time_source':'24 kHz exact original PCM, one thousand samples per frame', 'events':gates})
    write(target/'edit.json',edit)
    copyfile(target/'edit.json',target/'timeline.json')


if __name__ == '__main__':
    derive(ROOT/'edition')
