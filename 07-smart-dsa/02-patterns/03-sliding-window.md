# Sliding Window

## Recognition Signals (how to spot this in <90s)
- Problem asks for the **longest/shortest subarray or substring** satisfying some condition
- Problem asks to **count subarrays** where some property holds (often reduces to window size tracking)
- The condition is monotone: adding an element to the window can only make it "more valid" or "less valid" (never skips between states)
- Problem explicitly mentions "contiguous" elements — that word is the clearest signal
- Brute force is O(n^2) (check every start/end pair) and n is large enough to need O(n)

## Mental Model

A sliding window maintains a contiguous subarray defined by two pointers `left` and `right`. The right pointer expands the window one element at a time; the left pointer shrinks it when the window violates the desired invariant. The key insight is that you never need to move `left` backward — once a starting position is invalid, all smaller windows starting there are also invalid (for maximum problems) or all larger windows are also invalid (for minimum problems). This monotonicity means each element is added and removed at most once: O(n) total work.

The template splits into two flavors. **Variable-size window** (most problems): expand right unconditionally, then shrink from left until the window is valid again, recording the result after each shrink or each expansion depending on whether you want max or min. **Fixed-size window**: advance both pointers together — add `right`, remove `left` only when window size exceeds `k`. The invariant to maintain is what differentiates every problem: it might be "all characters distinct" (use a set or count map), "at most k zeros" (use a counter), or "sum ≤ target" (use a running sum). Identify the invariant before you write a line of code.

## Reusable Python Template

```python
from collections import defaultdict

# --- Variable-size window (longest valid window) ---
def longest_window(s: str) -> int:
    counts: dict[str, int] = defaultdict(int)   # tracks window state
    left = 0
    best = 0

    for right in range(len(s)):
        counts[s[right]] += 1                   # expand: add right element

        while not is_valid(counts):             # shrink until valid
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        best = max(best, right - left + 1)      # window is valid here

    return best


# --- Fixed-size window (window of size k) ---
def fixed_window(nums: list[int], k: int) -> list[int]:
    result: list[int] = []
    window_sum = sum(nums[:k])                  # seed the first window
    result.append(window_sum)

    for i in range(k, len(nums)):
        window_sum += nums[i]                   # add incoming element
        window_sum -= nums[i - k]               # remove outgoing element
        result.append(window_sum)

    return result


def is_valid(counts: dict[str, int]) -> bool:
    # example: all characters in window appear at most once
    return all(v <= 1 for v in counts.values())
    # replace with your invariant check
```

## Common Mistakes

- **Shrinking to a fixed condition instead of a while loop**: if you write `if not valid: shrink by 1`, you may leave the window in an invalid state before recording the result. Always use `while not valid: shrink` so the window is fully valid before you update the answer.
- **Recording the answer inside the shrink loop instead of after**: for longest-window problems, the answer is the window size *after* it becomes valid (post-shrink). Recording inside the loop gives the wrong (smaller) window.
- **Forgetting to clean up zero-count entries from the map**: leaving keys with count 0 in a `dict` means `len(counts)` gives a wrong "number of distinct chars" count. Either `del` them or check `> 0` consistently.
- **Confusing "at most k distinct" with "exactly k distinct"**: "exactly k" is `at_most_k(s, k) - at_most_k(s, k-1)`. This decomposition comes up in counting problems and is easy to miss under pressure.
- **Off-by-one in window size**: the window `[left, right]` has `right - left + 1` elements, not `right - left`. Double-check when computing max length or comparing to `k`.

## Watch Me Solve (I do)

**Problem: Longest Substring Without Repeating Characters (LC 3)**

Given a string `s`, find the length of the longest substring without repeating characters.

---

I see "longest substring" + a condition ("no repeating characters") — that's the clearest possible sliding window signal. The condition is also monotone: once a character repeats, every larger window containing that window will also repeat. So I can shrink from the left to restore validity.

My invariant: **every character in `window[left..right]` appears exactly once.** I'll maintain this using a set (since I only care about membership, not counts).

Design choices:
- **Set vs. dict**: a `set` suffices here — I just need "is this char in the window?" But if I used counts (for more general variants), a `defaultdict(int)` works too. I'll use a set for clarity.
- **When to update the answer**: after the shrink loop, the window is valid, so I update `best = max(best, right - left + 1)`. The answer is outside the shrink loop.
- **Shrink condition**: `while s[right] in window_set: remove s[left]; left++`. I expand right unconditionally, then shrink until the duplicate is gone.

```python
def length_of_longest_substring(s: str) -> int:
    window_chars: set[str] = set()
    left = 0
    best = 0

    for right in range(len(s)):
        # shrink from left until the incoming character can be added
        while s[right] in window_chars:
            window_chars.remove(s[left])
            left += 1

        window_chars.add(s[right])               # expand: right element is now safe
        best = max(best, right - left + 1)       # window is valid; record length

    return best
```

**Complexity:** O(n) time — each character is added and removed at most once. O(min(n, |alphabet|)) space for the set.

**Edge cases I'd call out:**
1. Empty string: the for loop doesn't execute, returns 0. Correct.
2. All same characters (`"aaaa"`): every expansion hits the while, shrinking left to `right`, window is always size 1. Returns 1. Correct.
3. All unique characters (`"abcde"`): the while loop never fires, window grows to full length. Correct.

**Alternative: hash map for O(n) with fewer iterations.** Instead of a set, store `char → last seen index`. When a repeat is found, jump `left` directly to `max(left, last_seen[s[right]] + 1)` — skipping multiple shrink steps. It's faster in practice but slightly harder to reason about (the `max` guards against moving left backward when a char was seen before the current window). For an interview I'd present the set version first (clearer invariant), then offer the map optimization if asked.

```python
def length_of_longest_substring_map(s: str) -> int:
    last_seen: dict[str, int] = {}
    left = 0
    best = 0

    for right, c in enumerate(s):
        if c in last_seen and last_seen[c] >= left:
            left = last_seen[c] + 1              # jump past the previous occurrence
        last_seen[c] = right
        best = max(best, right - left + 1)

    return best
```

Both are O(n). In an interview, lead with whichever you can explain the invariant of most confidently.
