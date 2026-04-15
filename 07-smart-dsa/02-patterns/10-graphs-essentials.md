# Graphs Essentials

## Recognition Signals (how to spot this in <90s)
- Problem mentions nodes/vertices and edges, or cells in a grid that connect to neighbors
- Keywords: "connected components", "reachable", "cycle", "shortest path", "dependencies", "prerequisites"
- You need to visit something and avoid revisiting it (visited set / in-degree tracking)
- The structure is explicitly a graph, or implicitly one (grid, word ladder, friend network)
- Ordering with dependencies → topological sort; grouping connected nodes → Union-Find or DFS flood-fill

## Mental Model
A graph is just a set of nodes and edges. Every graph algorithm boils down to one of four questions: (1) Are these nodes connected? → DFS/BFS or Union-Find. (2) What is the shortest path? → BFS for unweighted, Dijkstra for weighted. (3) Is there a valid ordering given dependencies? → Topological sort (Kahn's BFS). (4) Can I group nodes into components efficiently as edges arrive? → Union-Find.

The single hardest part of graphs for most engineers is not the algorithm itself — it is **translating the problem into graph vocabulary**. Grids are graphs where each cell is a node and its 4 neighbors are edges. Word ladders are graphs where each word is a node and a one-letter-change is an edge. Once you identify nodes, edges, and what you are searching for, the rest is template work.

## Reusable Python Template

### 1. DFS on a Grid (flood-fill / connected components)

```python
def dfs_grid(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited: set[tuple[int, int]] = set()
    components = 0

    def dfs(r: int, c: int) -> None:
        # Mark visited before recursing to avoid re-entry
        visited.add((r, c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and (nr, nc) not in visited
                and grid[nr][nc] == "1"   # ← your validity condition
            ):
                dfs(nr, nc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                dfs(r, c)
                components += 1

    return components
```

### 2. BFS — Shortest Path (unweighted)

```python
from collections import deque

def bfs_shortest_path(
    graph: dict[int, list[int]], src: int, dst: int
) -> int:
    """Returns shortest hop count from src to dst, or -1 if unreachable."""
    visited: set[int] = {src}
    queue: deque[tuple[int, int]] = deque([(src, 0)])  # (node, distance)

    while queue:
        node, dist = queue.popleft()
        if node == dst:
            return dist
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1  # unreachable
```

Key invariant: **mark visited when you enqueue**, not when you dequeue. Marking on dequeue lets duplicate entries pile up and can blow up on dense graphs.

### 3. Topological Sort — Kahn's BFS

```python
from collections import deque

def topo_sort(num_nodes: int, prerequisites: list[tuple[int, int]]) -> list[int]:
    """
    prerequisites: list of (course, prereq) meaning prereq → course.
    Returns topological order, or [] if a cycle exists.
    """
    adj: dict[int, list[int]] = {i: [] for i in range(num_nodes)}
    in_degree: list[int] = [0] * num_nodes

    for course, prereq in prerequisites:
        adj[prereq].append(course)
        in_degree[course] += 1

    # Start with all nodes that have no dependencies
    queue: deque[int] = deque(n for n in range(num_nodes) if in_degree[n] == 0)
    order: list[int] = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If we processed all nodes, no cycle; otherwise cycle exists
    return order if len(order) == num_nodes else []
```

Cycle detection is free: if `len(order) < num_nodes`, some nodes were never reachable from in-degree-0 nodes — a cycle blocked them.

### 4. Union-Find (Disjoint Set Union)

```python
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent: list[int] = list(range(n))
        self.rank: list[int] = [0] * n
        self.components: int = n

    def find(self, x: int) -> int:
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Returns True if x and y were in different components."""
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False  # already connected — adding this edge creates a cycle
        # Union by rank
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.components -= 1
        return True
```

Use Union-Find when edges arrive incrementally and you need fast "same component?" queries. Use DFS/BFS when you need to traverse the structure (e.g., detect a cycle with path info, find actual shortest path).

## Common Mistakes
- **Marking visited on dequeue instead of enqueue (BFS)**: leads to O(V·E) enqueue storms on dense graphs and wrong shortest-path answers when the same node is enqueued multiple times.
- **Mutating the grid instead of using a visited set**: marking cells `"0"` in-place works but destroys input. Acceptable in interviews if you call it out, but a visited set is cleaner and reusable.
- **Forgetting to build the adjacency list and only using the edge list**: iterating over all edges to find neighbors is O(E) per node; an adjacency list gives O(degree) per node.
- **Topological sort cycle check missed**: if you don't compare `len(order) == num_nodes` at the end, you silently return a partial order for a cyclic graph.
- **Union-Find without path compression**: plain `find` is O(n) per call, making the whole thing O(n²). Path compression + union by rank gets you near O(1) amortized.

## Watch Me Solve (I do)

**Problem: Number of Islands (LC 200)**
Given a 2D grid of `"1"` (land) and `"0"` (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent land cells horizontally or vertically.

```
Input:
11110
11010
11000
00000

Output: 1
```

---

I read "2D grid", "connected", "count groups" — that's a connected-components problem on a graph where each `"1"` cell is a node and the 4-directional neighbors are edges. Classic DFS flood-fill. I've solved this shape before: outer loop finds unvisited land, inner DFS sinks the whole island by marking everything reachable.

My plan before coding:
1. Outer double loop over every cell.
2. If the cell is `"1"` and unvisited, increment `islands` and kick off a DFS.
3. DFS marks the current cell visited, then recurses into 4 neighbors if they are in-bounds, unvisited, and `"1"`.
4. When DFS returns, the entire connected component has been marked — outer loop skips all of it.

I'll use a `visited` set rather than mutating the grid, because it's cleaner and the interviewer might ask "what if we can't modify input?"

```python
def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited: set[tuple[int, int]] = set()
    islands = 0

    def dfs(r: int, c: int) -> None:
        visited.add((r, c))                          # mark before recursing
        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:  # 4-directional neighbors
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < rows          # in bounds
                and 0 <= nc < cols
                and (nr, nc) not in visited
                and grid[nr][nc] == "1" # is land
            ):
                dfs(nr, nc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1   # new unvisited land cell = new island
                dfs(r, c)      # flood-fill the whole island

    return islands
```

Dry-run on the 4x5 example: the outer loop hits `(0,0)` which is `"1"` and unvisited. DFS fans out and marks all 9 connected land cells. The rest of the outer loop skips them. Final count: 1. Correct.

Time: O(m·n) — each cell is visited at most once.
Space: O(m·n) — visited set, plus recursion stack up to O(m·n) in the worst case (all land, one big island). If stack depth is a concern, BFS with an explicit queue is drop-in equivalent and avoids recursion limits.

**Edge cases I check before calling it done:**
- Empty grid → guarded by `if not grid`.
- Single cell `[["1"]]` → outer loop hits it, DFS immediately returns, count is 1. Correct.
- All water → outer loop never triggers DFS, returns 0. Correct.

One interviewer follow-up I anticipate: "Can you do it iteratively?" Yes — replace the recursive `dfs` with a BFS using `deque`. The structure (outer loop finds seed → inner loop/queue drains component) is identical; only the traversal order changes.
