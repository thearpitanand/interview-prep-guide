# Arrays & Hashing

## Recognition Signals (how to spot this in <90s)
- Problem asks for a pair, group, or count where equality or frequency matters (anagram, duplicate, sum target)
- You need O(1) lookup for "have I seen this before?" or "how many times?"
- Problem says "unsorted array" and optimal solution must beat O(n log n) — that means hashing, not sorting
- Problem involves grouping elements by some derived key (e.g. sorted form, character count, remainder)
- Constraints are large (n up to 10^5 or 10^6) and O(n^2) brute force would TLE

## Mental Model

A hash map trades space for time. You make one pass through the array and, for each element, ask a question about something you've already seen — storing the answer so you don't have to look back. The invariant is simple: after processing index `i`, the map contains exactly the information you need to answer the question for index `i+1` through `n-1`. This is why you often build the map and query it in the same pass rather than two separate passes.

Grouping problems extend this idea: instead of a key → bool/count map, you build a key → list map where the key is some canonical form (sorted tuple, frozenset of counts, etc.). Two elements that map to the same canonical key belong to the same group. When you see a grouping problem, immediately ask: "what is the invariant that all members of a group share, and can I compute it cheaply?" That invariant becomes your hash key.

## Reusable Python Template

```python
from collections import defaultdict

def arrays_hashing_template(nums: list[int]) -> ...:
    # --- Pattern 1: existence / complement lookup ---
    seen: dict[int, int] = {}           # value → index (or True for membership)
    for i, x in enumerate(nums):
        complement = target - x         # or whatever you're looking for
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i                     # store AFTER lookup to avoid using self

    # --- Pattern 2: frequency count ---
    freq: dict[int, int] = defaultdict(int)
    for x in nums:
        freq[x] += 1
    # then sort by freq, filter, etc.

    # --- Pattern 3: group by canonical key ---
    groups: dict[tuple, list] = defaultdict(list)
    for x in nums:
        key = canonical(x)              # e.g. tuple(sorted(str(x))) or tuple(sorted(x))
        groups[key].append(x)
    return list(groups.values())

def canonical(s: str) -> tuple[int, ...]:
    # example: character frequency tuple (for anagram grouping)
    count = [0] * 26
    for c in s:
        count[ord(c) - ord('a')] += 1
    return tuple(count)
```

## Common Mistakes

- **Storing index before lookup**: writing `seen[x] = i` before checking `complement in seen` means you might match an element with itself (e.g. Two Sum with target=6 and `nums[2]=3`). Always check first, store after.
- **Using a list instead of a set/dict for lookup**: `if x in some_list` is O(n) — the whole point of hashing is O(1). Use `set` or `dict`.
- **Forgetting that `defaultdict` still raises on `.pop()` of missing key**: use `d.get(key, default)` or check membership first when you need safe reads.
- **Sorting to group when you should hash**: sorting a string to check anagram is O(k log k). A 26-bucket character-count array is O(k) and works as a hashable key — prefer it when k (string length) is large or called many times.
- **Off-by-one on frequency problems**: when the answer depends on count thresholds (e.g. "appears more than n/2 times"), build the full frequency map first, then filter — don't try to decide mid-pass.

## Watch Me Solve (I do)

**Problem: Two Sum (LC 1)**

Given an array of integers `nums` and an integer `target`, return indices of the two numbers that add up to `target`. Exactly one solution exists; do not use the same element twice.

---

I read the problem and immediately notice: given a number `x`, I want to know if `target - x` exists somewhere in the array and, if so, where. That's a lookup question — I need O(1) access to "have I seen this value, and at what index?" That signals a hash map.

My first instinct is always to check whether sorting would work. It would — sort + two pointers gives O(n log n). But the problem asks for *indices*, and sorting destroys original indices unless I track them separately. Hashing is cleaner and faster: O(n) time, O(n) space.

The key design choice: do I build the map first (two passes) or build and query simultaneously (one pass)? One pass is strictly better — I can query the map for the complement *before* inserting the current element. This automatically prevents matching an element with itself. Here's the reasoning: at index `i`, my map contains only elements at indices `0..i-1`. So if `target - nums[i]` is in the map, that hit came from a strictly earlier index — a valid, distinct pair.

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}        # value → original index

    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:       # found a valid pair
            return [seen[complement], i]
        seen[x] = i                  # insert AFTER lookup

    return []                        # problem guarantees one solution; unreachable
```

**Complexity:** O(n) time — one pass, O(1) hash ops per element. O(n) space — map grows up to n entries.

**Edge cases I'd flag in an interview:**
1. Duplicate values: `nums = [3, 3]`, `target = 6`. Works correctly — at index 0 we insert `seen[3] = 0`; at index 1, `complement = 3` hits `seen`, returning `[0, 1]`.
2. Negative numbers: no issue — we're just hashing integers.
3. The problem guarantees exactly one solution, so I don't need to handle zero or multiple answers. If it didn't, I'd ask the interviewer before coding.

**If asked to optimize space:** you can't beat O(n) here without losing the O(n) time — you'd have to fall back to the sorted two-pointer approach (which needs the index trick). Always state the trade-off explicitly.
