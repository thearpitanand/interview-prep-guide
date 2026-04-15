# AI Reviewer Prompt

After each mock, paste this prompt into a Claude session. Fill in the two placeholders and send.

---

## How to Use This

1. Open a new Claude conversation (claude.ai or the CLI — does not matter).
2. Copy the prompt below exactly as written.
3. Replace `<paste problem statement here>` with the full LeetCode problem statement.
4. Replace `<paste Fathom transcript here>` with the exported Fathom transcript — raw text, no editing.
5. Send it.
6. When the response arrives:
   - Log all 5 axis scores in `mock-log.md`.
   - Copy the "top 2 behaviors to practice" into the last column of your log row.
   - Pick one behavior to drill in the next 5 daily problems. Add a note to the relevant week file.
   - Do not optimize for the score — optimize for making the next mock 1 point better on your weakest axis.

---

## The Prompt

```
You are a FAANG staff engineer running a post-mock interview review.

Problem statement (paste below):
<paste problem statement here>

My 45-minute Fathom transcript (paste below):
<paste Fathom transcript here>

Grade me against this 5-axis rubric. For each axis, provide:
1. A score out of 5
2. One concrete thing I did well (quote the transcript if possible)
3. One concrete thing to fix (specific, actionable, not generic)

The 5 axes are:

**Axis 1 — Problem Clarification**
Did I ask disambiguating questions before writing any code?
- Score 1: No clarifying questions at all; dived straight into coding.
- Score 3: Asked one question but skipped obvious ambiguities.
- Score 5: Asked at least 2 targeted questions, confirmed I/O shape, restated the problem before coding.

**Axis 2 — Communication**
Did I narrate my pattern match and plan before touching code?
- Score 1: Went silent and started coding with no spoken plan.
- Score 3: Mentioned the approach mid-way through coding, or narrated inconsistently.
- Score 5: Named the pattern and signal before opening the editor, described full plan with complexity, narrated every key decision, never silent > 15 seconds.

**Axis 3 — Optimization Thinking**
Did I state brute force, its complexity, and the reasoning step to optimal?
- Score 1: No brute force mentioned; jumped to a solution with no complexity analysis.
- Score 3: Named brute force but skipped complexity or made the transition to optimal implicit.
- Score 5: Named brute force + complexity, identified the bottleneck, articulated the optimization insight, confirmed new complexity and trade-offs.

**Axis 4 — Edge Cases**
Were edge cases enumerated before writing tests, not discovered after?
- Score 1: Ran only the provided example; no edge cases mentioned.
- Score 3: Named 1–2 edge cases but missed category-specific ones, or mentioned them only after coding.
- Score 5: Listed 3+ category-appropriate edge cases before implementing; traced through 2 of them during testing.

**Axis 5 — Recovery**
When I got stuck, did I pivot cleanly or spiral?
- Score 1: Went silent > 2 minutes with no recovery attempt; no hint requested.
- Score 3: Attempted recovery but took 3–4+ minutes; pivot was unstructured.
- Score 5: Applied the recovery ladder: restated at 2 min, described brute force at 5 min, asked for hint at 10 min; each pivot was clean and immediate.

After scoring all 5 axes, end your response with:

**Top 2 behaviors to practice in my next mock:**
[List exactly 2 specific, concrete behaviors — not general advice.]
```

---

## What to Do With the Output

| Step | Action |
|------|--------|
| 1 | Fill in all 5 scores and the "top 2 behaviors" in `mock-log.md` for this mock row. |
| 2 | Pick the lower of the two axes the reviewer flagged. That is your drill focus for the coming week. |
| 3 | In the relevant `03-weekly/week-N.md`, add a note under the next 3–5 daily problem entries: "Drill: [behavior]." This keeps it visible during daily practice, not just during mocks. |
| 4 | If the same axis scores 3 or below for two consecutive mocks, re-read the corresponding section of `01-method/interview-framework.md` before Mock #(N+1). |
| 5 | Do not obsess over the total score after Mock #1 or #2. Early mocks are protocol calibration, not performance signals. |
