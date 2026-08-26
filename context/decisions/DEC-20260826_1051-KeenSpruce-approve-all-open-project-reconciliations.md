---
apiVersion: processkit.projectious.work/v2
kind: DecisionRecord
metadata:
  id: DEC-20260826_1051-KeenSpruce-approve-all-open-project-reconciliations
  created: '2026-08-26T10:51:48+00:00'
spec:
  title: Approve all open project reconciliations
  state: accepted
  decision: Resolve all currently open reconciliation items, including pending migrations
    and every pk-doctor error, warning, and actionable informational finding.
  context: The owner explicitly approved all open reconciliations and requested a
    clean migration and pk-doctor state.
  rationale: Blanket approval removes the confirmation gates previously blocking migration
    conflict resolution, team scaffolding, archival, filename normalization, and sensitive-data
    remediation.
  consequences: The reconciliation may mutate processkit entities through MCP tools,
    archive historical briefings, normalize migration identifiers, adjust generated
    team exports or storage, and remediate or disposition sensitive-data findings.
  decided_at: '2026-08-26T10:51:48+00:00'
---
