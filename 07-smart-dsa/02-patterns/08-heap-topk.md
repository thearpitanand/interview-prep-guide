# Heap & Top-K

## Recognition Signals (how to spot this in <90s)
- Problem asks for the **k-th largest/smallest**, **top K**, or **K closest**
- You need to repeatedly extract the minimum or maximum from a dynamic set
- "Median from a stream", "merge K sorted lists" — you need ordered access without full sorting
- Brute force would sort everything (O(n log n)) but you only need K results
- The dataset is too large to sort, or elements arrive **online** (one at a time)

## Mental Model

A heap is a data structure that always gives you the min (or max) in O(1) and lets you insert or remove in O(log n). Python's `heapq` module is a min-heap: `heapq.heappop()` always returns the smallest element. To get a max-heap, negate your values on the way in and negate again on the way out.

The core Top-K insight: you don't need all n elements sorted — you only need to maintain the K best. A min-heap of size K does exactly this. As you scan the input, push each element in. If the heap grows beyond K, pop the smallest. After the full scan, the heap contains exactly the K largest elements and the root is the K-th largest. This runs in O(n log k) — far better than O(n log n) sort when k is small. Invert the logic (max-heap, pop the largest) for K smallest.

## Reusable Python Template

```python
import heapq
from typing import Any


# --- Fixed-size min-heap for Top-K largest ---
def top_k_largest(nums: list[int], k: int) -> list[int]:
    heap: list[int] = []
    for num in nums:
        heapq.heappush(heap, num)       # push onto min-heap
        if len(heap) > k:
            heapq.heappop(heap)         # evict the smallest, keeping K largest
    return heap  # heap[0] is the K-th largest


# --- Max-heap via negation ---
def max_heap_example(nums: list[int]) -> int:
    max_heap = [-x for x in nums]
    heapq.heapify(max_heap)             # O(n) heapify, not O(n log n)
    return -heapq.heappop(max_heap)     # negate on the way out


# --- Heap with tuples (for K closest, etc.) ---
def k_closest_points(points: list[list[int]], k: int) -> list[list[int]]:
    # max-heap of size K: negate distance so we can evict the FARTHEST
    heap: list[tuple[float, list[int]]] = []
    for x, y in points:
        dist = -(x * x + y * y)         # negate for max-heap behavior
        heapq.heappush(heap, (dist, [x, y]))
        if len(heap) > k:
            heapq.heappop(heap)         # pops the largest (negated = farthest)
    return [point for _, point in heap]


# --- Merge K sorted lists skeleton ---
def merge_k_sorted(lists: list[list[int]]) -> list[int]:
    result: list[int] = []
    heap: list[tuple[int, int, int]] = []  # (value, list_index, element_index)

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, li, ei = heapq.heappop(heap)
        result.append(val)
        if ei + 1 < len(lists[li]):
            heapq.heappush(heap, (lists[li][ei + 1], li, ei + 1))

    return result
```

## Common Mistakes

- **Using max-heap for "K largest" without negating**: Python only has a min-heap. For K largest, you want to evict the smallest, so a min-heap IS correct here — no negation needed. Negation is only needed when you want the largest to be popped first (e.g., K closest with max-heap eviction of farthest).
- **Calling `heapq.heappush` + `heappop` separately instead of `heappushpop`**: When you always push then immediately pop (common in the fixed-size pattern), `heapq.heappushpop(heap, item)` does both in one step and is faster.
- **Not using `heapq.heapify` for bulk construction**: If you already have all elements, `heapq.heapify(lst)` converts in-place in O(n). Pushing n elements one by one is O(n log n).
- **Tuple comparison ambiguity**: When storing `(priority, object)` tuples, Python will compare the second element if priorities are equal. If the object isn't comparable (e.g., a custom class), this crashes. Add a tie-breaking counter: `(priority, counter, object)`.
- **Forgetting that heap[0] is always the minimum**: You can peek at the min without popping via `heap[0]`. This is O(1) and often useful to check a threshold before deciding to push.

## Watch Me Solve (I do)

**Problem: Kth Largest Element in an Array (LC 215)**

Given an integer array `nums` and an integer `k`, return the k-th largest element in the array. Note: it is the k-th largest in sorted order, not the k-th distinct element.

---

I see "k-th largest" — this is the canonical heap problem. Let me think through the approaches.

**Brute force:** sort descending, return `nums[k-1]`. O(n log n) time. This works and I'd mention it first to show I understand the problem, but it's not optimal.

**Heap approach:** I want the k-th largest, which means there are exactly k-1 elements larger than it. If I maintain a min-heap of size k, the smallest element in that heap is exactly the k-th largest overall.

Why? Because I keep the k largest elements I've seen so far in the heap. The smallest of those k elements is the k-th largest.

Let me trace through `nums = [3, 2, 1, 5, 6, 4]`, `k = 2`:

- Push 3. Heap: `[3]`. Size ≤ k=2, no pop.
- Push 2. Heap: `[2, 3]`. Size = k=2, no pop.
- Push 1. Heap: `[1, 3, 2]` → size > k, pop min → pop 1. Heap: `[2, 3]`.
- Push 5. Heap: `[2, 3, 5]` → size > k, pop min → pop 2. Heap: `[3, 5]`.
- Push 6. Heap: `[3, 5, 6]` → size > k, pop min → pop 3. Heap: `[5, 6]`.
- Push 4. Heap: `[4, 6, 5]` → size > k, pop min → pop 4. Heap: `[5, 6]`.

Loop ends. `heap[0]` = 5. That's the 2nd largest. ✓ (Sorted desc: 6, 5, 4, 3, 2, 1 — 2nd is 5.)

```python
import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    heap: list[int] = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)   # evict the smallest; keep only the K largest

    return heap[0]   # the smallest of the K largest = K-th largest overall
```

**Complexity:** O(n log k) time — n pushes, each O(log k) since the heap never exceeds size k. O(k) space.

**Concise alternative using `heapq.nlargest`:**

```python
def find_kth_largest_short(nums: list[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]
```

This is valid in an interview but I'd always show the manual heap version first — it demonstrates that I understand the underlying mechanism, not just the standard library call.

**What an interviewer might follow up with:**

- "What if k is very large, close to n?" → The heap approach degrades toward O(n log n). QuickSelect (O(n) average) would be better. Worth mentioning even if you don't code it.
- "What if the array doesn't fit in memory?" → External sort or reservoir sampling — the heap approach generalizes nicely to streaming because you process one element at a time.
- "What about duplicates?" → The approach handles them correctly because we're comparing values, not positions. Trace through `[3,3,3]`, `k=2` to confirm: heap ends up as `[3,3]`, returns 3. ✓
