# Week 3 — Stack / Monotonic Stack + Linked List

**Theme:** First contact with stack-based patterns and pointer manipulation on linear structures.

**Why this matters for target companies:** Monotonic stack is a reliable signal separating mid-level from senior candidates at Dream11, Cars24, Unacademy, and Razorpay. Interviewers use Largest Rectangle or Daily Temperatures as a filter because most candidates recognize "use a stack" but cannot articulate the invariant. Linked list problems (cycle, reorder, LRU Cache) appear in at least one round at nearly every product company — they test pointer discipline and in-place mutation without extra memory.

---

## Week 3 Schedule

| Day | P1 | P2 | Pattern | Marker |
|-----|----|----|---------|----- --|
| 15 | Valid Parentheses (E, 15m) | Min Stack (M, 20m) | Stack basics | 🤝 P1 |
| 16 | Evaluate RPN (M, 25m) | Daily Temperatures (M, 25m) | Monotonic stack intro | 🤝 P2 |
| 17 | Largest Rectangle in Histogram (H, 40m) | Car Fleet (M, 25m) | Monotonic stack hard | 🎯 both |
| 18 | Reverse Linked List (E, 15m) | Merge Two Sorted Lists (E, 15m) | LL pointer basics | 🤝 P1 |
| 19 | Linked List Cycle (M, 20m) | Reorder List (M, 30m) | Fast/slow pointers | 🎯 both |
| 20 (Sat) | LRU Cache (M, 35m) | Rev × 2 | Hash + doubly LL | 🎯 P1 |
| 21 (Sun) | Flex / catch-up | — | — | — |

---

## Day 15 — Valid Parentheses + Min Stack

**New pattern today? Yes — read `02-patterns/05-stack-monotonic.md` before starting.**

---

### Problem 1 🤝 — Valid Parentheses (LC 20)

**Stub:** `07-smart-dsa/03-problems/d15-p1_valid_parentheses.py`

**Intuition:** A stack lets you match each closing bracket against the most recent unmatched open bracket — LIFO order mirrors the nesting structure exactly.

**Scaffolded outline (we do together):**
1. Create an empty stack and a mapping `{')': '(', ']': '[', '}': '{'}`.
2. Iterate each character: if it's an open bracket, push it; if it's a close bracket, check that the top of the stack matches the expected open bracket (use the map).
3. If the stack top doesn't match, or the stack is empty when you need to pop, return `False`.
4. After the loop, return `True` only if the stack is empty (all opens were matched).

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 16

---

### Problem 2 🎯 — Min Stack (LC 155)

**Stub:** `07-smart-dsa/03-problems/d15-p2_min_stack.py`

**Intuition:** Maintain a second stack that tracks the running minimum — each push records the new minimum so `get_min()` is always O(1) without scanning.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 16

---

## Day 16 — Evaluate RPN + Daily Temperatures

**New pattern today? Yes (Monotonic Stack) — read the monotonic-stack section of `02-patterns/05-stack-monotonic.md` before starting P2.**

---

### Problem 1 🎯 — Evaluate RPN (LC 150)

**Stub:** `07-smart-dsa/03-problems/d16-p1_evaluate_rpn.py`

**Intuition:** A stack naturally accumulates operands; when you hit an operator, pop the top two, apply the operation, and push the result back.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 17

---

### Problem 2 🤝 — Daily Temperatures (LC 739)

**Stub:** `07-smart-dsa/03-problems/d16-p2_daily_temperatures.py`

**Intuition:** A monotonic decreasing stack stores indices of days we haven't found a warmer day for yet; when a warmer day arrives it resolves all stacked days in one sweep.

**Scaffolded outline (we do together):**
1. Initialize `result = [0] * len(temps)` and an empty stack (stores indices).
2. For each index `i`, while the stack is non-empty and `temps[i] > temps[stack[-1]]`, pop index `j` from the stack and set `result[j] = i - j`.
3. Push `i` onto the stack.
4. Any index remaining in the stack at the end has no warmer day — they stay 0.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 17

---

## Day 17 — Largest Rectangle in Histogram + Car Fleet

**New pattern today? No — monotonic stack continuation.**

---

### Problem 1 🎯 — Largest Rectangle in Histogram (LC 84)

**Stub:** `07-smart-dsa/03-problems/d17-p1_largest_rectangle_histogram.py`

**Intuition:** Maintain a monotonic increasing stack of (index, height) pairs; when a shorter bar is encountered, pop and compute the rectangle that could have extended left to the popped bar's position.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 18

---

### Problem 2 🎯 — Car Fleet (LC 853)

**Stub:** `07-smart-dsa/03-problems/d17-p2_car_fleet.py`

**Intuition:** Sort cars by position descending; compute each car's time to reach the target and use a stack to track distinct fleets — a faster car that catches a slower one joins its fleet.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 18

---

## Day 18 — Reverse Linked List + Merge Two Sorted Lists

**New pattern today? Yes (Linked List) — read `02-patterns/06-linked-list.md` before starting.**

---

### Problem 1 🤝 — Reverse Linked List (LC 206)

**Stub:** `07-smart-dsa/03-problems/d18-p1_reverse_linked_list.py`

**Intuition:** Three pointers (`prev`, `curr`, `next`) walk the list once, rewiring each `.next` in place — no extra memory needed.

**Scaffolded outline (we do together):**
1. Initialize `prev = None`, `curr = head`.
2. While `curr` is not `None`: save `next_node = curr.next`, set `curr.next = prev`, advance `prev = curr` and `curr = next_node`.
3. After the loop `prev` is the new head — return it.
4. Edge cases: empty list and single-node list both fall through the loop correctly.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 19

---

### Problem 2 🎯 — Merge Two Sorted Lists (LC 21)

**Stub:** `07-smart-dsa/03-problems/d18-p2_merge_two_sorted_lists.py`

**Intuition:** A dummy head node eliminates the edge case of choosing the first node; compare front nodes of each list and attach the smaller one, advancing that pointer.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 19

---

## Day 19 — Linked List Cycle + Reorder List

**New pattern today? No — fast/slow pointer variant of linked list.**

---

### Problem 1 🎯 — Linked List Cycle (LC 141)

**Stub:** `07-smart-dsa/03-problems/d19-p1_linked_list_cycle.py`

**Intuition:** Floyd's tortoise-and-hare: a slow pointer moves one step and a fast pointer moves two; if they ever meet, there's a cycle.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 20

---

### Problem 2 🎯 — Reorder List (LC 143)

**Stub:** `07-smart-dsa/03-problems/d19-p2_reorder_list.py`

**Intuition:** Find the midpoint with fast/slow pointers, reverse the second half in place, then interleave the two halves — three sub-problems you already know.

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 20

---

## Day 20 (Sat) — LRU Cache + Revision × 2

**New pattern today? No — hash map + doubly linked list composition.**

---

### Problem 1 🎯 — LRU Cache (LC 146)

**Stub:** `07-smart-dsa/03-problems/d20-p1_lru_cache.py`

**Intuition:** A hash map gives O(1) key lookup while a doubly linked list maintains recency order; on every access move the node to the head and on eviction remove from the tail — both O(1).

**Feynman slot:**
- Pattern: ...
- Invariant: ...
- Where I'd trip: ...

**Log:** solved __ / budget hit __ / confidence __/5 / next review: Day 21

---

### Revision × 2

Pull the two problems due per your revision schedule (check `04-revision/review-log.md`). Re-solve from a blank file with the timer running.

---

## Week 3 Revision Reminder

By the end of this week, the following problems should be in your spaced-repetition queue. Verify they appear in `04-revision/review-log.md`:

- Day 15: Valid Parentheses, Min Stack
- Day 16: Evaluate RPN, Daily Temperatures
- Day 17: Largest Rectangle in Histogram, Car Fleet
- Day 18: Reverse Linked List, Merge Two Sorted Lists
- Day 19: Linked List Cycle, Reorder List
- Day 20: LRU Cache

Confidence < 3 on any re-solve → reset interval to Day+1 and re-solve from scratch tomorrow.
