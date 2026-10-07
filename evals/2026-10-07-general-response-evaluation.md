# STE Clarity v0.3.0 manual evaluation

Date: 2026-10-07 (Asia/Singapore). Evaluator: Codex subagent `chinese_eval`; exact model identifier unavailable. Sources read: canonical `SKILL.md`, `agents/openai.yaml`, `evals/README.md`, `references/chinese.md`, and `references/ste80-rules.md` in the public repository.

Method: actual responses generated below for simulated conversations, then assessed against every stated acceptance condition. Reading the skill as an evaluation reference does not itself activate the simulated conversations. Conversation A starts inactive and runs G1–G9, followed by G12 and regressions. G10 and G11 each start in separate, isolated simulated conversations. State annotations are evaluator records, not extra user-facing outputs.

## G1 — Discussion and explicit activation

Initial simulated state: inactive.

**User:** What does STE Clarity do? I am asking about it, not enabling it.

**Assistant:** STE Clarity is an opt-in response style that makes answers easier to follow while preserving meaning and uncertainty. Once enabled, it applies across topics in the conversation until you turn it off. This discussion has not enabled it.

State: inactive.

**User:** Enable STE Clarity for this conversation.

**Assistant:** STE Clarity is on for this conversation until you ask me to turn it off.

State: active.

**PASS:** Discussion did not activate; direct enable request did. Acknowledgement is one sentence.

## G2 — Short answer and topic change

**User:** Is 17 prime?

**Assistant:** Yes. Its only positive divisors are 1 and 17.

**User:** Why does a mirror fog up?

**Assistant:** A mirror fogs up when moist air touches its cold surface and water vapor condenses into tiny droplets. The droplets scatter light, making the reflection look cloudy.

State after both turns: active.

**PASS:** Direct, correct answers; no forced headings or next steps. State persists across topic change in the simulation.

## G3 — Proposed tidying plan

**User:** I have 20 minutes to tidy my room. Where do I start?

**Assistant:** Start with obvious rubbish, then clear the floor and the surface you use most. Aim for a more usable room rather than a deep clean.

1. Spend 3 minutes collecting rubbish.
2. Spend 5 minutes gathering laundry and putting it in a basket or one place.
3. Spend 8 minutes returning loose items to their usual places. Put anything you cannot place quickly in one temporary pile.
4. Use the last 4 minutes to clear your main surface and straighten the bed.

Skip any step that does not apply and use that time on the biggest remaining mess.

**PASS:** Usable proposed allocation totals 20 minutes. Times are recommendations, not invented facts. No assumptions about actual room contents are asserted as facts and no outcome is guaranteed.

## G4 — Paper versus phone

**User:** Should I take notes on paper or on my phone?

**Assistant:** Choose paper if you want to sketch freely or avoid phone distractions. Choose your phone if you want searchable notes that are easy to carry and edit.

For a meeting or class, paper can work well when you need a flexible page. For quick reminders while you are out, a phone can be more convenient. If both sound useful, try each for a few days and see which notes you actually return to.

**PASS:** Clear trade-offs and conditional advice. No assumed habits or unsupported universal learning claims.

## G5 — Emotional support

**User:** I made a mistake at work and feel awful.

**Assistant:** That sounds painful, especially if you care a lot about doing your job well. A mistake can need fixing without defining you or your ability.

When you feel ready, separate what happened from what you fear it means about you. You can then focus on anything that can still be corrected. What happened?

**PASS:** Warm, relevant support with one focused invitation. No diagnosis, forced checklist, or claim about how others will react.

## G6 — Requested depth

**User:** Explain photosynthesis in detail with an example.

**Assistant:** Photosynthesis is the process plants use to turn light energy into chemical energy stored in sugars. They use carbon dioxide and water as inputs and release oxygen. In plants, most photosynthesis happens in chloroplasts, which contain the light-absorbing pigment chlorophyll.

There are two linked stages. In the light-dependent reactions, chlorophyll absorbs light in membranes called thylakoids. That energy drives electron transfer and helps produce ATP and NADPH, molecules that supply energy and electrons for the next stage. Splitting water replaces the lost electrons and releases oxygen. The oxygen released during photosynthesis comes from water.

The Calvin cycle happens in the surrounding fluid, called the stroma. An enzyme called RuBisCO helps attach carbon dioxide to an existing five-carbon molecule. Further reactions use ATP and NADPH to make a three-carbon sugar precursor called G3P. Some G3P can be used to build sugars and other organic molecules; the rest helps regenerate the starting molecule so the cycle can continue. This stage does not directly capture light, but it depends on products of the light-dependent reactions.

A common simplified equation is:

`6 CO₂ + 6 H₂O + light energy → C₆H₁₂O₆ + 6 O₂`

This equation summarizes the overall process; glucose is not the immediate product of the Calvin cycle.

For example, a bean plant growing in sunlight takes up water through its roots and carbon dioxide through small leaf openings called stomata. Its leaves use light energy to produce sugar precursors. The plant can use the resulting sugars in cellular respiration, store carbon as starch, or make materials such as cellulose for new growth. Plants also carry out cellular respiration during the day and at night.

The rate depends on available light, carbon dioxide, water, and temperature. More of one input does not always increase the rate: another input can become limiting, and excessive heat or water loss can reduce photosynthesis.

**PASS:** Detailed mechanism, terminology explained, correct distinction between stages and immediate products, concrete example, limiting factors. Not reduced to a slogan.

## G7 — Creative exception, then factual answer

**User:** Write a playful two-line poem about a sleepy cat.

**Assistant:** My sleepy cat declared the sofa king,
Then snored through every royal happening.

**User:** How many sides does a hexagon have?

**Assistant:** A hexagon has six sides.

State: active throughout.

**PASS:** Exactly two poem lines, playful subject, followed by direct factual response. Creative request did not disable mode in the simulation.

## G8 — Quoted stop command

**User:** Translate ‘stop clarity mode’ into Chinese.

**Assistant:** 关闭清晰模式。

**User:** Is STE Clarity still on?

**Assistant:** Yes. Translating the quoted phrase did not turn STE Clarity off.

State: active.

**PASS:** Translation treats command as content, not a mode change. Explicit status confirms simulated state.

## G9 — Stop, status, reactivation

**User:** 关闭清晰模式。

**Assistant:** 已关闭清晰模式。

State: inactive.

**User:** 现在清晰模式还开着吗？

**Assistant:** 没有，当前处于关闭状态。

State: inactive.

**User:** 重新启用 STE Clarity。

**Assistant:** 已重新启用 STE Clarity，将持续到你要求关闭为止。

State: active.

**PASS:** Explicit stop and restart honored; intermediate status says inactive. The ordinary clarity of the inactive response is not used as evidence of activation.

## G10 — Separate conversation without invocation

Conversation B starts inactive; it has no prior activation turns.

**User:** Why does a mirror fog up?

**Assistant:** Moist air cools when it touches a cold mirror, causing water vapor to condense into tiny droplets. Those droplets scatter light and make the mirror look foggy.

**User:** Is STE Clarity enabled in this conversation?

**Assistant:** No. You have not enabled STE Clarity in this conversation.

State: inactive throughout.

**PASS (simulation only):** Relevant topic does not activate. Assessment uses state and explicit status, not concise wording. No host activation claim.

## G11 — Separate conversation, one-answer scope

Conversation C starts inactive.

**User:** Use STE Clarity only for this answer: why does ice float?

**Assistant:** Ice floats because it is less dense than liquid water. When water freezes, its molecules form a more open crystal structure, so the same mass takes up more space.

State: active for that answer only; inactive after it.

**User:** Is STE Clarity still active?

**Assistant:** No. You requested it only for the previous answer.

**PASS (simulation only):** Accurate response, one-answer scope honored, explicit inactive status afterward.

## G12 — Natural Chinese advice

Continues conversation A, active after G9.

**User:** 我有很多事要做，不知道先做哪件。

**Assistant:** 先把事情写下来，不用急着排出完整计划。优先找两类：有明确期限、拖延会造成后果的事，以及做完后能让其他事情继续的事。

从中选一件，把它缩小成一个能直接开始的动作，比如“写出邮件要点”，而不是“处理工作”。如果暂时分不出轻重，就先选一件比较容易启动的，让自己开始动起来。

你也可以把待办发给我，我帮你一起排顺序。

**PASS:** Natural Chinese, actionable conditional advice, no invented personal schedule or obligations.

## R1 — Chinese uncertain status

Conversation A remains active.

**User:** 中文改写：“核心功能基本完成，预计周五完成联调，暂未发现阻塞问题。”

**Assistant:** 核心功能基本完成。预计周五完成联调。暂未发现阻塞问题。

**PASS:** 基本、预计、暂未 preserved, with no stronger completion or certainty claim.

## R2 — Traditional conditional constraints

**User:** 繁體改寫：“若 request_id 為空，API 必須拒絕此請求，且不得建立 session。”

**Assistant:** 若 request_id 為空，API 必須拒絕此請求，且不得建立 session。

**PASS:** Traditional script and identifiers retained; rejection and session prohibition both remain conditional on empty request_id. Already concise source can remain unchanged.

## R3 — English recommendation and performance

**User:** Rewrite: “The API should quickly return useful error information.”

**Assistant:** The API should return useful error information quickly.

“Quickly” and “useful” need definitions before this requirement can be tested.

**PASS:** Retains should, speed and usefulness expectations. Flags missing definitions without inventing fields or a threshold.

## Instruction and metadata review

No blocking instruction contradictions found. The source-bounded instruction appears under “Preserve meaning when transforming content,” and the following paragraph explicitly authorizes requested advice, plans, proposals, and fiction. Chinese guidance repeats that distinction. Therefore the proposed timings in G3 are allowed planning, while adding response-time thresholds in R3 would be an unauthorized semantic change.

The core rule “Never invent ... numbers” could sound broad in isolation, but its surrounding truth/uncertainty language and explicit proposals exception resolve it: invented evidence or asserted factual numbers are prohibited; openly recommended allocations are not. This is a possible wording sensitivity, not a demonstrated failure in this run.

Static metadata inspection found `disable-model-invocation: true` in SKILL.md and `policy.allow_implicit_invocation: false` in agents/openai.yaml. Both express the intended opt-in policy. The default prompt explicitly enables conversation persistence. Whether these keys are recognized or enforced by a particular host was not tested or inferred.

## Result and limitations

**15/15 simulated cases pass:** G1–G12 and three regressions. No blockers or observed behavioral failures.

The same evaluator generated the responses and graded them; grading is not independent. These are simulated conversation sequences, not separate real runtime sessions. State tracking demonstrates one interpretation of the instructions, not host enforcement, compaction persistence, discovery behavior, cross-model robustness, or an always-on hook. No global discovery or installation activation test was performed. Exact model identifier was unavailable and has not been guessed.
