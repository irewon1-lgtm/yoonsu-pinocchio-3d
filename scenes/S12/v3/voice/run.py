"""Drive the established IndexTTS2, cast-check and ASR production workers."""

import runpy
import sys
from types import SimpleNamespace

import prepare


def qualify_story_words():
    existing_main = runpy.run_path(str(prepare.S11_WORKER/'qualify.py'))['main']

    def load_with_selection_gate(path):
        helpers = runpy.run_path(path)
        if path == str(prepare.V2_WORKER/'qualify.py'):
            original_selection = helpers['selection']

            def publish(row, *evidence):
                if row['id'] == 'S12-N012':
                    print('HOLD S12-N012 for independent hurt/heard review', flush=True)
                    return
                original_selection(row, *evidence)

            helpers['selection'] = publish
        return helpers

    existing_main.__globals__['runpy'] = SimpleNamespace(run_path=load_with_selection_gate)
    existing_main()


def main():
    args = sys.argv[1:]
    if args == ['words']:
        qualify_story_words()
        return
    explicit = [args[i + 1] for i, arg in enumerate(args[:-1]) if arg == '--line']
    if explicit:
        read = prepare.load
        rank = {identifier: i for i, identifier in enumerate(explicit)}

        def ordered(path):
            data = read(path)
            if path == prepare.WORK/'stage_jobs.json':
                return sorted(data, key=lambda item: rank.get(item['id'], len(rank)))
            return data

        prepare.load = ordered
    runpy.run_path(str(prepare.S11_WORKER/'run.py'), run_name='__main__')


if __name__ == '__main__':
    main()
