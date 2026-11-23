#!/usr/bin/env python3
"""S05 original, action/timing, per-line acting and document synchronization checks."""
import argparse
import sys
from voice_direction_tools import ROOT, validate_scene, negative_checks

def validate(root=ROOT, emit=print):
    return validate_scene(root, "S05", emit=emit)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    validate()
    if args.self_test:
        negative_checks(ROOT, ["S05"])
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, OSError, AssertionError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        raise SystemExit(1)
