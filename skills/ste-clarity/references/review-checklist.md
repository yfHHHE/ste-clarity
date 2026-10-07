# STE Clarity Review Rubric

## Meaning integrity: mandatory gate

Before scoring clarity, compare the source and the result. Confirm that:

- Facts, numbers, identifiers, actors, sequence, and technical distinctions are preserved.
- Obligation, permission, prohibition, negation, uncertainty, conditions, and exceptions are preserved.
- Performance expectations and other constraints remain, even when they need clarification.
- No unsupported causes, owners, thresholds, advice, or details were added.
- Unresolved ambiguity is retained or flagged rather than silently resolved.

**PASS:** All checks hold for the requested transformation.
**FAIL:** The result changes or invents meaning. Report the specific change and repair it before assigning a clarity rating.
**UNVERIFIED:** The source or supporting evidence is insufficient to check fidelity. State the limitation; do not give an overall passing rating.

For newly authored content, check against the user brief and supplied evidence. Distinguish proposed designs or recommendations from established facts. For a review of an original document without an earlier source, review its clarity but mark source fidelity unverified.

## Clarity score: only after the gate passes

Score each applicable category from 0 to 2:

- **0:** Material problem.
- **1:** Usable but can improve.
- **2:** Clear.
- **N/A:** Not relevant to this content; exclude from the denominator and give a brief reason.

| Category | What to check |
| --- | --- |
| Terminology | One term per concept; stable identifiers; abbreviations explained when needed. |
| Sentences | Clear main points, explicit supported actors, unambiguous references, visible conditions. |
| Actionability | For actionable content: steps, supported owners, branches, and expected results are clear. |
| Decision quality | For decision content: facts, evidence, inference, risks, and recommendations are distinguishable. |
| Testability | For requirements: responsible component, observable behavior, conditions, and supported limits are clear. |
| Information design | Important information comes first; lists and tables help; formatting is proportional to the task. |

Report the gate result, applicable scores, and total as `earned / (2 × applicable categories)`. Do not count N/A as a full score.

## Interpretation

- **90–100%:** Excellent clarity.
- **70–<90%:** Good; fix the weakest category.
- **50–<70%:** Significant clarity problems.
- **Below 50%:** Rewrite before publication.

Any applicable category scored 0 requires a targeted fix, even if the overall percentage is high. If no categories apply, give no numerical rating. Scores guide review; they do not certify ASD-STE100 compliance or establish the truth of the source.
