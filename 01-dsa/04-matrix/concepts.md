# Matrix (2D Array) - Days 15-16

## 1. What is a Matrix?

A **matrix** is a 2D array organized in rows and columns. In Python, we represent it as a list of lists. Elements are accessed by `matrix[row][col]`.

### Row-Major Order

Elements are stored row by row in memory:

```mermaid
graph LR
    subgraph "Matrix (3x3)"
        direction TB
        subgraph "Row 0"
            A["[0,0]=1"] --- B["[0,1]=2"] --- C["[0,2]=3"]
        end
        subgraph "Row 1"
            D["[1,0]=4"] --- E["[1,1]=5"] --- F["[1,2]=6"]
        end
        subgraph "Row 2"
            G["[2,0]=7"] --- H["[2,1]=8"] --- I["[2,2]=9"]
        end
    end
```

```mermaid
block-beta
    columns 3
    block:row0["Row 0"]
        columns 3
        a["1"] b["2"] c["3"]
    end
    block:row1["Row 1"]
        columns 3
        d["4"] e["5"] f["6"]
    end
    block:row2["Row 2"]
        columns 3
        g["7"] h["8"] i["9"]
    end

    style a fill:#4CAF50,color:#fff
    style b fill:#4CAF50,color:#fff
    style c fill:#4CAF50,color:#fff
    style d fill:#2196F3,color:#fff
    style e fill:#2196F3,color:#fff
    style f fill:#2196F3,color:#fff
    style g fill:#FF9800,color:#fff
    style h fill:#FF9800,color:#fff
    style i fill:#FF9800,color:#fff
```

**Key dimensions:**
- `rows = len(matrix)`
- `cols = len(matrix[0])`
- Total elements = rows * cols

---

## 2. Matrix Operations in Python

### Using Nested Lists

```python
# Create a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element at row 1, col 2
val = matrix[1][2]  # 6

# Get dimensions
rows = len(matrix)       # 3
cols = len(matrix[0])    # 3

# Iterate all elements
for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=" ")
    print()
```

### Common Initialization Patterns

```python
# WRONG - all rows share same reference!
bad = [[0] * 3] * 3

# CORRECT - each row is independent
good = [[0] * 3 for _ in range(3)]

# Initialize m x n matrix
m, n = 4, 3
grid = [[0] * n for _ in range(m)]
```

### Accessing Rows and Columns

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]

# Get row i (easy)
row = matrix[1]  # [4, 5, 6]

# Get column j (need list comprehension)
col = [matrix[r][2] for r in range(len(matrix))]  # [3, 6, 9]

# Get diagonal (top-left to bottom-right)
diag = [matrix[i][i] for i in range(len(matrix))]  # [1, 5, 9]

# Get anti-diagonal
n = len(matrix)
anti = [matrix[i][n-1-i] for i in range(n)]  # [3, 5, 7]
```

### 4-Directional Movement

```python
# The 4 neighbors of (r, c)
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for dr, dc in directions:
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        # (nr, nc) is a valid neighbor
        pass
```

---

## 3. Key Patterns

---

### Pattern 1: Spiral Traversal

Traverse the matrix in a spiral (clockwise) order by maintaining four boundaries: top, bottom, left, right. Shrink them inward after processing each edge.

```mermaid
graph TD
    subgraph "Spiral Traversal on 3x4 Matrix"
        direction TB
        A["Step 1: Traverse top row LEFT to RIGHT<br/>top=0, move top down"]
        B["Step 2: Traverse right col TOP to BOTTOM<br/>right=3, move right left"]
        C["Step 3: Traverse bottom row RIGHT to LEFT<br/>bottom=2, move bottom up"]
        D["Step 4: Traverse left col BOTTOM to TOP<br/>left=0, move left right"]
        E["Repeat until boundaries cross"]

        A --> B --> C --> D --> E
    end
```

```mermaid
graph LR
    subgraph "Boundary Movement"
        direction TB
        subgraph "Initial"
            T1["top=0"]
            B1["bottom=2"]
            L1["left=0"]
            R1["right=3"]
        end
        subgraph "After 1 loop"
            T2["top=1"]
            B2["bottom=1"]
            L2["left=1"]
            R2["right=2"]
        end
    end
    Initial -->|"shrink"| After_1_loop
```

**Template:**
```python
def spiral_order(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # go right across top row
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1

        # go down along right col
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1

        # go left across bottom row (if still valid)
        if top <= bottom:
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1

        # go up along left col (if still valid)
        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1

    return result
```

**When to use:** Any problem asking for spiral, layer-by-layer, or onion-peel traversal.

---

### Pattern 2: Diagonal Traversal

Traverse elements along diagonals. Two main types:
- **Primary diagonals** (top-left to bottom-right): `row - col` is constant
- **Anti-diagonals** (top-right to bottom-left): `row + col` is constant

```mermaid
graph TD
    subgraph "Primary Diagonals (row - col = constant)"
        direction LR
        D0["d=0: (0,0) (1,1) (2,2)"]
        D1["d=1: (1,0) (2,1)"]
        Dn1["d=-1: (0,1) (1,2)"]
        D2["d=2: (2,0)"]
        Dn2["d=-2: (0,2)"]
    end
```

```mermaid
graph TD
    subgraph "Anti-Diagonals (row + col = constant)"
        direction LR
        S0["sum=0: (0,0)"]
        S1["sum=1: (0,1) (1,0)"]
        S2["sum=2: (0,2) (1,1) (2,0)"]
        S3["sum=3: (1,2) (2,1)"]
        S4["sum=4: (2,2)"]
    end
```

**Template:**
```python
from collections import defaultdict

def diagonal_traverse(matrix):
    diags = defaultdict(list)
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            diags[r + c].append(matrix[r][c])  # anti-diagonal grouping

    result = []
    for key in sorted(diags):
        if key % 2 == 0:
            result.extend(diags[key][::-1])  # reverse even diagonals
        else:
            result.extend(diags[key])
    return result
```

**When to use:** Diagonal print, zigzag traversal, or when elements on same diagonal share a property.

---

### Pattern 3: Staircase Search (Search in Sorted Matrix)

For a matrix where each row and column is sorted in ascending order, start from the **top-right corner** (or bottom-left). At each step, eliminate an entire row or column.

```mermaid
graph TD
    subgraph "Search for target=14 in sorted matrix"
        direction TB
        S1["Start at top-right: (0,3)=15<br/>15 > 14 -> move LEFT"]
        S2["At (0,2)=11<br/>11 < 14 -> move DOWN"]
        S3["At (1,2)=14<br/>14 == 14 -> FOUND!"]

        S1 --> S2 --> S3
    end
```

```mermaid
graph LR
    subgraph "Matrix with search path"
        direction TB
        R0["1  4  7  ❌15"]
        R1["2  5  8  19"]
        R2["3  6  ✅14 22"]
        R3["10 13 17 24"]
    end

    subgraph "Logic"
        direction TB
        L1["if val > target: move LEFT (eliminate column)"]
        L2["if val < target: move DOWN (eliminate row)"]
        L3["if val == target: FOUND"]
        L1 --- L2 --- L3
    end
```

**Template:**
```python
def search_matrix(matrix, target):
    if not matrix:
        return False
    rows, cols = len(matrix), len(matrix[0])
    r, c = 0, cols - 1  # start top-right

    while r < rows and c >= 0:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            c -= 1  # eliminate column
        else:
            r += 1  # eliminate row

    return False
```

**Time: O(m + n)** -- much better than O(m*n) brute force!

**When to use:** Matrix is sorted row-wise AND column-wise, search / count problems.

---

### Pattern 4: In-place Modification

Modify the matrix without extra space. Common tricks:
- **Use first row/col as markers** (Set Matrix Zeroes)
- **Transpose + Reverse** (Rotate Image)
- **Swap in layers** (Rotate by rings)

```mermaid
graph TD
    subgraph "Rotate 90 degrees Clockwise"
        direction LR
        A["Original<br/>1 2 3<br/>4 5 6<br/>7 8 9"]
        B["Step 1: Transpose<br/>1 4 7<br/>2 5 8<br/>3 6 9"]
        C["Step 2: Reverse rows<br/>7 4 1<br/>8 5 2<br/>9 6 3"]
        A -->|"swap [i][j] with [j][i]"| B
        B -->|"reverse each row"| C
    end
```

```mermaid
graph TD
    subgraph "Set Matrix Zeroes - Use first row/col as flags"
        direction TB
        S1["Scan matrix for zeroes"]
        S2["Mark matrix[0][col]=0 and matrix[row][0]=0<br/>as flags in first row/col"]
        S3["Use a separate variable for<br/>whether first row/col themselves had zeroes"]
        S4["Second pass: set cells to 0<br/>based on flags"]
        S5["Handle first row and first col last"]

        S1 --> S2 --> S3 --> S4 --> S5
    end
```

**When to use:** Problem says "in-place" or "O(1) extra space." Look for symmetry or reuse existing cells.

---

### Pattern 5: Island / Grid DFS/BFS

Treat the grid as a graph. Each cell is a node, and adjacent cells (4-directional) are edges. Use DFS or BFS to explore connected components.

```mermaid
graph TD
    subgraph "Number of Islands - DFS"
        direction TB
        S1["Iterate through every cell"]
        S2{"Is cell == '1'<br/>and not visited?"}
        S3["Run DFS/BFS from this cell<br/>Mark all connected '1's as visited"]
        S4["Increment island count"]
        S5["Continue to next cell"]

        S1 --> S2
        S2 -->|Yes| S3 --> S4 --> S5
        S2 -->|No| S5
        S5 -->|"next cell"| S1
    end
```

```mermaid
graph TD
    subgraph "DFS on Grid - Mark visited by changing value"
        direction TB
        A["At cell (r,c)"]
        B["Mark as visited:<br/>grid[r][c] = '0'"]
        C["Check all 4 neighbors"]
        D{"Neighbor valid<br/>and == '1'?"}
        E["Recurse DFS on neighbor"]

        A --> B --> C --> D
        D -->|Yes| E --> C
        D -->|No| F["Return"]
    end
```

**Template:**
```python
def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        grid[r][c] = '0'  # mark visited
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1

    return count
```

**When to use:** Connected components, flood fill, shortest path in grid, surrounded regions, island problems.

---

## 4. Which Pattern to Use?

```mermaid
flowchart TD
    Start["Matrix Problem"] --> Q1{"Traversal order<br/>specified?"}

    Q1 -->|"Spiral"| P1["Spiral Traversal<br/>Use 4 boundaries"]
    Q1 -->|"Diagonal"| P2["Diagonal Traversal<br/>Group by r+c or r-c"]
    Q1 -->|"No specific order"| Q2{"Is matrix sorted<br/>row & col wise?"}

    Q2 -->|"Yes"| Q3{"Search or<br/>count?"}
    Q3 -->|"Yes"| P3["Staircase Search<br/>Start top-right"]
    Q3 -->|"No"| Q4

    Q2 -->|"No"| Q4{"Modify matrix<br/>in-place?"}

    Q4 -->|"Rotate"| P4A["Transpose + Reverse"]
    Q4 -->|"Set zeroes"| P4B["Use first row/col<br/>as markers"]
    Q4 -->|"No"| Q5{"Grid with connected<br/>components?"}

    Q5 -->|"Yes"| P5["DFS/BFS on Grid<br/>4-directional traversal"]
    Q5 -->|"No"| P6["Brute force or<br/>other technique"]

    style P1 fill:#4CAF50,color:#fff
    style P2 fill:#2196F3,color:#fff
    style P3 fill:#FF9800,color:#fff
    style P4A fill:#9C27B0,color:#fff
    style P4B fill:#9C27B0,color:#fff
    style P5 fill:#F44336,color:#fff
    style P6 fill:#607D8B,color:#fff
```

---

## 5. Common Mistakes

| Mistake | Fix |
|---|---|
| Confusing `row` and `col` indices | Always use `matrix[row][col]`, rows = `len(matrix)`, cols = `len(matrix[0])` |
| Wrong initialization: `[[0]*n]*m` | Use `[[0]*n for _ in range(m)]` -- each row must be independent |
| Off-by-one in spiral boundaries | Check `top <= bottom` and `left <= right` before inner loops |
| Not marking visited in grid DFS | Either mutate grid or use a `visited` set to avoid infinite loops |
| Modifying matrix while reading it | Use flags/markers first, then do a second pass to apply changes |
| Forgetting bounds check in DFS/BFS | Always check `0 <= r < rows and 0 <= c < cols` before accessing |

---

## 6. Day Schedule

### Day 15 (Easy + Medium Foundations)

| # | Problem | Difficulty | Pattern | Time Target |
|---|---------|-----------|---------|-------------|
| 1 | Matrix Transpose (LC 867) | Easy | Matrix Manipulation | 10 min |
| 2 | Flood Fill (LC 733) | Easy | DFS/BFS | 15 min |
| 3 | Island Perimeter (LC 463) | Easy | Grid Traversal | 15 min |
| 4 | Spiral Matrix (LC 54) | Medium | Spiral Traversal | 20 min |
| 5 | Rotate Image (LC 48) | Medium | In-place Rotation | 20 min |

**Focus:** Get comfortable with matrix traversal, boundary handling, and basic grid DFS.

### Day 16 (Medium + Hard)

| # | Problem | Difficulty | Pattern | Time Target |
|---|---------|-----------|---------|-------------|
| 1 | Set Matrix Zeroes (LC 73) | Medium | In-place Modification | 20 min |
| 2 | Word Search (LC 79) | Medium | DFS/Backtracking | 25 min |
| 3 | Maximal Rectangle (LC 85) | Hard | Stack/Histogram | 35 min |
| 4 | Number of Islands (LC 200) | Hard | DFS/BFS | 20 min |

**Focus:** In-place tricks, backtracking on grids, and combining matrix with other data structures (stacks).
