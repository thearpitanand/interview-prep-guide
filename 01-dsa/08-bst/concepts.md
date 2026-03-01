# Binary Search Tree (BST) - Days 26-27

## 1. What is a BST?

A **Binary Search Tree** is a binary tree where every node satisfies the **BST property**:

- All values in the **left subtree** are **less than** the node's value
- All values in the **right subtree** are **greater than** the node's value
- Both left and right subtrees are also BSTs

This property holds for **every** node in the tree, not just the root.

```mermaid
graph TD
    subgraph "Valid BST"
        A((8)) --> B((3))
        A --> C((10))
        B --> D((1))
        B --> E((6))
        E --> F((4))
        E --> G((7))
        C --> H((None))
        C --> I((14))
        I --> J((13))
        I --> K((None))
    end

    style A fill:#4CAF50,color:white
    style B fill:#2196F3,color:white
    style C fill:#2196F3,color:white
    style D fill:#FF9800,color:white
    style E fill:#FF9800,color:white
    style F fill:#9C27B0,color:white
    style G fill:#9C27B0,color:white
    style I fill:#FF9800,color:white
    style J fill:#9C27B0,color:white
    style H fill:#eee,color:#999
    style K fill:#eee,color:#999
```

```mermaid
graph TD
    subgraph "INVALID BST"
        A2((5)) --> B2((1))
        A2 --> C2((4))
        C2 --> D2((3))
        C2 --> E2((6))
    end

    style A2 fill:#f44336,color:white
    style C2 fill:#f44336,color:white
    style B2 fill:#FF9800,color:white
    style D2 fill:#FF9800,color:white
    style E2 fill:#FF9800,color:white
```

> The second tree is invalid because `4` is in the right subtree of `5`, but `4 < 5` violates the BST property.

---

## 2. Operations

### Search

To find a value, compare it with the current node and go left or right accordingly.

```mermaid
graph TD
    subgraph "Search for 4"
        A((8)) -->|"4 < 8, go left"| B((3))
        A --> C((10))
        B --> D((1))
        B -->|"4 > 3, go right"| E((6))
        E -->|"4 < 6, go left"| F((4))
        E --> G((7))
    end

    style A fill:#FFC107,color:black
    style B fill:#FFC107,color:black
    style E fill:#FFC107,color:black
    style F fill:#4CAF50,color:white
    style C fill:#eee,color:#666
    style D fill:#eee,color:#666
    style G fill:#eee,color:#666
```

**Steps:**
1. Start at root (8). Target 4 < 8, go **left**.
2. At node 3. Target 4 > 3, go **right**.
3. At node 6. Target 4 < 6, go **left**.
4. At node 4. **Found!**

### Insert

Insert always happens at a leaf position. Traverse like search, then attach.

```mermaid
graph TD
    subgraph "Insert 5 into BST"
        A((8)) -->|"5 < 8"| B((3))
        A --> C((10))
        B --> D((1))
        B -->|"5 > 3"| E((6))
        E -->|"5 < 6"| F((4))
        E --> G((7))
        F --> H((None))
        F -->|"5 > 4, insert right"| I((5))
    end

    style I fill:#4CAF50,color:white,stroke:#4CAF50,stroke-width:3px
    style A fill:#FFC107,color:black
    style B fill:#FFC107,color:black
    style E fill:#FFC107,color:black
    style F fill:#FFC107,color:black
    style C fill:#eee,color:#666
    style D fill:#eee,color:#666
    style G fill:#eee,color:#666
    style H fill:#eee,color:#999
```

### Delete (3 Cases)

Deleting a node from a BST has three cases:

```mermaid
graph TD
    subgraph "Case 1: Leaf Node - Delete 4"
        A1((8)) --> B1((3))
        A1 --> C1((10))
        B1 --> D1((1))
        B1 --> E1((4))
        E1 -.->|"Simply remove"| X1((None))
    end

    style E1 fill:#f44336,color:white
    style X1 fill:#eee,color:#999,stroke-dasharray: 5 5
    style A1 fill:#2196F3,color:white
    style B1 fill:#2196F3,color:white
    style C1 fill:#2196F3,color:white
    style D1 fill:#2196F3,color:white
```

```mermaid
graph TD
    subgraph "Case 2: One Child - Delete 10"
        A2((8)) --> B2((3))
        A2 --> C2((10))
        C2 --> D2((None))
        C2 --> E2((14))

        A2R((8)) --> B2R((3))
        A2R -->|"Replace 10 with 14"| E2R((14))
    end

    style C2 fill:#f44336,color:white
    style D2 fill:#eee,color:#999
    style E2 fill:#4CAF50,color:white
    style A2 fill:#2196F3,color:white
    style B2 fill:#2196F3,color:white
    style A2R fill:#2196F3,color:white
    style B2R fill:#2196F3,color:white
    style E2R fill:#4CAF50,color:white
```

```mermaid
graph TD
    subgraph "Case 3: Two Children - Delete 3"
        A3((8)) --> B3((3))
        A3 --> C3((10))
        B3 --> D3((1))
        B3 --> E3((6))
        E3 --> F3((4))
        E3 --> G3((7))
    end

    style B3 fill:#f44336,color:white
    style F3 fill:#4CAF50,color:white
    style A3 fill:#2196F3,color:white
    style C3 fill:#2196F3,color:white
    style D3 fill:#2196F3,color:white
    style E3 fill:#2196F3,color:white
    style G3 fill:#2196F3,color:white
```

**Case 3 Steps:**
1. Find the **inorder successor** (smallest node in right subtree) = `4`
2. **Replace** the deleted node's value with the successor's value
3. **Delete** the successor from its original position (which is Case 1 or 2)

```mermaid
graph TD
    subgraph "After deleting 3 - replaced by inorder successor 4"
        A3R((8)) --> B3R((4))
        A3R --> C3R((10))
        B3R --> D3R((1))
        B3R --> E3R((6))
        E3R --> F3R((None))
        E3R --> G3R((7))
    end

    style B3R fill:#4CAF50,color:white
    style A3R fill:#2196F3,color:white
    style C3R fill:#2196F3,color:white
    style D3R fill:#2196F3,color:white
    style E3R fill:#2196F3,color:white
    style G3R fill:#2196F3,color:white
    style F3R fill:#eee,color:#999
```

---

## 3. Time Complexities

| Operation | Average Case | Worst Case (Skewed) |
|-----------|:------------:|:-------------------:|
| Search    | O(log n)     | O(n)                |
| Insert    | O(log n)     | O(n)                |
| Delete    | O(log n)     | O(n)                |
| Traversal | O(n)         | O(n)                |
| Space     | O(n)         | O(n)                |

**Why worst case O(n)?** When the tree degenerates into a linked list (e.g., inserting sorted data: 1, 2, 3, 4, 5).

```mermaid
graph TD
    subgraph "Balanced - O(log n) height"
        BA((4)) --> BB((2))
        BA --> BC((6))
        BB --> BD((1))
        BB --> BE((3))
        BC --> BF((5))
        BC --> BG((7))
    end

    subgraph "Skewed - O(n) height"
        SA((1)) --> SX1((None))
        SA --> SB((2))
        SB --> SX2((None))
        SB --> SC((3))
        SC --> SX3((None))
        SC --> SD((4))
    end

    style BA fill:#4CAF50,color:white
    style BB fill:#4CAF50,color:white
    style BC fill:#4CAF50,color:white
    style BD fill:#4CAF50,color:white
    style BE fill:#4CAF50,color:white
    style BF fill:#4CAF50,color:white
    style BG fill:#4CAF50,color:white
    style SA fill:#f44336,color:white
    style SB fill:#f44336,color:white
    style SC fill:#f44336,color:white
    style SD fill:#f44336,color:white
    style SX1 fill:#eee,color:#999
    style SX2 fill:#eee,color:#999
    style SX3 fill:#eee,color:#999
```

---

## 4. Inorder Traversal = Sorted Output

The **most important** BST property for interviews: **inorder traversal of a BST produces elements in sorted (ascending) order**.

```mermaid
graph TD
    subgraph "Inorder: Left -> Root -> Right"
        A((8)) --> B((3))
        A --> C((10))
        B --> D((1))
        B --> E((6))
        C --> F((None))
        C --> G((14))
        E --> H((4))
        E --> I((7))
    end

    style A fill:#2196F3,color:white
    style B fill:#2196F3,color:white
    style C fill:#2196F3,color:white
    style D fill:#4CAF50,color:white
    style E fill:#2196F3,color:white
    style G fill:#2196F3,color:white
    style H fill:#4CAF50,color:white
    style I fill:#4CAF50,color:white
    style F fill:#eee,color:#999
```

**Traversal order:** `1 -> 3 -> 4 -> 6 -> 7 -> 8 -> 10 -> 14` (sorted!)

```mermaid
graph LR
    N1((1)) --> N3((3)) --> N4((4)) --> N6((6)) --> N7((7)) --> N8((8)) --> N10((10)) --> N14((14))

    style N1 fill:#4CAF50,color:white
    style N3 fill:#4CAF50,color:white
    style N4 fill:#4CAF50,color:white
    style N6 fill:#4CAF50,color:white
    style N7 fill:#4CAF50,color:white
    style N8 fill:#4CAF50,color:white
    style N10 fill:#4CAF50,color:white
    style N14 fill:#4CAF50,color:white
```

This property is used in many problems:
- Finding **kth smallest** element
- **Validating** a BST
- Converting BST to **sorted list**
- **Recovering** a BST with swapped nodes

---

## 5. Key Patterns

### Pattern 1: BST Search/Insert (Easy)

Use the BST property to decide left/right at each step.

```python
# Recursive Search
def search(root, val):
    if not root or root.val == val:
        return root
    if val < root.val:
        return search(root.left, val)
    return search(root.right, val)

# Iterative Search (preferred for O(1) space)
def search_iterative(root, val):
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    return root
```

### Pattern 2: BST Validation (Medium)

Pass a valid **range** `(low, high)` down the recursion. Every node must fall within its allowed range.

```mermaid
graph TD
    subgraph "Range-based Validation"
        A((8))
        A -->|"range: -inf to 8"| B((3))
        A -->|"range: 8 to +inf"| C((10))
        B -->|"range: -inf to 3"| D((1))
        B -->|"range: 3 to 8"| E((6))
    end

    style A fill:#4CAF50,color:white
    style B fill:#2196F3,color:white
    style C fill:#2196F3,color:white
    style D fill:#FF9800,color:white
    style E fill:#FF9800,color:white
```

```python
def isValidBST(root, low=float('-inf'), high=float('inf')):
    if not root:
        return True
    if root.val <= low or root.val >= high:
        return False
    return (isValidBST(root.left, low, root.val) and
            isValidBST(root.right, root.val, high))
```

### Pattern 3: Inorder Successor/Predecessor (Medium)

The **inorder successor** is the node with the smallest value **greater than** the given node.

Two approaches:
1. **With parent pointer**: Go up until you find a left-child relationship.
2. **Without parent pointer**: Track the last node where you went **left** (that's a potential successor).

```python
def inorder_successor(root, target):
    successor = None
    while root:
        if target.val < root.val:
            successor = root  # potential successor
            root = root.left
        else:
            root = root.right
    return successor
```

### Pattern 4: BST to Sorted List (Medium)

Use **inorder traversal** (iterative or recursive) to collect values in sorted order, then reconstruct.

### Pattern 5: Balanced BST from Sorted Array (Medium)

Always pick the **middle element** as root. Recursively build left and right subtrees.

```mermaid
graph TD
    subgraph "Sorted Array: [-10, -3, 0, 5, 9]"
        A((0))
        A -->|"left half: [-10,-3]"| B(("-3"))
        A -->|"right half: [5,9]"| C((5))
        B -->|"left half: [-10]"| D(("-10"))
        B -->|"right half: empty"| E((None))
        C -->|"left half: empty"| F((None))
        C -->|"right half: [9]"| G((9))
    end

    style A fill:#4CAF50,color:white
    style B fill:#2196F3,color:white
    style C fill:#2196F3,color:white
    style D fill:#FF9800,color:white
    style G fill:#FF9800,color:white
    style E fill:#eee,color:#999
    style F fill:#eee,color:#999
```

### Pattern 6: Kth Smallest (Medium)

Perform **inorder traversal** and count nodes. When count reaches k, you have the answer.

```python
def kth_smallest(root, k):
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right
```

---

## 6. Which Pattern to Use?

```mermaid
flowchart TD
    Start["BST Problem"] --> Q1{"Need to find/insert\na specific value?"}
    Q1 -->|Yes| P1["Pattern 1: BST Search/Insert\nUse BST property to go left/right"]

    Q1 -->|No| Q2{"Need to verify\nBST property?"}
    Q2 -->|Yes| P2["Pattern 2: Validation\nPass range (low, high) down"]

    Q2 -->|No| Q3{"Need sorted order\nor kth element?"}
    Q3 -->|Yes| Q3a{"Kth element?"}
    Q3a -->|Yes| P6["Pattern 6: Kth Smallest\nInorder + counter"]
    Q3a -->|No| P4["Pattern 4: BST to Sorted\nInorder traversal"]

    Q3 -->|No| Q4{"Need to find\nnext/prev node?"}
    Q4 -->|Yes| P3["Pattern 3: Successor/Predecessor\nTrack last left/right turn"]

    Q4 -->|No| Q5{"Build BST from\nsorted data?"}
    Q5 -->|Yes| P5["Pattern 5: Balanced BST\nPick middle, recurse"]

    Q5 -->|No| Q6{"Delete a node?"}
    Q6 -->|Yes| P7["Delete: Handle 3 cases\nLeaf / One child / Two children"]

    Q6 -->|No| P8["Consider: Is BST property\nuseful? If not, treat as\ngeneral binary tree"]

    style Start fill:#9C27B0,color:white
    style P1 fill:#4CAF50,color:white
    style P2 fill:#4CAF50,color:white
    style P3 fill:#4CAF50,color:white
    style P4 fill:#4CAF50,color:white
    style P5 fill:#4CAF50,color:white
    style P6 fill:#4CAF50,color:white
    style P7 fill:#4CAF50,color:white
    style P8 fill:#FF9800,color:white
    style Q1 fill:#2196F3,color:white
    style Q2 fill:#2196F3,color:white
    style Q3 fill:#2196F3,color:white
    style Q3a fill:#2196F3,color:white
    style Q4 fill:#2196F3,color:white
    style Q5 fill:#2196F3,color:white
    style Q6 fill:#2196F3,color:white
```

---

## 7. Day Schedule

### Day 26: BST Fundamentals + Core Problems

| Order | Problem | Difficulty | Pattern | Time |
|:-----:|---------|:----------:|---------|:----:|
| 1 | Search in BST (LC 700) | Easy | BST Search | 10 min |
| 2 | Minimum Absolute Diff (LC 530) | Easy | Inorder | 15 min |
| 3 | Range Sum of BST (LC 938) | Easy | DFS | 15 min |
| 4 | Sorted Array to BST (LC 108) | Easy | Divide & Conquer | 15 min |
| 5 | Validate BST (LC 98) | Medium | DFS with Range | 20 min |
| 6 | Kth Smallest (LC 230) | Medium | Inorder | 20 min |
| 7 | Insert into BST (LC 701) | Medium | BST Insert | 15 min |

**Focus**: Master BST search/insert pattern, understand inorder = sorted property.

### Day 27: Advanced BST Operations + Hard Problems

| Order | Problem | Difficulty | Pattern | Time |
|:-----:|---------|:----------:|---------|:----:|
| 1 | Delete Node BST (LC 450) | Medium | BST Delete | 25 min |
| 2 | Inorder Successor (LC 285) | Medium | BST Property | 20 min |
| 3 | LCA in BST (LC 235) | Medium | BST Property | 15 min |
| 4 | BST Iterator (LC 173) | Medium | Controlled Inorder | 20 min |
| 5 | Recover BST (LC 99) | Hard | Inorder | 30 min |
| 6 | Count Smaller After Self (LC 315) | Hard | BST/BIT | 35 min |
| 7 | Serialize/Deserialize BST (LC 449) | Hard | BST Property | 25 min |

**Focus**: Delete operation (3 cases), leveraging BST property for efficiency, hard pattern recognition.

---

## Quick Reference Card

```
BST Essentials:
  - left < root < right (for ALL nodes, not just immediate children)
  - Inorder traversal = sorted order
  - Average operations: O(log n), Worst: O(n)

Interview Tips:
  1. Always ask: "Can I use the BST property here?"
  2. Inorder traversal solves most BST problems
  3. For validation, pass range (low, high) -- do NOT just check left < root < right
  4. BST delete has 3 cases - know them cold
  5. Balanced BST from sorted data = always pick middle
```
