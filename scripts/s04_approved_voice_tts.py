#!/usr/bin/env python3
"""S04 directed voice preflight/export. No neutral fallback synthesis."""
import sys
from voice_direction_tools import legacy_voice_cli

if __name__ == "__main__":
    try:
        raise SystemExit(legacy_voice_cli("S04"))
    except (ValueError, KeyError, OSError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        raise SystemExit(1)
