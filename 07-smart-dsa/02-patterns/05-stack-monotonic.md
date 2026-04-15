# Stack & Monotonic Stack

## Recognition Signals (how to spot this in <90s)

### Regular Stack Signals
- Problem involves **matching, balancing, or nesting** (brackets, tags, operators)
- You need the **most recently seen** element again (LIFO access pattern)
- "Valid" or "evaluate" with paired characters
- Recursive structure you want to flatten iteratively

### Monotonic Stack Signals
- "Next greater element", "next smaller element", "previous greater/smaller"
- **Span, temperature, histogram, water** — any problem about how far until something changes
- Result for index `i` depends on a **future or past element that breaks a monotone order**
- Brute force is O(n²) nested loops comparing each element to every other

## Mental Model

A regular stack is a scratchpad for unfinished business. You push something when you encounter it and pop it when you find the thing that "closes" it — a matching bracket, an operator's operand, or an expression boundary. The invariant is simple: the top of the stack is always the most recent unresolved item.

A monotonic stack maintains a stricter invariant: elements in the stack are always in non-increasing (or non-decreasing) order. When a new element arrives that violates the order, you pop everything it beats. The key insight is that every element you pop has found its answer — the new element is the first one to beat it. You never need to compare that popped element to anything again. This collapses an O(n²) brute force into O(n): each element is pushed and popped at most once.

## Reusable Python Template

```python
from collections import deque

# --- Regular Stack (matching/balancing) ---
def stack_matching_template(s: str) -> bool:
    stack: list[str] = []
    pair = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in '({[':
            stack.append(ch)
        elif ch in ')}]':
            if not stack or stack[-1] != pair[ch]:
                return False
            stack.pop()
    return len(stack) == 0


# --- Monotonic Stack (next greater element pattern) ---
def monotonic_stack_template(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [-1] * n          # default: no greater element found
    stack: list[int] = []      # stores INDICES, not values

    for i in range(n):
        # pop everything the current element beats
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]   # nums[i] is the "next greater" for idx
        stack.append(i)

    # anything left in stack has no next greater → stays -1
    return result


# --- Monotonic Stack (previous smaller / span pattern) ---
def previous_smaller_template(nums: list[int]) -> list[int]:
    result: list[int] = []
    stack: list[int] = []   # stores VALUES in non-decreasing order

    for x in nums:
        while stack and stack[-1] >= x:
            stack.pop()
        result.append(stack[-1] if stack else -1)
        stack.append(x)

    return result
```

## Common Mistakes

- **Storing values instead of indices**: You almost always need the index later (for span calculations, result arrays). Push indices; read `nums[stack[-1]]` for the value.
- **Wrong monotone direction**: "Next greater" needs a stack that stays non-increasing (pop when you see something bigger). Drawing two examples before coding prevents this.
- **Forgetting leftovers**: After the loop, elements still in the stack have no answer. Handle them explicitly (assign `-1`, `0`, or `n` depending on the problem).
- **Off-by-one in span problems**: The span to the left is `i - stack[-1]` after popping, not `i - stack[-1] - 1`. Trace through index 0 by hand.
- **Using a deque when a list works**: Python's `list` with `.append()` / `.pop()` is a perfectly fast stack. No need for `collections.deque` unless you also need popleft.

## Watch Me Solve (I do)

**Problem: Daily Temperatures (LC 739)**

Given an integer array `temperatures`, return an array `answer` such that `answer[i]` is the number of days you have to wait after day `i` to get a warmer temperature. If there is no future day with a warmer temperature, `answer[i] = 0`.

---

I read this and immediately think: for each day, I need the *next day with a higher temperature*. The brute force is obvious — nested loops, O(n²). But with n up to 100,000, that's too slow.

The phrase "next greater" is a flashing neon sign for a monotonic stack. Here is my mental model for this problem: I walk through the days left to right. I keep a stack of days where I haven't yet found a warmer day. The moment I see a temperature that beats the top of the stack, that stack entry has its answer: the current day.

Let me trace through `[73, 74, 75, 71, 69, 72, 76, 73]`:

- Day 0 (73): stack empty, push index 0. Stack: [0]
- Day 1 (74): 74 > 73 (top). Pop index 0, answer[0] = 1 - 0 = 1. Push 1. Stack: [1]
- Day 2 (75): 75 > 74. Pop 1, answer[1] = 2 - 1 = 1. Push 2. Stack: [2]
- Day 3 (71): 71 < 75. Just push. Stack: [2, 3]
- Day 4 (69): 69 < 71. Push. Stack: [2, 3, 4]
- Day 5 (72): 72 > 69 → pop 4, answer[4] = 5 - 4 = 1. 72 > 71 → pop 3, answer[3] = 5 - 3 = 2. 72 < 75 → stop. Push 5. Stack: [2, 5]
- Day 6 (76): 76 > 72 → pop 5, answer[5] = 6 - 5 = 1. 76 > 75 → pop 2, answer[2] = 6 - 2 = 4. Stack empty, push 6. Stack: [6]
- Day 7 (73): 73 < 76. Push. Stack: [6, 7]

Loop ends. Indices 6 and 7 are still in the stack — no warmer day found, answer stays 0.

Final: `[1, 1, 4, 2, 1, 1, 0, 0]` ✓

Now I code it up cleanly:

```python
def daily_temperatures(temperatures: list[int]) -> list[int]:
    n = len(temperatures)
    answer = [0] * n
    stack: list[int] = []  # indices of days awaiting a warmer day

    for i, temp in enumerate(temperatures):
        # while current day is warmer than the day at top of stack
        while stack and temp > temperatures[stack[-1]]:
            prev_day = stack.pop()
            answer[prev_day] = i - prev_day  # days waited
        stack.append(i)

    # remaining indices in stack never found a warmer day → answer stays 0
    return answer
```

**Complexity:** O(n) time — each index is pushed once and popped once. O(n) space for the stack in the worst case (strictly decreasing temperatures).

**Edge cases I'd mention to an interviewer:**
- Single element → loop runs once, pushes, ends. Returns `[0]`. Correct.
- Strictly increasing → every element pops the one before it immediately. All answers are 1. Stack never grows past size 1.
- Strictly decreasing → nothing ever gets popped during the loop. Every element stays in the stack and gets answer 0. Stack grows to size n.
