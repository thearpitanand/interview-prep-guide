# Review Log

Maintain this table as you progress. Update it immediately after each review — do not batch-update.

Rules for filling columns:

- **First Solved (day):** the day number you first completed the problem (e.g. `1`, `8`, `22`).
- **Last Review (day):** the day number of your most recent review. On first solve this equals First Solved.
- **Next Due (day):** computed from the interval table in `revision-schedule.md` (Day+1, Day+3, Day+7, Day+21). Reset to Last Review + 1 if confidence dropped below 3.
- **Confidence 1–5:** your score from the most recent review or solve. See the confidence scale in `revision-schedule.md`.
- **Notes:** one short phrase — what tripped you up, which edge case you missed, or "clean solve". Keep it to ≤ 10 words.

---

| Problem | Pattern | First Solved (day) | Last Review (day) | Next Due (day) | Confidence 1-5 | Notes |
|---------|---------|-------------------|------------------|---------------|---------------|-------|
| Two Sum | Hash Map | 1 | 1 | 2 | 4 | Clean. Remember index not value. |
| Valid Anagram | Hash Map / Counting | 1 | 1 | 2 | 5 | Trivial after Two Sum warmup. |
| Group Anagrams | Hash Map + Sort key | 2 | 2 | 3 | 3 | Forgot tuple(sorted(s)) as key first pass. |
| Top K Frequent Elements | Hash Map + Heap | 2 | 2 | 3 | 3 | Heap push direction tripped me up. |

---

> **How to add rows:**
> After solving each new problem on its scheduled day, append a row with First Solved = today's day number, Last Review = same, Next Due = day + 1, and your honest confidence score.
>
> After each review, find the existing row and update Last Review, Next Due (advance the interval), and Confidence. Do not create a duplicate row.
>
> To pull today's revision queue: filter this table for rows where `Next Due (day)` ≤ today's day number. Sort ascending. Work top-to-bottom.
