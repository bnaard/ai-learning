---
apiVersion: processkit.projectious.work/v1
kind: Migration
metadata:
  id: MIG-20260727_0541-LockBaseline
  created: 2026-07-27 05:41:54+00:00
  updated: '2026-08-26T10:47:42+00:00'
spec:
  source: aibox-lock
  source_url: aibox://lock
  kind: schema-extension
  state: applied
  generated_by: aibox apply
  generated_at: 2026-07-27 05:41:54+00:00
  summary: 'Backfilled previous_selection: 5 addon(s), 23 tool(s), 2 harness(es)'
  started_at: '2026-08-26T10:47:42+00:00'
  applied_at: '2026-08-26T10:47:42+00:00'
  progress_notes:
  - timestamp: '2026-08-26T10:47:42+00:00'
    actor: mcp
    note: 'Reconciled by pk-reconcile: acknowledgement-only lock schema baseline;
      migration states that no code change is required.'
---

# Migration MIG-20260727_0541-LockBaseline

`aibox.lock` schema extended in v0.25.6 to record the previously
applied addon-tool and harness selection (DEC-20260508_1515-SilentAsh,
BR-CLEANUP-ARCH item 1). This backfill captures the current selection
as the baseline so the next `aibox apply` can compute a removal diff
when a tool or harness is disabled.

Backfilled previous_selection: 5 addon(s), 23 tool(s), 2 harness(es)

## Backfilled addon selection

- `git-ui`: gh, lazygit
- `latex`: svg-inkscape, texlive-biber, texlive-code, texlive-core, texlive-diagrams, texlive-fonts, texlive-math, texlive-recommended
- `node`: node, pnpm
- `preview-archive`: chafa, entr, librsvg, mupdf, p7zip, poppler, resvg, timg
- `preview-enhanced`: ffmpeg, ghostscript, rich

## Backfilled harness selection

- claude, codex

## Next action

Acknowledge with the migration-management skill (`/pk-resume` will
surface it). No code change is required — the next `aibox apply`
will use this baseline automatically.
