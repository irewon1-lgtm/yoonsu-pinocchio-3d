# Codex / AI agent entrypoint (main)

**DO NOT produce S02-S12 content from the main branch.** This branch only hosts an entrypoint. The canonical production branch is `s01/full-story-production`.

Before making changes:

```sh
git fetch origin
git switch s01/full-story-production
python3 scripts/validate_series_v2.py
```

Read the production branch `AGENTS.md`, `docs/series_v2/PRODUCTION_PRD_V2_0.md`, and `docs/series_v2/CODEX_HANDOFF.md`. Keep S01 unchanged. S02-S12: each 360+ seconds of non-wait narrative and exactly 10 Yoonsu interactions including original interactions; expand the original V1.1 story one scene at a time. Review S02 detailed screenplay before rendering.
