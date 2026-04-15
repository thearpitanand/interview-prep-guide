# Mock Rubric — 5-Axis Scoring

Each axis is scored /5. Use the anchor descriptions at 1, 3, and 5 to calibrate. Interpolate for 2 and 4.

Total: /25. A FAANG-pass performance is ≥ 20/25 with no axis below 3.

---

## Axis 1 — Problem Clarification

*Did you ask disambiguating questions before touching code?*

| Score | Anchor |
|-------|--------|
| 1 | Completely absent. Dove straight into coding with no clarifying questions. Assumed all constraints without stating them aloud. |
| 3 | Present but inconsistent. Asked one question (e.g. confirmed return type) but skipped obvious ambiguities (e.g. whether input is sorted, whether duplicates are possible, whether `n` can be 0). Restated the problem passively rather than probing it. |
| 5 | Strong signal — FAANG pass. Asked at least 2 targeted, non-trivial clarifying questions before writing a single line. Confirmed input shape, edge-case constraints, and expected output format. Restated the problem in own words and got explicit confirmation before proceeding. |

---

## Axis 2 — Communication

*Did you narrate the pattern match and plan before touching code?*

| Score | Anchor |
|-------|--------|
| 1 | Completely absent. Went silent and started coding immediately. No spoken plan, no pattern identification, no explanation of intent. Interviewer would have no idea what you were doing. |
| 3 | Present but inconsistent. Mentioned the approach after starting to code, or narrated some lines but went silent on the hard parts. Pattern name was stated but not the signal that led to it. |
| 5 | Strong signal — FAANG pass. Named the pattern and the signal out loud before opening the editor. Described the full plan in plain English and stated complexity before writing code. Narrated every non-trivial implementation decision as it happened. Never silent for more than 15 seconds. |

---

## Axis 3 — Optimization Thinking

*Did you state brute force, its complexity, and the step to optimal?*

| Score | Anchor |
|-------|--------|
| 1 | Completely absent. Jumped to (or attempted) an optimized solution without naming the brute force. No complexity mentioned at any point. |
| 3 | Present but inconsistent. Named the brute force but skipped its complexity, or stated the optimal complexity but not why it is better. The transition from brute to optimal was implicit ("I'll use a hash map") rather than reasoned ("the bottleneck is the O(n²) inner loop; a hash map removes it to O(n)"). |
| 5 | Strong signal — FAANG pass. Explicitly described brute force and its time/space complexity before mentioning any optimization. Named the bottleneck. Articulated the optimization insight in one clear sentence. Confirmed the new complexity and any trade-offs (e.g. O(n) space for O(n) time). |

---

## Axis 4 — Edge Cases

*Were edge cases enumerated before writing tests, not after?*

| Score | Anchor |
|-------|--------|
| 1 | Completely absent. Ran only the provided example. No mention of edge cases at any point, or edge cases named only after the solution was written as an afterthought. |
| 3 | Present but inconsistent. Named one or two edge cases (e.g. empty input) but missed category-specific ones (e.g. single element, all duplicates, negative numbers, integer overflow). Enumerated them during testing rather than before implementing. |
| 5 | Strong signal — FAANG pass. Before implementing, listed at least 3 category-appropriate edge cases out loud (empty, single element, all-same, boundary values, etc.). Traced the solution through at least two of them during the test phase. Did not discover new edge cases only after the code was written. |

---

## Axis 5 — Recovery

*When stuck, did you pivot cleanly or spiral?*

| Score | Anchor |
|-------|--------|
| 1 | Completely absent. Hit a wall and went silent for more than 2 minutes. Made no attempt to restate the problem, fall back to brute force, or ask for a hint. Spiraled by re-reading the problem statement repeatedly without visible progress. |
| 3 | Present but inconsistent. Attempted a recovery move (e.g. restated the problem or described brute force) but took too long to execute it — more than 3–4 minutes of visible struggle before pivoting. Recovery was reactive and unstructured. |
| 5 | Strong signal — FAANG pass. Applied the recovery ladder proactively: at 2 min stuck, restated the problem aloud; at 5 min stuck, described the brute force even if ugly; at 10 min stuck, asked explicitly for a hint. Each pivot was clean — no apology spiral, no silence, no abandoning the prior plan without explaining why. |

---

## Score Interpretation

| Total | Signal |
|-------|--------|
| 23–25 | Strong hire signal. Ready for real loops. |
| 20–22 | Likely pass with polish. Drill the weak axis before the next mock. |
| 16–19 | Mixed signal. One axis is dragging the score — target it in next week's daily problems. |
| 12–15 | High risk. Two or more axes are weak. Re-read `01-method/interview-framework.md` and run a dry-run mock before the next scheduled mock. |
| < 12  | Escalate to a human mock partner. Solo mocks are not providing enough signal. |
