# Day 5: The DSA Toolkit

> Master the Python standard library modules you'll use in every DSA problem.

---

## 1. The `collections` Module

```mermaid
flowchart TB
    subgraph "collections module"
        A["Counter"]
        B["defaultdict"]
        C["deque"]
        D["OrderedDict"]
    end

    A --> A1["Count occurrences"]
    A --> A2["most_common(k)"]
    A --> A3["Arithmetic: +, -, &, |"]

    B --> B1["Auto-initialize keys"]
    B --> B2["defaultdict(int)"]
    B --> B3["defaultdict(list)"]
    B --> B4["defaultdict(set)"]

    C --> C1["O(1) append/pop both ends"]
    C --> C2["appendleft / popleft"]
    C --> C3["BFS, sliding window"]

    D --> D1["Remembers insertion order"]
    D --> D2["Rarely needed in Python 3.7+"]
```

### Counter

```python
from collections import Counter

# Count occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Most common
count.most_common(2)
# [('apple', 3), ('banana', 2)]

# Counting characters in a string
Counter("mississippi")
# Counter({'s': 4, 'i': 4, 'p': 2, 'm': 1})

# Arithmetic with Counters
a = Counter("aabbc")
b = Counter("abccc")
print(a + b)  # Counter({'c': 4, 'a': 3, 'b': 3})
print(a - b)  # Counter({'a': 1, 'b': 1})  (only positive counts)
print(a & b)  # Counter({'a': 1, 'b': 1, 'c': 1})  (min of each)
print(a | b)  # Counter({'c': 3, 'a': 2, 'b': 2})  (max of each)

# elements() returns an iterator over elements
list(Counter("aabbc").elements())
# ['a', 'a', 'b', 'b', 'c']
```

### defaultdict

```python
from collections import defaultdict

# defaultdict(int) -- default value is 0
counter = defaultdict(int)
for ch in "hello":
    counter[ch] += 1   # no KeyError if key doesn't exist!
# defaultdict(int, {'h': 1, 'e': 1, 'l': 2, 'o': 1})

# defaultdict(list) -- default value is []
groups = defaultdict(list)
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
for word in words:
    key = "".join(sorted(word))
    groups[key].append(word)   # no need to check if key exists
# {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}

# defaultdict(set) -- default value is set()
graph = defaultdict(set)
edges = [(1, 2), (1, 3), (2, 3)]
for u, v in edges:
    graph[u].add(v)
    graph[v].add(u)
# {1: {2, 3}, 2: {1, 3}, 3: {1, 2}}
```

### deque (Double-Ended Queue)

```mermaid
flowchart LR
    subgraph "deque vs list"
        direction TB
        subgraph "deque - O(1) both ends"
            DL["appendleft()"] --> D["deque: [1, 2, 3, 4]"]
            D --> DR["append()"]
            DPL["popleft()"] --> D
            D --> DPR["pop()"]
        end
        subgraph "list - O(1) right only"
            L["list: [1, 2, 3, 4]"]
            LL["insert(0, x) O(n)"] --> L
            L --> LR["append() O(1)"]
            LPL["pop(0) O(n)"] --> L
            L --> LPR["pop() O(1)"]
        end
    end
```

```python
from collections import deque

# Create a deque
dq = deque([1, 2, 3])

# O(1) operations on both ends
dq.append(4)       # [1, 2, 3, 4]
dq.appendleft(0)   # [0, 1, 2, 3, 4]
dq.pop()            # returns 4, deque is [0, 1, 2, 3]
dq.popleft()        # returns 0, deque is [1, 2, 3]

# BFS pattern (most common DSA use)
queue = deque([start_node])
while queue:
    node = queue.popleft()        # O(1) dequeue
    for neighbor in graph[node]:
        queue.append(neighbor)    # O(1) enqueue

# Comparison with list:
# Operation        | list    | deque
# append (right)   | O(1)    | O(1)
# pop (right)      | O(1)    | O(1)
# insert (left)    | O(n)    | O(1)  <-- deque wins
# pop (left)       | O(n)    | O(1)  <-- deque wins
# random access    | O(1)    | O(n)  <-- list wins
```

### OrderedDict

In Python 3.7+, regular `dict` already maintains insertion order. `OrderedDict` is rarely needed but has one useful feature: `move_to_end()`.

```python
from collections import OrderedDict

# Useful for LRU Cache implementation
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)  # mark as recently used
            return self.cache[key]
        return -1
```

---

## 2. The `heapq` Module

Python's `heapq` implements a **min-heap** using a regular list. The smallest element is always at index 0.

```mermaid
flowchart TB
    subgraph "Min-Heap: [1, 3, 2, 7, 6, 4, 5]"
        N1((1)) --> N3((3))
        N1 --> N2((2))
        N3 --> N7((7))
        N3 --> N6((6))
        N2 --> N4((4))
        N2 --> N5((5))
    end

    subgraph "Heap Property"
        R["Parent <= Both Children"]
        R --> R1["heap[0] is ALWAYS the minimum"]
        R --> R2["heappush: O(log n)"]
        R --> R3["heappop: O(log n)"]
        R --> R4["heapify: O(n)"]
    end
```

### Core Operations

```python
import heapq

# heapify: convert list to heap in O(n)
nums = [5, 3, 8, 1, 2]
heapq.heapify(nums)
# nums is now a valid heap: [1, 2, 8, 5, 3]

# heappush: add element in O(log n)
heapq.heappush(nums, 0)
# [0, 2, 1, 5, 3, 8]

# heappop: remove and return smallest in O(log n)
smallest = heapq.heappop(nums)  # returns 0

# nlargest and nsmallest
heapq.nsmallest(3, [5, 1, 8, 3, 2])  # [1, 2, 3]
heapq.nlargest(3, [5, 1, 8, 3, 2])   # [8, 5, 3]
```

### Max-Heap Trick

Python only has min-heap. To simulate a max-heap, **negate the values**:

```python
import heapq

# Max-heap using negation
max_heap = []
for val in [3, 1, 4, 1, 5, 9]:
    heapq.heappush(max_heap, -val)

largest = -heapq.heappop(max_heap)  # 9
```

### Heap with Custom Priority (Tuples)

```python
import heapq

# Priority queue: (priority, data)
tasks = []
heapq.heappush(tasks, (2, "low priority"))
heapq.heappush(tasks, (1, "high priority"))
heapq.heappush(tasks, (3, "lowest priority"))

priority, task = heapq.heappop(tasks)
# priority=1, task="high priority"
```

---

## 3. The `bisect` Module

`bisect` performs **binary search** on sorted lists in O(log n).

```mermaid
flowchart LR
    subgraph "bisect_left vs bisect_right on [1, 3, 3, 3, 5]"
        direction TB
        A["target = 3"]
        B["bisect_left -> index 1<br>(insert BEFORE existing 3s)"]
        C["bisect_right -> index 4<br>(insert AFTER existing 3s)"]
        A --> B
        A --> C
    end

    subgraph "Visual"
        D["[1, | 3, 3, 3, | 5]"]
        E["     ^bisect_left    ^bisect_right"]
    end
```

```
Array:   [ 1,  3,  3,  3,  5 ]
Index:     0   1   2   3   4   5
                ^               ^
          bisect_left(3)=1   bisect_right(3)=4
```

### Core Functions

```python
import bisect

sorted_list = [1, 3, 3, 3, 5, 7, 9]

# bisect_left: leftmost position to insert (before duplicates)
bisect.bisect_left(sorted_list, 3)    # 1

# bisect_right: rightmost position to insert (after duplicates)
bisect.bisect_right(sorted_list, 3)   # 4

# insort: insert while keeping sorted order
bisect.insort(sorted_list, 4)
# [1, 3, 3, 3, 4, 5, 7, 9]
```

### Common DSA Patterns

```python
import bisect

# Count occurrences in sorted list: O(log n)
def count_in_sorted(arr, target):
    left = bisect.bisect_left(arr, target)
    right = bisect.bisect_right(arr, target)
    return right - left

# Count elements less than target: O(log n)
def count_less_than(arr, target):
    return bisect.bisect_left(arr, target)

# Count elements less than or equal to target: O(log n)
def count_leq(arr, target):
    return bisect.bisect_right(arr, target)

# Find element in sorted list (like binary search): O(log n)
def binary_search(arr, target):
    i = bisect.bisect_left(arr, target)
    if i < len(arr) and arr[i] == target:
        return i
    return -1
```

---

## 4. `functools.lru_cache` (Memoization)

`lru_cache` automatically caches function results, turning recursive solutions from exponential to polynomial time.

```mermaid
flowchart TD
    subgraph "Without Memoization: fib(5)"
        A5["fib(5)"] --> A4["fib(4)"]
        A5 --> A3a["fib(3)"]
        A4 --> A3b["fib(3)"]
        A4 --> A2a["fib(2)"]
        A3a --> A2b["fib(2)"]
        A3a --> A1a["fib(1)"]
        A3b --> A2c["fib(2)"]
        A3b --> A1b["fib(1)"]
    end

    subgraph "With @lru_cache: fib(5)"
        B5["fib(5)"] --> B4["fib(4)"]
        B5 -.->|"cached"| B3["fib(3)"]
        B4 --> B3
        B4 -.->|"cached"| B2["fib(2)"]
        B3 --> B2
        B3 -.->|"cached"| B1["fib(1)"]
    end
```

```python
from functools import lru_cache

# Without memoization: O(2^n) -- extremely slow
def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)

# With memoization: O(n) -- fast!
@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

fib(100)  # instant, returns 354224848179261915075
```

### Common DSA Patterns with `lru_cache`

```python
from functools import lru_cache

# Climbing stairs (how many ways to reach step n?)
@lru_cache(maxsize=None)
def climb_stairs(n):
    if n <= 2:
        return n
    return climb_stairs(n - 1) + climb_stairs(n - 2)

# Grid paths (unique paths from top-left to bottom-right)
@lru_cache(maxsize=None)
def unique_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return unique_paths(m - 1, n) + unique_paths(m, n - 1)
```

**Important:** `lru_cache` requires that all arguments are **hashable** (no lists or dicts -- use tuples instead).

---

## 5. The `itertools` Module

`itertools` provides efficient looping utilities that are extremely handy in DSA.

### permutations and combinations

```python
from itertools import permutations, combinations, product

# permutations: all orderings (n! results)
list(permutations([1, 2, 3]))
# [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]

# permutations of specific length
list(permutations([1, 2, 3], 2))
# [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]

# combinations: selections without order (n choose k)
list(combinations([1, 2, 3], 2))
# [(1,2), (1,3), (2,3)]

# product: cartesian product (nested loops)
list(product([0, 1], repeat=3))
# [(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]
```

### chain and groupby

```python
from itertools import chain, groupby

# chain: combine multiple iterables
list(chain([1, 2], [3, 4], [5]))
# [1, 2, 3, 4, 5]

# Flatten a list of lists
lists = [[1, 2], [3], [4, 5, 6]]
list(chain.from_iterable(lists))
# [1, 2, 3, 4, 5, 6]

# groupby: group consecutive elements (MUST be sorted first!)
data = sorted(["apple", "avocado", "banana", "blueberry", "cherry"])
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, list(group))
# a ['apple', 'avocado']
# b ['banana', 'blueberry']
# c ['cherry']
```

---

## 6. `sys.setrecursionlimit`

Python's default recursion limit is **1000**. Many DSA problems have inputs up to 10^5, which means deep recursion will crash.

```python
import sys
sys.setrecursionlimit(10**6)  # increase to 1 million

# Now deep recursion won't hit RecursionError
def dfs(node, graph, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)
```

**When to use it:**
- DFS on large graphs (up to 10^5 nodes)
- Deep recursive DP solutions
- Tree traversals on skewed trees

**Caution:** Setting it too high (10^7+) can cause a segmentation fault. For very deep recursion, convert to an iterative approach using an explicit stack.

---

## Quick Reference Cheat Sheet

```python
# --- Counter ---
from collections import Counter
Counter("aabbc").most_common(2)

# --- defaultdict ---
from collections import defaultdict
d = defaultdict(list)
d["key"].append(1)

# --- deque ---
from collections import deque
q = deque()
q.append(1); q.popleft()

# --- heapq ---
import heapq
heapq.heappush(heap, val)
heapq.heappop(heap)

# --- bisect ---
import bisect
bisect.bisect_left(sorted_arr, target)

# --- lru_cache ---
from functools import lru_cache
@lru_cache(maxsize=None)
def dp(state): ...

# --- itertools ---
from itertools import permutations, combinations
list(permutations([1,2,3]))
list(combinations([1,2,3], 2))

# --- Recursion limit ---
import sys
sys.setrecursionlimit(10**6)
```
