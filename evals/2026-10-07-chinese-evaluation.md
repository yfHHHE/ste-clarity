# STE Clarity manual model evaluation

Date: 2026-10-07 (Asia/Singapore). Agent: Codex subagent `chinese_eval`. Exact model identifier is not exposed in this evaluation context. Method: manually generated responses using the current canonical skill and relevant references, followed by acceptance review. This is not automated runtime integration or ASD-STE100 certification.

Read: the canonical skill and its Chinese/content references and examples, plus `evals/README.md`. Package version: 0.2.0.

## C1 — Chinese recommendation and performance

Request: 中文改写：“接口应该尽快返回有用的错误信息。”

Actual output:

> 接口应该尽快返回有用的错误信息。
>
> 说明：“尽快”和“有用”尚未定义；原文未给出响应时限或错误信息的具体内容。

**PASS:** Preserves 应该, 尽快, and 有用; invents no threshold or response fields. Keeping the already short source unchanged is compatible with the meaning-integrity rule.

## C2 — Conditional permission and prohibition

Request: 中文改写：“仅当两个副本均健康时才可以清空缓存，不得重启服务。”

Actual output:

> 仅当两个副本都健康时，才可以清空缓存。不得重启服务。

**PASS:** Both replicas remain the necessary condition; permission stays permission; the restart prohibition remains unconditional.

## C3 — Qualified status

Request: 中文改写：“核心功能基本完成，预计周五完成联调，暂未发现阻塞问题。”

Actual output:

> 核心功能基本完成。预计周五完成联调。暂未发现阻塞问题。

**PASS:** Preserves 基本, 预计, 暂未 and the original milestone. Does not claim completion, guaranteed timing, or absence of blockers.

## C4 — Unknown sender and recipient

Request: 中文改写：“审核完成后通知对方。”

Actual output:

> 审核完成后通知对方。
>
> 说明：原文未明确通知人和接收方。

**PASS:** Preserves sequence and unresolved actors. Does not invent a team or customer.

## C5 — Chinese instruction, English source

Request: 请改写这段英文：The API should quickly return useful error information.

Actual output:

> The API should return useful error information quickly.
>
> 说明：“quickly”和“useful”尚未定义；需明确响应时限和错误信息要求，才能据此验证。

**PASS:** Deliverable stays English; notes are Chinese and separate. Retains should and performance/usefulness expectations without supplying missing values.

## C6 — Traditional Chinese with conditional constraints

Request: 繁體改寫：“若 request_id 為空，API 必須拒絕此請求，且不得建立 session。”

Actual output:

> 若 request_id 為空，API 必須拒絕此請求，且不得建立 session。

**PASS:** Preserves Traditional Chinese, identifiers, mandatory rejection, and session prohibition. Both constraints remain governed by the same condition.

## C7 — No requirement is not a prohibition

Request: 翻译成中文：“Operators are not required to restart the service after this update.”

Actual output:

> 本次更新后，操作人员无需重启服务。

**PASS:** 无需 preserves absence of an obligation, with the operator actor and post-update timing intact.

## C8 — Normative 应当

Request: 中文改写：“根据本规范，服务应当保留审计记录。”

Actual output:

> 根据本规范，服务应当保留审计记录。

**PASS:** Preserves 应当 and reference to the standard. Does not assert a guessed modal definition.

## C9 — Strict ASD-STE100 review of Chinese

Request: 将中文文档做严格 ASD-STE100 合规审阅，未提供英文原文。

Actual output:

> ASD-STE100 的正式审阅范围是英文，中文清晰度审阅不能证明 ASD-STE100 合规。可以审阅中文文档的术语一致性、条件、主体和约束表达。
>
> 请提供待审阅的中文文档。

**PASS:** States the English-only boundary and offers Chinese clarity review. No actual document was supplied in this case, so requesting it is necessary. Does not certify compliance, fabricate findings, or translate without a request.

## C10 — Ambiguity lint only

Request: 只检查歧义，不重写：“服务必须及时响应。”

Actual output:

> “及时”缺少明确的响应时限，无法据此判断是否满足“必须响应”的要求。需明确响应时限。

**PASS:** Findings only; preserves the mandatory force; flags the missing timing criterion without inventing one.

## E1 — Should, quickly, useful

Request: Rewrite: “The API should quickly return useful error information.”

Actual output:

> The API should return useful error information quickly.
>
> Note: “Quickly” and “useful” need definitions before this requirement can be tested.

**PASS:** All three semantic elements remain. No invented fields or threshold.

## E2 — Ambiguous retry owner

Request: Rewrite: “After Service A calls Service B, it retries twice if the request times out.”

Actual output:

> After Service A calls Service B, it retries twice if the request times out.
>
> Note: “It” could refer to Service A or Service B. The retry owner needs clarification.

**PASS:** Does not select an owner; retains twice, timeout condition, and sequence; explicitly flags ambiguity.

## E3 — Cache permission and restart prohibition

Request: Rewrite: “The cache may be cleared only if both replicas are healthy. Do not restart the service.”

Actual output:

> Only if both replicas are healthy may the cache be cleared. Do not restart the service.

**PASS:** Maintains permission, the necessary condition involving both replicas, and unconditional prohibition.

## Result and conflicts

**13/13 cases pass all stated acceptance conditions in this manual evaluation.** No direct instruction conflicts found. The preference for conditions before actions is subordinate to the explicit meaning-integrity rule, so retaining the ambiguous retry sentence is appropriate. Strict review of Chinese is intentionally limited to clarity review. Unchanged short rewrites are permitted and sometimes necessary.

Evaluation limitation: these are same-agent generated outputs and self-assessments, with examples visible in the skill. They demonstrate one successful application, not independent grading, robustness across repeated runs, or runtime activation behavior.
