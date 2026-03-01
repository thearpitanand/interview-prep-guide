# Heap - Day 28

## 1. What is a Heap?

A **heap** is a **complete binary tree** stored as an array that satisfies the **heap property**:

- **Max-Heap**: Every parent node is **greater than or equal to** its children.
- **Min-Heap**: Every parent node is **less than or equal to** its children.

**Complete Binary Tree** means every level is fully filled except possibly the last, which is filled from left to right. This property allows us to store the tree efficiently in an array with no gaps.

### Min-Heap Example

```mermaid
graph TD
    A((1)) --> B((3))
    A --> C((5))
    B --> D((7))
    B --> E((9))
    C --> F((8))
    C --> G((10))

    style A fill:#4CAF50,stroke:#333,color:#fff
    style B fill:#2196F3,stroke:#333,color:#fff
    style C fill:#2196F3,stroke:#333,color:#fff
    style D fill:#FF9800,stroke:#333,color:#fff
    style E fill:#FF9800,stroke:#333,color:#fff
    style F fill:#FF9800,stroke:#333,color:#fff
    style G fill:#FF9800,stroke:#333,color:#fff
```

### Array Representation

```
Index:  [0]  [1]  [2]  [3]  [4]  [5]  [6]
Value:   1    3    5    7    9    8    10
         ^    ^    ^
         |    |    |
        root  |    |
          left  right
          child child
          of 0  of 0
```

### Max-Heap Example

```mermaid
graph TD
    A((50)) --> B((30))
    A --> C((40))
    B --> D((10))
    B --> E((20))
    C --> F((35))
    C --> G((15))

    style A fill:#e74c3c,stroke:#333,color:#fff
    style B fill:#e67e22,stroke:#333,color:#fff
    style C fill:#e67e22,stroke:#333,color:#fff
    style D fill:#f39c12,stroke:#333,color:#fff
    style E fill:#f39c12,stroke:#333,color:#fff
    style F fill:#f39c12,stroke:#333,color:#fff
    style G fill:#f39c12,stroke:#333,color:#fff
```

### Min-Heap vs Max-Heap at a Glance

| Property | Min-Heap | Max-Heap |
|----------|----------|----------|
| Root | Smallest element | Largest element |
| Parent vs Children | Parent <= Children | Parent >= Children |
| Python `heapq` | Default behavior | Negate values trick |
| Use case | Find minimum quickly | Find maximum quickly |

---

## 2. How It Works

### Parent-Child Index Relationships

For a node at index `i` (0-indexed):

```
Parent Index     = (i - 1) // 2
Left Child Index  = 2 * i + 1
Right Child Index = 2 * i + 2
```

```mermaid
graph TD
    A["Index 0<br/>parent = N/A"] --> B["Index 1<br/>parent = (1-1)//2 = 0"]
    A --> C["Index 2<br/>parent = (2-1)//2 = 0"]
    B --> D["Index 3<br/>parent = (3-1)//2 = 1"]
    B --> E["Index 4<br/>parent = (4-1)//2 = 1"]
    C --> F["Index 5<br/>parent = (5-1)//2 = 2"]
    C --> G["Index 6<br/>parent = (6-1)//2 = 2"]

    style A fill:#9b59b6,stroke:#333,color:#fff
    style B fill:#3498db,stroke:#333,color:#fff
    style C fill:#3498db,stroke:#333,color:#fff
    style D fill:#1abc9c,stroke:#333,color:#fff
    style E fill:#1abc9c,stroke:#333,color:#fff
    style F fill:#1abc9c,stroke:#333,color:#fff
    style G fill:#1abc9c,stroke:#333,color:#fff
```

### Sift Up (Used During Insert)

When we insert a new element, we place it at the end of the array and **bubble it up** by comparing with its parent. If it violates the heap property, we swap.

```mermaid
graph TD
    subgraph Step3["Step 3: Done - Heap property restored"]
        S3A((1)) --> S3B((3))
        S3A --> S3C((5))
        S3B --> S3D((7))
        S3B --> S3E((9))
        S3C --> S3F((8))
    end

    subgraph Step2["Step 2: Swap 2 with parent 5, then swap 2 with parent 1? No, 2 > 1"]
        S2A((1)) --> S2B((3))
        S2A --> S2C(("2 ^"))
        S2B --> S2D((7))
        S2B --> S2E((9))
        S2C --> S2F((8))
        S2C --> S2G((5))
    end

    subgraph Step1["Step 1: Insert 2 at end, compare with parent 5"]
        S1A((1)) --> S1B((3))
        S1A --> S1C((5))
        S1B --> S1D((7))
        S1B --> S1E((9))
        S1C --> S1F((8))
        S1C --> S1G(("2 NEW"))
    end

    style S1G fill:#e74c3c,stroke:#333,color:#fff
    style S2C fill:#e74c3c,stroke:#333,color:#fff
```

### Sift Down (Used During Extract)

When we extract the root, we replace it with the last element and **push it down** by swapping with the smaller (min-heap) or larger (max-heap) child.

```mermaid
graph TD
    subgraph Step3["Step 3: 8 > 7? No swap needed. Done!"]
        T3A((3)) --> T3B((7))
        T3A --> T3C((5))
        T3B --> T3D((8))
        T3B --> T3E((9))
        T3C --> T3F((10))
    end

    subgraph Step2["Step 2: Swap 8 with smaller child 7"]
        T2A((3)) --> T2B(("8 v"))
        T2A --> T2C((5))
        T2B --> T2D((7))
        T2B --> T2E((9))
        T2C --> T2F((10))
    end

    subgraph Step1["Step 1: Remove root 1, move last element 8 to root"]
        T1A(("8 v")) --> T1B((3))
        T1A --> T1C((5))
        T1B --> T1D((7))
        T1B --> T1E((9))
        T1C --> T1F((10))
    end

    style T1A fill:#e74c3c,stroke:#333,color:#fff
    style T2B fill:#e74c3c,stroke:#333,color:#fff
```

---

## 3. Python `heapq` Module

Python's `heapq` module implements a **min-heap** by default. There is no built-in max-heap, but we can simulate one by negating values.

### Core Operations

```python
import heapq

# --- Min-Heap (default) ---
heap = []
heapq.heappush(heap, 5)       # Push element
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)
print(heap)                     # [3, 5, 7]

val = heapq.heappop(heap)      # Pop smallest -> 3
val = heap[0]                   # Peek smallest (don't pop) -> 5

# --- Build heap from existing list (in-place, O(n)) ---
nums = [5, 3, 7, 1, 9]
heapq.heapify(nums)             # nums is now a valid min-heap
print(nums)                     # [1, 3, 7, 5, 9]

# --- Push and Pop in one operation ---
val = heapq.heapreplace(heap, 4)  # Pop smallest, then push 4
val = heapq.heappushpop(heap, 2)  # Push 2, then pop smallest (faster)

# --- Top-K helpers ---
heapq.nlargest(3, nums)         # 3 largest elements -> [9, 7, 5]
heapq.nsmallest(3, nums)        # 3 smallest elements -> [1, 3, 5]
```

### Max-Heap Trick (Negate Values)

```python
import heapq

# Simulate max-heap by pushing negative values
max_heap = []
for val in [5, 3, 7, 1, 9]:
    heapq.heappush(max_heap, -val)

largest = -heapq.heappop(max_heap)   # 9
second  = -heapq.heappop(max_heap)   # 7
```

### Heap with Tuples (Priority Queue Style)

```python
import heapq

# Tuples are compared element by element
# (priority, data)
tasks = []
heapq.heappush(tasks, (2, "low priority"))
heapq.heappush(tasks, (1, "high priority"))
heapq.heappush(tasks, (3, "lowest priority"))

priority, task = heapq.heappop(tasks)  # (1, "high priority")
```

---

## 4. Operations & Time Complexities

| Operation | Time Complexity | Description |
|-----------|:-:|-------------|
| `heappush` (Insert) | **O(log n)** | Add element, sift up |
| `heappop` (Extract Min/Max) | **O(log n)** | Remove root, sift down |
| `heap[0]` (Peek) | **O(1)** | Access root without removal |
| `heapify` (Build Heap) | **O(n)** | Convert list to heap in-place |
| `heapreplace` | **O(log n)** | Pop then push (combined) |
| `heappushpop` | **O(log n)** | Push then pop (optimized) |
| `nlargest(k)` | **O(n log k)** | Find k largest elements |
| `nsmallest(k)` | **O(n log k)** | Find k smallest elements |

**Space Complexity**: O(n) for storing n elements.

### Why is `heapify` O(n) and not O(n log n)?

Building a heap bottom-up means most nodes are near the leaves and need very few swaps. The math works out to O(n) total swaps across all nodes, not O(log n) per node.

```mermaid
graph TD
    subgraph Insight["Node Count vs Sift Distance"]
        A["n/2 leaf nodes -> 0 sifts"] --- B["n/4 nodes -> 1 sift"]
        B --- C["n/8 nodes -> 2 sifts"]
        C --- D["1 root node -> log n sifts"]
    end
```

**Total work** = n/4 * 1 + n/8 * 2 + n/16 * 3 + ... = **O(n)**

---

## 5. Key Patterns

### Pattern 1: Top-K Elements (Medium)

**When to use**: "Find k largest/smallest/most frequent elements."

**Strategy**: Maintain a **min-heap of size K**. For each element, push it. If heap size exceeds K, pop the smallest. At the end, the heap contains the K largest.

```mermaid
graph LR
    subgraph Stream["Input Stream: 3, 1, 5, 2, 8, 4"]
        direction LR
    end

    subgraph Process["Min-Heap (K=3)"]
        direction TB
        P1["Push 3 -> [3]"]
        P2["Push 1 -> [1,3]"]
        P3["Push 5 -> [1,3,5]"]
        P4["Push 2, Pop 1 -> [2,3,5]"]
        P5["Push 8, Pop 2 -> [3,5,8]"]
        P6["Push 4, Pop 3 -> [4,5,8]"]
        P1 --> P2 --> P3 --> P4 --> P5 --> P6
    end

    subgraph Result["Top 3: {4, 5, 8}"]
    end

    Stream --> Process --> Result
```

```python
def top_k_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # Remove smallest
    return heap  # Contains k largest
```

**Problems**: LC 215, LC 347, LC 703

---

### Pattern 2: Merge K Sorted (Hard)

**When to use**: "Merge K sorted lists/arrays/streams."

**Strategy**: Use a min-heap to always track the **smallest unprocessed element** across all K lists. Pop the smallest, then push the next element from that same list.

```mermaid
graph TD
    subgraph Lists["K Sorted Lists"]
        L1["List 1: 1 -> 4 -> 5"]
        L2["List 2: 1 -> 3 -> 4"]
        L3["List 3: 2 -> 6"]
    end

    subgraph Heap["Min-Heap tracks heads"]
        H["(1,L1), (1,L2), (2,L3)"]
    end

    subgraph Output["Merged Output"]
        O["1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6"]
    end

    Lists --> Heap
    Heap -->|"Pop min, push next from same list"| Output
```

**Time**: O(N log K) where N = total elements, K = number of lists

**Problems**: LC 23, LC 632

---

### Pattern 3: Two Heaps / Median (Hard)

**When to use**: "Find median in a stream", "Balance two halves."

**Strategy**: Maintain two heaps:
- **Max-heap** (negate values) for the **lower half**
- **Min-heap** for the **upper half**

Keep them balanced so the median is always at one or both roots.

```mermaid
graph TD
    subgraph TwoHeaps["Two Heaps for Median"]
        subgraph MaxHeap["Max-Heap (Lower Half)"]
            MH["Stores smaller values<br/>Root = max of lower half<br/>Python: negate values"]
        end
        subgraph MinHeap["Min-Heap (Upper Half)"]
            MIH["Stores larger values<br/>Root = min of upper half<br/>Python: default heapq"]
        end
    end

    MaxHeap -->|"max of lower <= min of upper"| MinHeap

    subgraph Balance["Balance Rule"]
        B["len(max_heap) == len(min_heap)<br/>OR<br/>len(max_heap) == len(min_heap) + 1"]
    end

    TwoHeaps --> Balance

    subgraph Median["Finding Median"]
        M1["If equal sizes: (max_root + min_root) / 2"]
        M2["If max_heap larger: max_root is median"]
    end

    Balance --> Median
```

```mermaid
graph LR
    subgraph Example["Stream: 5, 2, 8, 1, 4"]
        direction TB
        S1["Add 5: max=[-5] min=[] -> median=5"]
        S2["Add 2: max=[-2] min=[5] -> median=3.5"]
        S3["Add 8: max=[-2] min=[5,8] -> rebalance -> max=[-5,-2] min=[8] -> median=5"]
        S4["Add 1: max=[-5,-2,-1] min=[8] -> rebalance -> max=[-2,-1] min=[5,8] -> median=3.5"]
        S5["Add 4: max=[-4,-2,-1] min=[5,8] -> median=4"]
        S1 --> S2 --> S3 --> S4 --> S5
    end
```

**Problems**: LC 295, LC 480

---

### Pattern 4: Priority Queue (Medium)

**When to use**: "Schedule tasks by priority", "Process elements in a specific order."

**Strategy**: Use heap as a priority queue where elements are processed by their priority value. Tuples `(priority, data)` make this natural in Python.

```python
import heapq

# Task scheduler
tasks = [(3, "email"), (1, "urgent_bug"), (2, "code_review")]
heapq.heapify(tasks)

while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"Processing: {task} (priority {priority})")
# Output: urgent_bug, code_review, email
```

**Problems**: LC 767, LC 621

---

### Pattern 5: Heap Sort (Medium)

**When to use**: "Sort with O(n log n) guaranteed", "Sort a nearly sorted array."

**Strategy**: Build a heap from the array, then repeatedly extract the min/max.

```mermaid
graph LR
    subgraph Phase1["Phase 1: Build Heap O(n)"]
        A["[5,3,7,1,9]"] -->|heapify| B["[1,3,7,5,9]"]
    end

    subgraph Phase2["Phase 2: Extract O(n log n)"]
        B -->|"pop 1"| C["[3,5,7,9]"]
        C -->|"pop 3"| D["[5,7,9]"]
        D -->|"pop 5"| E["[7,9]"]
        E -->|"pop 7"| F["[9]"]
        F -->|"pop 9"| G["[]"]
    end

    subgraph Result["Sorted: [1,3,5,7,9]"]
    end

    Phase2 --> Result
```

**For nearly sorted arrays (k-sorted)**: Use a heap of size K+1 for O(n log k) sorting.

**Problems**: LC 658 variant

---

## 6. Which Pattern to Use?

```mermaid
flowchart TD
    Start["Heap Problem"] --> Q1{"Find K largest/<br/>smallest/frequent?"}
    Q1 -->|Yes| P1["Top-K Elements<br/>Min-heap size K"]

    Q1 -->|No| Q2{"Merge K sorted<br/>lists/arrays?"}
    Q2 -->|Yes| P2["Merge K Sorted<br/>Min-heap of K heads"]

    Q2 -->|No| Q3{"Find median<br/>in stream?"}
    Q3 -->|Yes| P3["Two Heaps<br/>Max-heap + Min-heap"]

    Q3 -->|No| Q4{"Process by<br/>priority order?"}
    Q4 -->|Yes| P4["Priority Queue<br/>Heap with tuples"]

    Q4 -->|No| Q5{"Sort nearly<br/>sorted array?"}
    Q5 -->|Yes| P5["Heap Sort<br/>Window of size K"]

    Q5 -->|No| Q6{"Need repeated<br/>min/max access?"}
    Q6 -->|Yes| P6["Basic Heap<br/>Push/Pop pattern"]

    Q6 -->|No| P7["Consider other<br/>data structures"]

    style P1 fill:#4CAF50,stroke:#333,color:#fff
    style P2 fill:#2196F3,stroke:#333,color:#fff
    style P3 fill:#9C27B0,stroke:#333,color:#fff
    style P4 fill:#FF9800,stroke:#333,color:#fff
    style P5 fill:#00BCD4,stroke:#333,color:#fff
    style P6 fill:#607D8B,stroke:#333,color:#fff
    style P7 fill:#f44336,stroke:#333,color:#fff
```

### Quick Reference

| Signal in Problem | Pattern | Heap Type |
|---|---|---|
| "K largest" / "K most frequent" | Top-K | Min-heap of size K |
| "K smallest" | Top-K | Max-heap of size K |
| "Merge K sorted" | Merge K Sorted | Min-heap of K elements |
| "Median" / "balance two halves" | Two Heaps | Max-heap + Min-heap |
| "Priority" / "schedule" / "order" | Priority Queue | Min-heap with tuples |
| "Nearly sorted" / "K-sorted" | Heap Sort | Min-heap of size K |
| "Continuously find min/max" | Basic Heap | Min or Max heap |

---

## 7. Day Schedule

### Day 28: Heaps

| # | Problem | Difficulty | Pattern | Time |
|---|---------|:---:|---------|------|
| 1 | Last Stone Weight (LC 1046) | Easy | Max Heap | 10 min |
| 2 | Kth Largest in Stream (LC 703) | Easy | Min Heap | 12 min |
| 3 | Relative Ranks (LC 506) | Easy | Heap/Sort | 10 min |
| 4 | Kth Largest Element (LC 215) | Medium | Min Heap | 12 min |
| 5 | Top K Frequent Elements (LC 347) | Medium | Heap | 15 min |
| 6 | Sort Nearly Sorted Array (LC 658 variant) | Medium | Heap Sort | 12 min |
| 7 | Reorganize String (LC 767) | Medium | Max Heap | 15 min |
| 8 | Merge K Sorted Lists (LC 23) | Hard | Merge K Sorted | 20 min |
| 9 | Find Median from Data Stream (LC 295) | Hard | Two Heaps | 20 min |
| 10 | Smallest Range (LC 632) | Hard | Heap + Sliding Window | 25 min |

**Total estimated time: ~2.5 hours**

**Suggested order**: Start with Easy problems to warm up, then Medium for pattern practice, then Hard for deep understanding. If short on time, prioritize: LC 215, LC 347, LC 295, LC 23.
