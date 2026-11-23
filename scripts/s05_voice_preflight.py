#!/usr/bin/env python3
"""S05 voice identity and per-line direction preflight; no actual synthesis."""
import sys
from voice_direction_tools import ROOT, legacy_voice_cli, voice_preflight

def audit(root=ROOT):
    return voice_preflight(root, "S05")

if __name__ == "__main__":
    try:
        raise SystemExit(legacy_voice_cli("S05"))
    except (ValueError, KeyError, OSError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        raise SystemExit(1)
