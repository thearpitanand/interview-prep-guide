# Interview Framework — UMPIRE

Six steps, every problem, every mock. Drill until it's automatic.
The goal: interviewers should never wonder "where is this person in the problem?"

---

## The UMPIRE Sequence

### U — Understand (2–3 min)

**What you do:**
- Restate the problem in your own words in one sentence.
- Ask exactly 2 clarifying questions. Not 0 (signals you're rushing), not 5 (signals you're stalling).
- Confirm input/output shape and at least one constraint.

**What to say:**
> "Let me restate: I'm given [input], and I need to return [output]. A couple of questions —
> can the input be empty? And are values guaranteed distinct, or can there be duplicates?"

**What interviewers look for:**
They're checking that you won't code for 20 minutes then say "oh, I assumed no duplicates."
Clarification questions signal senior instinct — you've been burned by edge cases before.

**Common clarifying questions by input type:**

| Input type | Questions worth asking |
|---|---|
| Array/string | Can it be empty? Are values sorted? Duplicates allowed? |
| Graph | Directed or undirected? Cycles possible? Connected? |
| Integer | Can it be negative? 32-bit overflow risk? |
| Tree | Is it a BST? Balanced? Can nodes have duplicate values? |

---

### M — Match (1 min)

**What you do:**
- Say the pattern out loud. Use the recognition signals from `pattern-recognition.md`.
- State why — one signal from the problem.

**What to say:**
> "This smells like [pattern] because [one concrete signal]."

Examples:
> "This smells like Sliding Window because we need the longest substring satisfying a constraint — that's a variable-size window problem."

> "This smells like BFS because we need minimum steps in an unweighted grid."

**What interviewers look for:**
They want to see you match before you implement. A senior engineer who names the pattern
before touching code signals pattern fluency, not luck. Do not say "let me just think through
this" and start coding — that's a red flag.

---

### P — Plan (2–3 min)

**What you do:**
- Describe the approach in English. No pseudocode, no code.
- State time and space complexity upfront.
- Get explicit buy-in before writing a single line: "Does that approach make sense to you?"

**What to say:**
> "My plan: [brute force in one sentence]. That's O(n^2). I can optimize by [strategy],
> which brings it to O(n log n) / O(n). I'll use [data structure] to [purpose].
> Does this approach make sense before I start coding?"

**What interviewers look for:**
- Did you mention brute force first? That shows you understand the problem space, not just the trick.
- Did you state complexity before coding? That shows you're thinking about correctness and performance together.
- Did you get buy-in? That prevents 20 minutes of silent coding in the wrong direction.

---

### I — Implement (10–15 min)

**What you do:**
- Write clean, readable code. Name variables clearly.
- Narrate each significant block in one sentence as you write it.
- Do not apologize for syntax pauses. Say "let me check the heap API" and move on.

**What to say while coding:**
> "I'll initialize a hash map to track... Now I iterate — when I see a duplicate, I shrink
> the window from the left... I'll track the max here..."

**What interviewers look for:**
- Can you translate a plan into code without re-planning?
- Is your code readable without explanation?
- Are you narrating the *why*, not just the *what*?

**Traps to avoid:**
- Don't code silently for more than 60 seconds.
- Don't refactor mid-implementation — finish first, clean after.
- Don't forget to handle the edge case you identified in U.

---

### R — Review (2–3 min)

**What you do:**
- Dry-run the given example through your code, line by line. Trace variables aloud.
- Then test one edge case you identified in U (empty input, single element, all same values).

**What to say:**
> "Let me trace through the example: input is [X], so at step 1 I have [state]...
> At step 2... result is [Y]. That matches. Now let me check the empty input case —
> my loop doesn't execute, I return [Z], which is correct."

**What interviewers look for:**
- Do you catch your own bugs before they ask?
- Do you test edge cases proactively?
- Is your trace disciplined (state variables, not just "it looks right")?

---

### E — Evaluate (1 min)

**What you do:**
- State final time and space complexity.
- Name one optimization you'd make given more time.

**What to say:**
> "Time complexity is O(n log n) due to the sort, space is O(n) for the hash map.
> If we needed to optimize space, we could [approach], but it would add code complexity
> that isn't worth it for this input size."

**What interviewers look for:**
- Can you reason about complexity without prompting?
- Do you know the tradeoffs, not just the answer?

---

## Recovery Rules When Stuck

Apply in sequence. Don't skip levels.

| Time stuck | Action |
|---|---|
| **2 min** | Stop coding. Restate the problem aloud in one sentence. Sometimes the restatement reveals what you're missing. |
| **5 min** | Describe brute force aloud, even if it's O(n^3). Say: "I know this is slow, but let me describe the naive approach and we can optimize." Interviewers want signal — silence gives them nothing. |
| **10 min** | Ask for a hint explicitly. Say: "I've tried [X] and [Y]. Could you give me a nudge on the data structure?" Silent stuckness is the worst outcome. A student who asks well is better than one who spirals. |

**What "spiraling" looks like** (avoid this):
- Repeatedly writing the same approach with small variations.
- Going quiet for 3+ minutes.
- Saying "I think this is right" and submitting untested code.
- Apologizing instead of restating and re-planning.

---

## Full Timing Reference

| Step | Target time | If you go over |
|---|---|---|
| U — Understand | 2–3 min | Cut to 1 clarifying question |
| M — Match | 1 min | If no match, jump to P with brute force |
| P — Plan | 2–3 min | Cap at 3 min; interviewers get impatient |
| I — Implement | 10–15 min | Prioritize working over clean; refactor at the end |
| R — Review | 2–3 min | At minimum, trace one example |
| E — Evaluate | 1 min | Never skip — it's the easiest free signal |
| **Total** | **~20–25 min** | Leaves buffer for a second problem or deep follow-ups |

---

## Self-Mock Checklist

Before each mock in Weeks 5–8, run through this checklist:

- [ ] Timer set to 45 min
- [ ] Fathom running
- [ ] Narrating out loud from the first word (do not read silently)
- [ ] Named the pattern before coding
- [ ] Stated complexity before implementing
- [ ] Got buy-in on plan
- [ ] Traced at least one example in Review
- [ ] Stated one optimization in Evaluate

After the mock: paste transcript into the AI-reviewer prompt in `05-mocks/ai-reviewer-prompt.md`.
The rubric score on the **Communication** axis directly reflects how well you ran UMPIRE.
