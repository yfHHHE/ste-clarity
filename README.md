# STE Clarity

English | [简体中文](README.zh-CN.md)

**Make technical writing clearer without changing what it means.**

An agent skill for **English, Simplified Chinese, Traditional Chinese, and mixed Chinese-English** technical explanations, procedures, API documentation, requirements, and engineering reports. It preserves facts, uncertainty, conditions, and the difference between **should**, **may**, and **must**.

## Install

Ask your coding agent:

```text
Install the ste-clarity skill/plugin from https://github.com/yfHHHE/ste-clarity. Follow the repository's AGENTS.md and INSTALL.md. Install globally for my user account.
```

Or follow the [installation guide](INSTALL.md) for Codex, Claude Code, and compatible skill-based agents.

## Before and after

**Before**

> In circumstances where verification is unsuccessful, relevant information relating to the reason for the unsuccessful verification should ideally be made available to downstream consumers so that they can understand what happened.

**After**

> When verification fails, downstream consumers should ideally receive information that explains the failure.

The rewrite retains the recommendation. It does not invent an API, required fields, or a mandatory contract. See [more examples](skills/ste-clarity/examples/before-after.md).

## Three modes

- **STE-80:** Practical clarity editing. The default.
- **Strict review (English only):** Source-backed review against the requested official standard and terminology, with explicit verification limits.
- **Lint only:** Find important problems without rewriting the whole text.

Try:

```text
Rewrite this in STE-80. Preserve all technical meaning.
Lint this requirement for ambiguity. Do not rewrite it.
Review this procedure and flag missing conditions without inventing them.
```

## 中文支持

支持中文技术写作、改写与审阅，也支持中英混合内容。保留“必须 / 应当 / 可以 / 不得”的约束强度，以及“预计 / 暂未 / 基本”等限定语。

```text
使用 $ste-clarity 改写下面的中文，保留原意，不补充未知事实。
请只审阅这段需求的歧义，不要重写。
请改写这段英文，保留英文；用中文说明仍需确认的问题。
```

未指定输出语言时，改写保留原文语言及简繁体。中文指令不会自动触发翻译。中文审阅不属于 ASD-STE100 合规审阅。

**原文：** 目前核心功能基本完成，预计周五完成联调，暂未发现阻塞问题。

**改写：** 核心功能目前基本完成。预计周五完成联调。暂未发现阻塞问题。

See [Chinese guidance](skills/ste-clarity/references/chinese.md) and [Chinese/bilingual examples](skills/ste-clarity/examples/chinese.md).

## What it protects

1. Facts, numbers, units, identifiers, and sequence.
2. Obligation, permission, prohibition, and uncertainty.
3. Conditions, exceptions, and performance expectations.
4. Unknown actors and missing information: flagged, not guessed.
5. Meaning integrity: a mandatory gate before clarity scoring.

The skill applies to the requested deliverable. It does not impose a permanent conversation style. Compatible agents may select it automatically for relevant writing tasks; explicit invocation is also available.

## About STE-80

STE-80 is a practical style name, **not an 80% compliance score**. The skill is inspired by ASD-STE100 Simplified Technical English and references Issue 9. Formal review requires the applicable official edition and organization terminology.

This project is not affiliated with, endorsed by, or certified by ASD or STEMG. It does not distribute the official standard or certify compliance. See the [official ASD-STE100 site](https://www.asd-ste100.org/).

## Repository

- [Canonical skill](skills/ste-clarity/SKILL.md): instructions and mode selection.
- [Content guidance](skills/ste-clarity/references/ste80-rules.md): procedures, requirements, APIs, and reports.
- [Review rubric](skills/ste-clarity/references/review-checklist.md): integrity gate and clarity scoring.
- [Agent guide](AGENTS.md) and [contribution guide](CONTRIBUTING.md): maintenance and checks.

The Codex and Claude manifests package the same canonical skill. The Cursor copy is checked for exact equality. There are no runtime hooks, network calls, or executable installation scripts in the skill.

## Validation

```bash
python3 scripts/check_package.py
```

This checks package consistency and local documentation links. It does not prove model behavior or formal STE compliance. See [behavioral evaluation cases](evals/README.md) for manual testing.

## Credits and license

Repository packaging was inspired by [i-have-adhd](https://github.com/ayghri/i-have-adhd). STE Clarity is an independent skill with a different scope and activation policy.

[MIT License](LICENSE).
