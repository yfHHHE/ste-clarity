# Agent guide

## Installing for a user

Read `README.md`, `INSTALL.md`, and `skills/ste-clarity/SKILL.md`. Follow the route for the user's agent and requested scope. A global install means that user's skill or plugin directory, not all accounts on the machine. Preserve existing customized installations. Do not change persistent conversation rules or enable an always-on mode as part of installation.

## Maintaining the repository

The source of truth is `skills/ste-clarity/`. Edit it first, then synchronize the complete `.cursor/skills/ste-clarity/` mirror. Keep plugin versions aligned in `.codex-plugin/plugin.json` and `.claude-plugin/plugin.json`.

Read `CONTRIBUTING.md` before editing. Source examples must contain every fact used in a rewrite. Never strengthen should/may/must, invent missing information, or trade meaning for a higher clarity score.

Run:

```bash
python3 scripts/check_package.py
git diff --check
```

For behavior changes, use the cases in `evals/README.md` with the target model or harness and report actual outcomes. Package checks are not behavioral evidence.

## Publication boundaries

Use synthetic examples. Do not include employer or customer names, private domains, credentials, real incident identifiers, personal contact information, local absolute paths, or raw chat transcripts. Review only task-relevant files and publish only authorized content.

The skill cannot certify ASD-STE100 compliance. Do not copy the official standard or dictionary into this repository. Do not add integrations or hooks without a concrete need and appropriate user authorization.
