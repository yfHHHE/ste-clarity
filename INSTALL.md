# Install STE Clarity

Choose one route for your agent. Do not install both a plugin and a standalone copy in the same agent unless you intend to manage duplicates.

## Codex plugin

```bash
codex plugin marketplace add yfHHHE/ste-clarity --ref main
codex plugin add ste-clarity@ste-clarity
codex plugin list
```

Start a new chat and invoke `$ste-clarity`. It then applies to all responses in that conversation until you say “stop clarity mode” or “关闭清晰模式”.

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

Start a new chat and invoke `/ste-clarity:ste-clarity`. It then applies to all responses in that conversation until you turn it off.

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

1. Explicitly enable STE Clarity, then ask a simple everyday question.
2. Change topics and ask for a plan or comparison. The style should remain active without reinvocation.
3. Ask for a detailed explanation or a poem. The requested depth or form should be preserved.
4. Say “stop clarity mode” or “关闭清晰模式”. The agent should confirm and stop applying the skill.

For Chinese, try: `我只有 20 分钟整理房间，应该先做什么？` The answer should offer a practical proposal without inventing facts about your room.

A successful installation does not prove these behaviors. See [evaluation cases](evals/README.md) and test the agent you use.

## Activation and compatibility

Installation alone does not activate the skill. Codex uses `policy.allow_implicit_invocation: false` in `agents/openai.yaml`; Claude uses `disable-model-invocation: true` in `SKILL.md`. Invoke explicitly or directly ask the agent to enable STE Clarity. Discussion of the skill or quoted commands must not activate it.

Once active, it stays on across topics for the current conversation until you ask to stop. Say “stop clarity mode”, “normal mode”, “关闭清晰模式”, or “恢复普通模式”. Invoke again to reactivate. A request to apply it only to one answer limits its scope accordingly.

There are no always-on hooks or edits to persistent user instructions. A new conversation starts inactive. Persistence depends on the host retaining the conversation instructions; a host that discards context may require reinvocation. Other agents may interpret invocation metadata differently; verify their behavior instead of assuming these controls are enforced.
