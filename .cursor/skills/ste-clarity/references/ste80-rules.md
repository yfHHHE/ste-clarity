# STE-80 Content Guidance

Read only the section relevant to the requested deliverable. The governing meaning-preservation rules live in `../SKILL.md`.

## Procedures

Use one primary action per step when it improves execution. Put supplied warnings and prerequisites before the affected action. Keep optional actions optional; imperative wording must not silently strengthen a recommendation. Include expected results and failure branches only when supported by the source or explicitly proposed as new procedure design.

A missing verification method is a gap to flag, not permission to invent a health endpoint or remediation command.

## Requirements

Identify the responsible component and observable behavior when supplied. Preserve the original obligation level. A useful shape is:

`<component> <original obligation> <behavior> <condition or limit>.`

Flag vague words such as “quickly,” “useful,” or “robust” for definition. Do not drop the expectation, invent its metric, or change “should” to “must.” A complete specification may require a question about ownership, thresholds, or acceptance criteria.

## API and architecture documentation

Distinguish requests, responses, events, state changes, and side effects. Preserve direction and ordering. Keep canonical service, event, and field names.

Describe synchronization, retries, timeouts, idempotency, authentication, and failure behavior when relevant and established. If missing information prevents an accurate description, flag the gap. Event-like prose alone does not prove asynchronous behavior.

## Reports and technical explanations

Lead with the answer or current status when that serves the reader. Use evidence, cause, risk, and action sections only where the content supports them and the reader needs them. State unknown causes as unknown when material; omit irrelevant sections.

Keep evidence distinct from inference and recommendations. Put supplied numbers beside their claims, with their units, period, and baseline when available. Qualitative source material remains qualitative unless additional evidence supplies the numbers.

For explanations, include purpose, mechanism, failure behavior, and next steps only to the depth the user needs. Do not impose a fixed five-part template.
