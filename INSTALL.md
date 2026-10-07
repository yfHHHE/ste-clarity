# Install STE Clarity

Choose one route for your agent. Do not install both a plugin and a standalone copy in the same agent unless you intend to manage duplicates.

## Codex plugin

```bash
codex plugin marketplace add yfHHHE/ste-clarity --ref main
codex plugin add ste-clarity@ste-clarity
codex plugin list
```

Start a new chat and invoke `$ste-clarity`.

To update:

```bash
codex plugin marketplace upgrade ste-clarity
codex plugin remove ste-clarity
codex plugin add ste-clarity@ste-clarity
```

To uninstall:

```bash
codex plugin remove ste-clarity
codex plugin marketplace remove ste-clarity
```

## Standalone skill: Codex or a compatible agent

Ask Codex's skill installer to install `skills/ste-clarity` from `yfHHHE/ste-clarity` into your user-level skills directory.

For a manual global installation, clone the repository and copy the **entire** skill folder into your agent's user-level skills directory. References and examples are required. The default Codex destination is `~/.codex/skills/ste-clarity`; if `CODEX_HOME` is customized, use its `skills` directory instead.

Example for the default Codex location (refuses to overwrite an existing install):

```bash
git clone https://github.com/yfHHHE/ste-clarity.git
mkdir -p ~/.codex/skills
if [ -e ~/.codex/skills/ste-clarity ]; then
  echo "Already installed; review your copy before updating."
else
  cp -R ste-clarity/skills/ste-clarity ~/.codex/skills/ste-clarity
fi
```

For Cursor, use `~/.cursor/skills/ste-clarity`. For agents supporting the shared user-level directory, use `~/.agents/skills/ste-clarity`. Confirm the search path for your agent version.

To update a manual installation, pull the checkout, preserve any local edits, and replace the installed skill folder. To uninstall, remove only the installed `ste-clarity` directory from the path you used.

## Claude Code plugin

```bash
claude plugin marketplace add yfHHHE/ste-clarity
claude plugin install ste-clarity@ste-clarity --scope user
claude plugin list
```

Start a new chat and invoke `/ste-clarity:ste-clarity`.

To update:

```bash
claude plugin marketplace update ste-clarity
claude plugin update ste-clarity@ste-clarity
```

To uninstall:

```bash
claude plugin uninstall ste-clarity@ste-clarity
claude plugin marketplace remove ste-clarity
```

## Verify behavior

Ask the agent to rewrite:

> The API should quickly return useful error information.

The answer must retain the recommendation and performance expectation. It may flag “quickly” and “useful” as undefined; it must not invent a response-time target or replace “should” with “must.”

For Chinese, try: `请改写：核心功能基本完成，预计周五完成联调，暂未发现阻塞问题。` The result must retain “基本”, “预计”, and “暂未”; it must not claim completion, a confirmed deadline, or absence of problems.

A successful installation does not prove this behavior. Validate it in the agent you use.

## Activation

The skill permits normal automatic selection for relevant writing tasks. It has no always-on hook and does not modify persistent user instructions. Invoking it requests clarity editing for the supplied content, not a permanent mode for unrelated work.
