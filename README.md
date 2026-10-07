# STE Clarity

English | [简体中文](README.zh-CN.md)

**Clearer AI responses. Same meaning. Less effort to follow.**

An opt-in style for everyday questions, explanations, advice, planning, comparisons, and writing—not just technical documents. Supports English, Simplified Chinese, Traditional Chinese, and mixed-language conversations.

Invoke it once. It stays active for the conversation until you turn it off.

## Install and activate

Ask your coding agent:

```text
Install the ste-clarity skill/plugin from https://github.com/yfHHHE/ste-clarity. Follow AGENTS.md and INSTALL.md. Install globally for my user account.
```

Then activate:

- **Codex:** `$ste-clarity`
- **Claude Code:** `/ste-clarity:ste-clarity`
- **Direct request:** “Enable STE Clarity for this conversation.”

Installation alone does not turn it on. Say **“stop clarity mode”** or **“关闭清晰模式”** to turn it off. Invoke again to reactivate. See the [installation guide](INSTALL.md) for platform details and updates.

## What changes

1. **Answer first.** Lead with what the user needs, without generic preambles.
2. **Easy to follow.** Use concrete language, clear connections, and consistent terms.
3. **Structure that fits.** Use steps for a procedure and comparisons for a choice. A simple answer can stay one sentence.
4. **Enough depth.** Keep important details, alternatives, and requested explanations. Clear does not mean always short.
5. **Honest meaning.** Preserve uncertainty and conditions. Distinguish facts from assumptions and advice.

No mandatory headings, word limits, or closing action. Emotional support can be warm; creative requests can be playful. A special request changes the answer's form without resetting the conversation mode.

## Everyday example

**User:** I have 20 minutes to tidy my room. Where do I start?

**Response:**

> Start with the floor so you can move around easily. Try this 20-minute plan:
>
> 1. Spend 5 minutes collecting rubbish and dishes.
> 2. Spend 10 minutes putting loose items where they belong, starting with the floor.
> 3. Spend 5 minutes clearing one surface you use often.
>
> If you run out of time, leave the remaining areas for another session.

This is a proposed plan, not an invented claim about the user's room. See [general conversation examples](skills/ste-clarity/examples/conversation.md).

## 中文支持

明确启用后，清晰模式会持续作用于本次对话，适用于日常问答、解释、建议、计划、比较和写作。

```text
启用 STE Clarity，直到我说关闭。
我有很多事要做，不知道先做哪件。
```

**回答示例：** 先选一件今天不做就会有明确后果的事。如果没有，就选最能减轻你压力的一件。把它缩小成一个现在能开始的动作，例如打开要处理的文件。

保留“必须 / 应当 / 可以 / 不得”和“预计 / 暂未 / 基本”的含义。改写默认保留原文语言及简繁体，不因中文提问就自动翻译英文原文。

[完整中文说明](README.zh-CN.md) · [中文表达指南](skills/ste-clarity/references/chinese.md) · [中文与双语示例](skills/ste-clarity/examples/chinese.md)

## Scope and persistence

The style stays active across topics in the current conversation after explicit invocation. New conversations start inactive. A direct stop request disables it; quoted text such as “translate ‘stop clarity mode’” does not.

This is instruction-based persistence, not a runtime hook. If a host discards the conversation context, you may need to invoke the skill again. Hosts differ in whether they enforce invocation metadata; verify your agent's behavior. The skill does not change global user rules.

## Technical writing remains available

When requested, the skill also helps rewrite, translate, or review procedures, requirements, API docs, and reports. It preserves facts, actors, quantities, conditions, and obligation strength. Missing information is flagged rather than guessed. New advice and creative proposals remain welcome when the user requests them.

- [Technical content guidance](skills/ste-clarity/references/ste80-rules.md)
- [Technical examples](skills/ste-clarity/examples/before-after.md)
- [Review rubric](skills/ste-clarity/references/review-checklist.md)
- [Strict STE review guidance](skills/ste-clarity/references/strict-review.md)

STE-80 is a practical clarity approach, not an 80% compliance score. Formal ASD-STE100 review concerns English and requires the applicable official edition and organization terminology. Chinese clarity review does not establish STE compliance.

This project is inspired by ASD-STE100 but is not affiliated with, endorsed by, or certified by ASD/STEMG. It does not distribute the official standard or certify compliance. See the [official site](https://www.asd-ste100.org/).

## Validation and maintenance

```bash
python3 scripts/check_package.py
```

Checks package consistency, explicit-only metadata, and local links. It does not prove live activation or cross-model behavior. See [behavioral evaluation cases and recorded runs](evals/README.md).

The [canonical skill](skills/ste-clarity/SKILL.md) is shared by Codex and Claude; the Cursor mirror is checked for equality. See [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md) for maintenance.

## Credits and license

Packaging was inspired by [i-have-adhd](https://github.com/ayghri/i-have-adhd). STE Clarity is an independent skill. [MIT License](LICENSE).
