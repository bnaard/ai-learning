---
apiVersion: processkit.projectious.work/v1
kind: Migration
metadata:
  id: MIG-20260821_1647-RuntimeSync-aibox-runtime
  created: 2026-08-21 16:47:21+00:00
  updated: '2026-08-26T10:47:35+00:00'
spec:
  source: aibox-runtime-home
  source_url: aibox://runtime-home
  from_version: 0.28.14
  to_version: 0.34.2
  state: applied
  generated_by: aibox apply
  generated_at: 2026-08-21 16:47:21+00:00
  summary: 0 changed upstream, 0 conflicts, 5 new, 0 removed (1 groups affected)
  affected_groups:
  - runtime-misc
  affected_files:
  - path: .codex/themes/aibox.tmTheme
    classification: new-upstream
  - path: .config/bat/themes/aibox.tmTheme
    classification: new-upstream
  - path: .config/opencode/themes/aibox.json
    classification: new-upstream
  - path: .local/bin/aibox-agent-signal
    classification: new-upstream
  - path: .local/bin/aibox-codex-notify
    classification: new-upstream
  started_at: '2026-08-26T10:47:35+00:00'
  applied_at: '2026-08-26T10:47:35+00:00'
  progress_notes:
  - timestamp: '2026-08-26T10:47:35+00:00'
    actor: mcp
    note: 'Reconciled by pk-reconcile: host-managed runtime additions are unambiguous
      and already materialized.'
---

# Migration MIG-20260821_1647-RuntimeSync-aibox-runtime

Managed `.aibox-home/` runtime changes from `0.28.14` to `0.34.2`.

0 changed upstream, 0 conflicts, 5 new, 0 removed (1 groups affected)

## Counts

- unchanged: 43
- changed-locally-only: 0
- changed-upstream-only: 0
- conflict: 0
- new-upstream: 5
- removed-upstream: 0

- removed-upstream-stale: 0

## Changes by group

### runtime-misc

**new-upstream**

- `.aibox-home/.config/bat/themes/aibox.tmTheme` -> `.aibox-home/.config/bat/themes/aibox.tmTheme`
- `.aibox-home/.config/opencode/themes/aibox.json` -> `.aibox-home/.config/opencode/themes/aibox.json`
- `.aibox-home/.local/bin/aibox-agent-signal` -> `.aibox-home/.local/bin/aibox-agent-signal`
- `.aibox-home/.local/bin/aibox-codex-notify` -> `.aibox-home/.local/bin/aibox-codex-notify`
- `.aibox-home/.codex/themes/aibox.tmTheme` -> `.aibox-home/.codex/themes/aibox.tmTheme`
