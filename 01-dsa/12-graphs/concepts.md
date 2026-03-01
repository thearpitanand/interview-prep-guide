# Graphs - Days 33-35

## 1. What is a Graph?

A **graph** is a data structure consisting of **vertices** (nodes) and **edges** (connections between nodes). Graphs model relationships between objects and are one of the most versatile data structures in computer science.

**Formal Definition**: A graph G = (V, E) where V is a set of vertices and E is a set of edges connecting pairs of vertices.

### Undirected Graph

Edges have **no direction**. If there's an edge between A and B, you can go both ways.

```mermaid
graph LR
    A((A)) --- B((B))
    A --- C((C))
    B --- D((D))
    C --- D
    B --- C

    style A fill:#4CAF50,stroke:#333,color:#fff
    style B fill:#2196F3,stroke:#333,color:#fff
    style C fill:#FF9800,stroke:#333,color:#fff
    style D fill:#9C27B0,stroke:#333,color:#fff
```

### Directed Graph (Digraph)

Edges have a **direction**. An edge from A to B does NOT mean you can go from B to A.

```mermaid
graph LR
    A((A)) --> B((B))
    A --> C((C))
    B --> D((D))
    C --> D
    D --> A

    style A fill:#4CAF50,stroke:#333,color:#fff
    style B fill:#2196F3,stroke:#333,color:#fff
    style C fill:#FF9800,stroke:#333,color:#fff
    style D fill:#9C27B0,stroke:#333,color:#fff
```

### Weighted Graph

Each edge has a **weight** (cost/distance). Used in shortest path problems.

```mermaid
graph LR
    A((A)) -->|4| B((B))
    A -->|2| C((C))
    B -->|5| D((D))
    C -->|1| D
    C -->|3| B

    style A fill:#4CAF50,stroke:#333,color:#fff
    style B fill:#2196F3,stroke:#333,color:#fff
    style C fill:#FF9800,stroke:#333,color:#fff
    style D fill:#9C27B0,stroke:#333,color:#fff
```

### Unweighted Graph

All edges have **equal weight** (or weight = 1). BFS finds the shortest path in unweighted graphs.

```mermaid
graph LR
    A((A)) --- B((B))
    B --- C((C))
    C --- D((D))
    A --- D

    style A fill:#4CAF50,stroke:#333,color:#fff
    style B fill:#2196F3,stroke:#333,color:#fff
    style C fill:#FF9800,stroke:#333,color:#fff
    style D fill:#9C27B0,stroke:#333,color:#fff
```

### Graph Types at a Glance

| Property | Undirected | Directed |
|----------|-----------|----------|
| Edge direction | None (A -- B) | One-way (A -> B) |
| Example | Friendship graph | Twitter follows |
| Degree | Total edges on node | In-degree + Out-degree |
| Cycle detection | Union-Find or DFS | DFS with coloring |

| Property | Weighted | Unweighted |
|----------|----------|------------|
| Edge cost | Variable per edge | All edges equal |
| Shortest path | Dijkstra's / Bellman-Ford | BFS |
| Example | Road network distances | Social network hops |

### Special Graph Types

```mermaid
graph TD
    subgraph DAG["DAG (Directed Acyclic Graph)"]
        D1((A)) --> D2((B))
        D1 --> D3((C))
        D2 --> D4((D))
        D3 --> D4
    end

    subgraph Tree["Tree (Connected Acyclic)"]
        T1((A)) --- T2((B))
        T1 --- T3((C))
        T2 --- T4((D))
        T2 --- T5((E))
    end

    subgraph Bipartite["Bipartite Graph"]
        B1((1)) --- B4((A))
        B1 --- B5((B))
        B2((2)) --- B4
        B3((3)) --- B5
    end

    style D1 fill:#4CAF50,stroke:#333,color:#fff
    style D2 fill:#4CAF50,stroke:#333,color:#fff
    style D3 fill:#4CAF50,stroke:#333,color:#fff
    style D4 fill:#4CAF50,stroke:#333,color:#fff
    style T1 fill:#2196F3,stroke:#333,color:#fff
    style T2 fill:#2196F3,stroke:#333,color:#fff
    style T3 fill:#2196F3,stroke:#333,color:#fff
    style T4 fill:#2196F3,stroke:#333,color:#fff
    style T5 fill:#2196F3,stroke:#333,color:#fff
    style B1 fill:#FF9800,stroke:#333,color:#fff
    style B2 fill:#FF9800,stroke:#333,color:#fff
    style B3 fill:#FF9800,stroke:#333,color:#fff
    style B4 fill:#9C27B0,stroke:#333,color:#fff
    style B5 fill:#9C27B0,stroke:#333,color:#fff
```

- **DAG**: Directed graph with no cycles. Used for task scheduling (topological sort).
- **Tree**: Connected graph with no cycles. Has exactly V-1 edges.
- **Bipartite**: Vertices can be split into two groups where edges only connect across groups.

---

## 2. Graph Representations

### Adjacency Matrix

A 2D array where `matrix[i][j] = 1` (or weight) if there's an edge from vertex i to vertex j.

```mermaid
graph LR
    0((0)) --- 1((1))
    0 --- 2((2))
    1 --- 2
    1 --- 3((3))

    style 0 fill:#4CAF50,stroke:#333,color:#fff
    style 1 fill:#2196F3,stroke:#333,color:#fff
    style 2 fill:#FF9800,stroke:#333,color:#fff
    style 3 fill:#9C27B0,stroke:#333,color:#fff
```

```
    0  1  2  3
0 [ 0, 1, 1, 0 ]
1 [ 1, 0, 1, 1 ]
2 [ 1, 1, 0, 0 ]
3 [ 0, 1, 0, 0 ]
```

```python
# Adjacency Matrix - Undirected Graph
def build_adj_matrix(n, edges):
    """Build adjacency matrix from edge list."""
    matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1  # Remove this line for directed graph
    return matrix

# Usage
edges = [[0, 1], [0, 2], [1, 2], [1, 3]]
matrix = build_adj_matrix(4, edges)
# Check if edge exists: O(1)
print(matrix[0][1])  # 1 (edge exists)
print(matrix[0][3])  # 0 (no edge)
```

### Adjacency List

A dictionary (or list of lists) where each vertex maps to its list of neighbors.

```mermaid
graph LR
    subgraph AdjList["Adjacency List"]
        N0["0: [1, 2]"]
        N1["1: [0, 2, 3]"]
        N2["2: [0, 1]"]
        N3["3: [1]"]
    end

    style N0 fill:#4CAF50,stroke:#333,color:#fff
    style N1 fill:#2196F3,stroke:#333,color:#fff
    style N2 fill:#FF9800,stroke:#333,color:#fff
    style N3 fill:#9C27B0,stroke:#333,color:#fff
```

```python
# Adjacency List - Undirected Graph
from collections import defaultdict

def build_adj_list(n, edges):
    """Build adjacency list from edge list."""
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # Remove this line for directed graph
    return graph

# Usage
edges = [[0, 1], [0, 2], [1, 2], [1, 3]]
graph = build_adj_list(4, edges)
# Get neighbors: O(1) lookup
print(graph[1])  # [0, 2, 3]

# Weighted Adjacency List
def build_weighted_adj_list(n, edges):
    """Build weighted adjacency list. edges = [[u, v, weight], ...]"""
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # Remove for directed
    return graph
```

### Comparison Table

| Operation | Adjacency Matrix | Adjacency List |
|-----------|:---:|:---:|
| Space | O(V^2) | O(V + E) |
| Check edge exists | **O(1)** | O(degree) |
| Get all neighbors | O(V) | **O(degree)** |
| Add edge | O(1) | O(1) |
| Remove edge | O(1) | O(degree) |
| Best for | Dense graphs (E close to V^2) | **Sparse graphs (E << V^2)** |

**Rule of thumb**: Almost always use **adjacency list** in interviews. Most real-world and interview graphs are sparse.

---

## 3. Key Algorithms

### 3.1 BFS - Breadth-First Search (Medium)

BFS explores the graph **level by level**, visiting all neighbors of a node before moving deeper. It uses a **queue** and guarantees the shortest path in **unweighted** graphs.

**Time**: O(V + E) | **Space**: O(V)

```mermaid
graph LR
    A((0)) --- B((1))
    A --- C((2))
    B --- D((3))
    B --- E((4))
    C --- E

    style A fill:#e74c3c,stroke:#333,color:#fff
    style B fill:#e67e22,stroke:#333,color:#fff
    style C fill:#e67e22,stroke:#333,color:#fff
    style D fill:#f1c40f,stroke:#333,color:#000
    style E fill:#f1c40f,stroke:#333,color:#000
```

#### BFS Step-by-Step (Starting from Node 0)

```mermaid
graph TD
    subgraph Step4["Step 4: Visit 3, 4 - Queue: [] - DONE"]
        S4["Visited: {0, 1, 2, 3, 4}<br/>Level 2 complete"]
    end

    subgraph Step3["Step 3: Visit 4 from queue - Queue: [3]"]
        S3["Process 4 -> neighbors 1(seen), 2(seen)<br/>No new nodes added"]
    end

    subgraph Step2["Step 2: Dequeue 1, then 2 - Queue: [3, 4]"]
        S2["Process 1 -> add 3, 4<br/>Process 2 -> 4 already queued<br/>Visited: {0, 1, 2, 3, 4}"]
    end

    subgraph Step1["Step 1: Start at 0 - Queue: [0]"]
        S1["Dequeue 0 -> add neighbors 1, 2<br/>Queue: [1, 2]<br/>Visited: {0, 1, 2}"]
    end

    Step1 --> Step2 --> Step3 --> Step4
```

**Visit Order**: 0 -> 1 -> 2 -> 3 -> 4 (level by level)

```python
from collections import deque

def bfs(graph, start):
    """BFS traversal from start node."""
    visited = set([start])
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

def bfs_shortest_path(graph, start, end):
    """Find shortest path in unweighted graph using BFS."""
    visited = set([start])
    queue = deque([(start, [start])])  # (node, path)

    while queue:
        node, path = queue.popleft()
        if node == end:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []  # No path found
```

**When to use BFS**:
- Shortest path in **unweighted** graph
- Level-order traversal
- Multi-source BFS (start from multiple nodes simultaneously)
- Finding connected components

---

### 3.2 DFS - Depth-First Search (Medium)

DFS explores the graph by going **as deep as possible** before backtracking. It uses a **stack** (or recursion). Good for exploring all paths, detecting cycles, and topological sorting.

**Time**: O(V + E) | **Space**: O(V)

#### DFS Step-by-Step (Starting from Node 0)

```mermaid
graph TD
    subgraph Step5["Step 5: Backtrack to 2, backtrack to 0 - DONE"]
        S5["Visited: {0, 1, 3, 4, 2}<br/>Stack empty, traversal complete"]
    end

    subgraph Step4["Step 4: Visit 2 - Stack: []"]
        S4["Process 2 -> neighbors 0(seen), 4(seen)<br/>No new nodes to push"]
    end

    subgraph Step3["Step 3: Visit 4 - Stack: [2]"]
        S3["Process 4 -> neighbors 1(seen), 2(unseen)<br/>Push 2 -> Stack: [2]"]
    end

    subgraph Step2["Step 2: Visit 3, then backtrack, visit 4 - Stack: [2, 4]"]
        S2["Process 1 -> push 3, 4<br/>Visit 3 (leaf) -> backtrack<br/>Visit 4 next"]
    end

    subgraph Step1["Step 1: Start at 0 - Stack: [0]"]
        S1["Pop 0 -> push neighbors 1, 2<br/>Stack: [2, 1]<br/>Pop 1 next (LIFO)"]
    end

    Step1 --> Step2 --> Step3 --> Step4 --> Step5
```

**Visit Order**: 0 -> 1 -> 3 -> 4 -> 2 (goes deep first)

```python
# Recursive DFS
def dfs_recursive(graph, node, visited=None):
    """DFS traversal using recursion."""
    if visited is None:
        visited = set()

    visited.add(node)
    result = [node]

    for neighbor in graph[node]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result

# Iterative DFS (using explicit stack)
def dfs_iterative(graph, start):
    """DFS traversal using explicit stack."""
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)

        # Add neighbors in reverse order for consistent traversal
        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)

    return order
```

**When to use DFS**:
- Detecting cycles
- Topological sort
- Finding connected components
- Path existence
- Backtracking problems

### BFS vs DFS Comparison

| Property | BFS | DFS |
|----------|-----|-----|
| Data structure | Queue (FIFO) | Stack (LIFO) / Recursion |
| Explores | Level by level | Deep as possible first |
| Shortest path (unweighted) | **Yes** | No |
| Space | O(width of graph) | O(depth of graph) |
| Good for | Shortest path, level-order | Cycle detection, topo sort |

---

### 3.3 Topological Sort (Medium)

Topological sort produces a **linear ordering** of vertices in a **DAG** (Directed Acyclic Graph) such that for every directed edge u -> v, vertex u comes before v in the ordering.

**Use case**: Task scheduling, course prerequisites, build systems.

```mermaid
graph LR
    A((0)) --> B((1))
    A --> C((2))
    B --> D((3))
    C --> D

    style A fill:#4CAF50,stroke:#333,color:#fff
    style B fill:#2196F3,stroke:#333,color:#fff
    style C fill:#FF9800,stroke:#333,color:#fff
    style D fill:#9C27B0,stroke:#333,color:#fff
```

**Valid topological orders**: [0, 1, 2, 3] or [0, 2, 1, 3]

#### Kahn's Algorithm (BFS-based)

Start with nodes that have **in-degree 0** (no prerequisites). Remove them, reduce in-degrees, repeat.

```mermaid
graph TD
    subgraph Step4["Step 4: Process 3 - indegree becomes 0"]
        S4["Queue: [] -> DONE<br/>Result: [0, 1, 2, 3]"]
    end

    subgraph Step3["Step 3: Process 2 - reduce 3's indegree to 0"]
        S3["In-degrees: {3: 0}<br/>Queue: [3]<br/>Result: [0, 1, 2]"]
    end

    subgraph Step2["Step 2: Process 1 - reduce 3's indegree"]
        S2["In-degrees: {2: 0, 3: 1}<br/>Queue: [2]<br/>Result: [0, 1]"]
    end

    subgraph Step1["Step 1: Nodes with in-degree 0: [0]"]
        S1["In-degrees: {0: 0, 1: 1, 2: 1, 3: 2}<br/>Queue: [0]<br/>Process 0 -> reduce 1, 2"]
    end

    Step1 --> Step2 --> Step3 --> Step4
```

```python
from collections import deque, defaultdict

def topological_sort_kahn(num_nodes, edges):
    """Kahn's Algorithm (BFS-based topological sort).

    Returns topological order, or empty list if cycle detected.
    """
    graph = defaultdict(list)
    in_degree = [0] * num_nodes

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Start with all nodes that have in-degree 0
    queue = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If order doesn't contain all nodes, there's a cycle
    return order if len(order) == num_nodes else []
```

#### DFS-based Topological Sort

Run DFS and add nodes to result in **post-order** (after visiting all descendants). Then reverse.

```python
def topological_sort_dfs(num_nodes, edges):
    """DFS-based topological sort.

    Returns topological order, or empty list if cycle detected.
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    # 0 = unvisited, 1 = in current path, 2 = completed
    state = [0] * num_nodes
    order = []
    has_cycle = False

    def dfs(node):
        nonlocal has_cycle
        if has_cycle:
            return
        state[node] = 1  # Mark as in current path

        for neighbor in graph[node]:
            if state[neighbor] == 1:  # Back edge = cycle
                has_cycle = True
                return
            if state[neighbor] == 0:
                dfs(neighbor)

        state[node] = 2  # Mark as completed
        order.append(node)

    for i in range(num_nodes):
        if state[i] == 0:
            dfs(i)

    return order[::-1] if not has_cycle else []
```

---

### 3.4 Dijkstra's Algorithm (Medium)

Finds the **shortest path** from a source to all other vertices in a **weighted graph with non-negative weights**. Uses a **priority queue** (min-heap).

**Time**: O((V + E) log V) | **Space**: O(V)

```mermaid
graph LR
    A((A)) -->|4| B((B))
    A -->|1| C((C))
    B -->|2| D((D))
    C -->|5| D
    C -->|3| B

    style A fill:#4CAF50,stroke:#333,color:#fff
    style B fill:#2196F3,stroke:#333,color:#fff
    style C fill:#FF9800,stroke:#333,color:#fff
    style D fill:#9C27B0,stroke:#333,color:#fff
```

#### Dijkstra Step-by-Step (Source = A)

```mermaid
graph TD
    subgraph Step4["Step 4: Process D(dist=6) - DONE"]
        S4["All nodes processed<br/>Final: A=0, B=4, C=1, D=6"]
    end

    subgraph Step3["Step 3: Process B(dist=4) from PQ"]
        S3["B -> D: 4+2=6 < inf -> update D=6<br/>PQ: [(6,D)]<br/>Dist: {A:0, C:1, B:4, D:6}"]
    end

    subgraph Step2["Step 2: Process C(dist=1) from PQ"]
        S2["C -> D: 1+5=6 -> update D=6<br/>C -> B: 1+3=4 -> update B=4<br/>PQ: [(4,B), (6,D)]<br/>Dist: {A:0, C:1, B:4, D:6}"]
    end

    subgraph Step1["Step 1: Start at A(dist=0)"]
        S1["A -> B: 0+4=4 -> update B=4<br/>A -> C: 0+1=1 -> update C=1<br/>PQ: [(1,C), (4,B)]<br/>Dist: {A:0, B:4, C:1, D:inf}"]
    end

    Step1 --> Step2 --> Step3 --> Step4
```

```python
import heapq
from collections import defaultdict

def dijkstra(graph, start):
    """Dijkstra's shortest path algorithm.

    graph: adjacency list where graph[u] = [(v, weight), ...]
    Returns: dict of shortest distances from start to all nodes.
    """
    dist = {start: 0}
    pq = [(0, start)]  # (distance, node)

    while pq:
        d, u = heapq.heappop(pq)

        # Skip if we've already found a shorter path
        if d > dist.get(u, float('inf')):
            continue

        for v, weight in graph[u]:
            new_dist = d + weight
            if new_dist < dist.get(v, float('inf')):
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist
```

**Key points**:
- Does NOT work with **negative weights** (use Bellman-Ford instead)
- The `if d > dist[u]` check is crucial -- it skips stale entries in the priority queue
- To reconstruct the path, track `parent[v] = u` when updating distances

---

### 3.5 Union-Find / Disjoint Set Union (Medium)

Union-Find tracks **connected components** and efficiently answers "Are A and B connected?" and "Connect A and B".

**Time**: Nearly O(1) per operation (amortized with path compression + union by rank)

#### Core Operations

```mermaid
graph TD
    subgraph Find["Find(x): Follow parent pointers to root"]
        F1["find(4) -> parent[4]=2"]
        F2["find(2) -> parent[2]=0"]
        F3["find(0) -> parent[0]=0 ROOT"]
        F1 --> F2 --> F3
    end

    subgraph Union["Union(x, y): Connect roots of two sets"]
        U1["union(3, 4)"]
        U2["find root of 3 -> 1"]
        U3["find root of 4 -> 0"]
        U4["Attach smaller tree under larger: parent[1] = 0"]
        U1 --> U2 --> U3 --> U4
    end
```

#### Path Compression

After finding the root, make every node on the path point **directly** to the root. This flattens the tree.

```mermaid
graph TD
    subgraph Before["Before Path Compression"]
        B0((0)) --> B1((1))
        B1 --> B2((2))
        B2 --> B3((3))
    end

    subgraph After["After find(3) with Path Compression"]
        A0((0)) --> A1((1))
        A0 --> A2((2))
        A0 --> A3((3))
    end

    style B0 fill:#4CAF50,stroke:#333,color:#fff
    style B1 fill:#2196F3,stroke:#333,color:#fff
    style B2 fill:#FF9800,stroke:#333,color:#fff
    style B3 fill:#9C27B0,stroke:#333,color:#fff
    style A0 fill:#4CAF50,stroke:#333,color:#fff
    style A1 fill:#2196F3,stroke:#333,color:#fff
    style A2 fill:#FF9800,stroke:#333,color:#fff
    style A3 fill:#9C27B0,stroke:#333,color:#fff
```

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Each node is its own parent
        self.rank = [0] * n           # Rank for union by rank

    def find(self, x):
        """Find root with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """Union by rank. Returns False if already connected."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same set

        # Attach smaller tree under larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

    def connected(self, x, y):
        """Check if x and y are in the same set."""
        return self.find(x) == self.find(y)
```

**When to use Union-Find**:
- "Are these nodes connected?" queries
- Counting connected components
- Detecting cycles in undirected graphs
- Kruskal's MST algorithm

---

### 3.6 Cycle Detection (Medium)

#### Cycle in Directed Graph -- DFS Coloring

Use three states: **WHITE** (unvisited), **GRAY** (in current DFS path), **BLACK** (fully processed). A back edge (to a GRAY node) means a cycle.

```mermaid
graph LR
    A((0)) --> B((1))
    B --> C((2))
    C --> A

    style A fill:#808080,stroke:#333,color:#fff
    style B fill:#808080,stroke:#333,color:#fff
    style C fill:#808080,stroke:#333,color:#fff
```

```mermaid
graph TD
    subgraph Step3["Step 3: Visit 2 -> neighbor 0 is GRAY = CYCLE!"]
        S3["Node 2 = GRAY<br/>Neighbor 0 = GRAY (back edge)<br/>CYCLE DETECTED: 0 -> 1 -> 2 -> 0"]
    end

    subgraph Step2["Step 2: Visit 1 -> go to 2"]
        S2["Node 0 = GRAY, Node 1 = GRAY<br/>Visit neighbor 2"]
    end

    subgraph Step1["Step 1: Start DFS from 0"]
        S1["Mark 0 as GRAY<br/>Visit neighbor 1, mark as GRAY"]
    end

    Step1 --> Step2 --> Step3
```

```python
def has_cycle_directed(graph, num_nodes):
    """Detect cycle in directed graph using DFS coloring.

    WHITE=0, GRAY=1, BLACK=2
    """
    color = [0] * num_nodes  # All WHITE

    def dfs(node):
        color[node] = 1  # GRAY - in current path

        for neighbor in graph[node]:
            if color[neighbor] == 1:  # Back edge to GRAY node
                return True  # Cycle found
            if color[neighbor] == 0 and dfs(neighbor):
                return True

        color[node] = 2  # BLACK - fully processed
        return False

    for i in range(num_nodes):
        if color[i] == 0:
            if dfs(i):
                return True
    return False
```

#### Cycle in Undirected Graph -- Union-Find

For each edge, check if the two endpoints are already connected. If yes, adding this edge creates a cycle.

```python
def has_cycle_undirected(n, edges):
    """Detect cycle in undirected graph using Union-Find."""
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):  # Already connected = cycle
            return True
    return False
```

---

### 3.7 Bellman-Ford Algorithm (Hard)

Finds shortest paths from a source when **negative weights** exist. Can also detect **negative weight cycles**.

**Time**: O(V * E) | **Space**: O(V)

**Key idea**: Relax all edges V-1 times. If we can still relax on the V-th pass, there's a negative cycle.

```mermaid
graph LR
    A((A)) -->|4| B((B))
    A -->|5| C((C))
    B -->|-3| C
    C -->|2| D((D))

    style A fill:#4CAF50,stroke:#333,color:#fff
    style B fill:#2196F3,stroke:#333,color:#fff
    style C fill:#FF9800,stroke:#333,color:#fff
    style D fill:#9C27B0,stroke:#333,color:#fff
```

#### Bellman-Ford Step-by-Step (Source = A)

```mermaid
graph TD
    subgraph Round3["Round 3: No changes -> DONE"]
        R3["Dist: {A:0, B:4, C:1, D:3}<br/>No updates = converged"]
    end

    subgraph Round2["Round 2: Relax all edges"]
        R2["Edge B->C: 4+(-3)=1 < 5 -> update C=1<br/>Edge C->D: 1+2=3 < 7 -> update D=3<br/>Dist: {A:0, B:4, C:1, D:3}"]
    end

    subgraph Round1["Round 1: Relax all edges"]
        R1["Edge A->B: 0+4=4 < inf -> update B=4<br/>Edge A->C: 0+5=5 < inf -> update C=5<br/>Edge B->C: 4+(-3)=1 < 5 -> update C=1<br/>Edge C->D: 1+2=3 < inf -> update D=3<br/>Dist: {A:0, B:4, C:1, D:3}"]
    end

    subgraph Init["Initialize: dist[A]=0, all others=inf"]
        I["Dist: {A:0, B:inf, C:inf, D:inf}"]
    end

    Init --> Round1 --> Round2 --> Round3
```

```python
def bellman_ford(n, edges, start):
    """Bellman-Ford shortest path algorithm.

    edges: list of (u, v, weight)
    Returns: distances dict, or None if negative cycle exists.
    """
    dist = [float('inf')] * n
    dist[start] = 0

    # Relax all edges V-1 times
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative weight cycles (V-th pass)
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None  # Negative cycle detected

    return dist
```

### Dijkstra vs Bellman-Ford

| Property | Dijkstra | Bellman-Ford |
|----------|----------|--------------|
| Time | O((V+E) log V) | O(V * E) |
| Negative weights | **No** | **Yes** |
| Negative cycles | Cannot detect | **Can detect** |
| Data structure | Priority queue | Simple array |
| Use when | Non-negative weights | Negative weights possible |

---

## 4. Algorithm Selection Matrix

```mermaid
flowchart TD
    Start["Graph Problem"] --> Q1{"Weighted<br/>edges?"}

    Q1 -->|No| Q2{"Shortest path<br/>needed?"}
    Q2 -->|Yes| A1["BFS<br/>(unweighted shortest path)"]
    Q2 -->|No| Q3{"Detect cycle?"}
    Q3 -->|"Directed"| A2["DFS Coloring<br/>(WHITE/GRAY/BLACK)"]
    Q3 -->|"Undirected"| A3["Union-Find"]
    Q3 -->|No| Q4{"Ordering /<br/>scheduling?"}
    Q4 -->|Yes| A4["Topological Sort<br/>(Kahn's or DFS)"]
    Q4 -->|No| Q5{"Connected<br/>components?"}
    Q5 -->|Yes| A5["BFS/DFS or Union-Find"]
    Q5 -->|No| A6["BFS or DFS traversal"]

    Q1 -->|Yes| Q6{"Negative<br/>weights?"}
    Q6 -->|No| A7["Dijkstra's Algorithm"]
    Q6 -->|Yes| Q7{"Negative<br/>cycles?"}
    Q7 -->|"Detect/Handle"| A8["Bellman-Ford"]
    Q7 -->|No| A8

    style A1 fill:#4CAF50,stroke:#333,color:#fff
    style A2 fill:#e74c3c,stroke:#333,color:#fff
    style A3 fill:#FF9800,stroke:#333,color:#fff
    style A4 fill:#9C27B0,stroke:#333,color:#fff
    style A5 fill:#2196F3,stroke:#333,color:#fff
    style A6 fill:#607D8B,stroke:#333,color:#fff
    style A7 fill:#00BCD4,stroke:#333,color:#fff
    style A8 fill:#795548,stroke:#333,color:#fff
```

### Quick Reference Table

| Problem Signal | Algorithm | Time |
|---------------|-----------|------|
| "Shortest path" + unweighted | BFS | O(V + E) |
| "Shortest path" + weighted (non-negative) | Dijkstra | O((V+E) log V) |
| "Shortest path" + negative weights | Bellman-Ford | O(V * E) |
| "Can I finish all courses?" / ordering | Topological Sort | O(V + E) |
| "Number of islands" / connected groups | BFS/DFS | O(V + E) |
| "Is there a cycle?" (directed) | DFS coloring | O(V + E) |
| "Is there a cycle?" (undirected) | Union-Find | O(V * alpha(V)) |
| "Redundant edge" / connected? | Union-Find | O(V * alpha(V)) |
| "Bipartite check" / 2-coloring | BFS/DFS | O(V + E) |
| "Bridge" / "Articulation point" | Tarjan's | O(V + E) |

---

## 5. Common Mistakes

### 1. Forgetting the Visited Set

```python
# WRONG - infinite loop on cyclic graphs!
def bfs_wrong(graph, start):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            queue.append(neighbor)  # Will revisit nodes forever!

# RIGHT - always track visited nodes
def bfs_right(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### 2. Directed vs Undirected Confusion

```python
# Building undirected graph - MUST add both directions
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)  # Don't forget this for undirected!

# Building directed graph - only one direction
for u, v in edges:
    graph[u].append(v)  # Only u -> v
```

### 3. 0-Indexed vs 1-Indexed Nodes

```python
# If nodes are 1-indexed (like in many LC problems)
# Make sure arrays are sized correctly
n = 4  # Nodes 1, 2, 3, 4
in_degree = [0] * (n + 1)  # Index 0 unused, but safe

# Or convert to 0-indexed
for u, v in edges:
    graph[u - 1].append(v - 1)
```

### 4. Not Handling Disconnected Graphs

```python
# WRONG - only visits component containing node 0
visited = set()
dfs(graph, 0, visited)

# RIGHT - visit ALL components
visited = set()
for node in range(n):
    if node not in visited:
        dfs(graph, node, visited)
```

### 5. Using Dijkstra with Negative Weights

```python
# WRONG - Dijkstra does NOT work with negative weights!
# It may give incorrect results because it assumes
# once a node is processed, its distance is final.

# RIGHT - Use Bellman-Ford for negative weights
dist = bellman_ford(n, edges, start)
```

### 6. Grid Graphs -- Forgetting Bounds Check

```python
# For grid-based graph problems (islands, flood fill, etc.)
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for dr, dc in directions:
    nr, nc = r + dr, c + dc
    # ALWAYS check bounds before accessing grid
    if 0 <= nr < rows and 0 <= nc < cols:
        if grid[nr][nc] == target and (nr, nc) not in visited:
            # process...
```

---

## 6. Day Schedule

### Day 33: BFS/DFS Basics

| # | Problem | Difficulty | Pattern | Time |
|---|---------|:---:|---------|------|
| 1 | Find if Path Exists (LC 1971) | Easy | BFS/DFS | 10 min |
| 2 | Flood Fill (LC 733) | Easy | BFS/DFS on Grid | 12 min |
| 3 | Find Town Judge (LC 997) | Easy | In/Out Degree | 10 min |
| 4 | Find Center of Star (LC 1791) | Easy | Graph Property | 8 min |
| 5 | Number of Islands (LC 200) | Medium | DFS/BFS on Grid | 15 min |
| 6 | Clone Graph (LC 133) | Medium | BFS/DFS + HashMap | 15 min |

**Total estimated time: ~1.2 hours**

### Day 34: Topological Sort & Dijkstra

| # | Problem | Difficulty | Pattern | Time |
|---|---------|:---:|---------|------|
| 1 | Course Schedule (LC 207) | Medium | Topo Sort / Cycle | 15 min |
| 2 | Course Schedule II (LC 210) | Medium | Topological Sort | 15 min |
| 3 | Rotting Oranges (LC 994) | Medium | Multi-source BFS | 15 min |
| 4 | Surrounded Regions (LC 130) | Medium | DFS from Boundary | 15 min |
| 5 | Network Delay Time (LC 743) | Medium | Dijkstra | 15 min |

**Total estimated time: ~1.25 hours**

### Day 35: Union-Find, Hard Problems & Review

| # | Problem | Difficulty | Pattern | Time |
|---|---------|:---:|---------|------|
| 1 | Redundant Connection (LC 684) | Medium | Union-Find | 15 min |
| 2 | Pacific Atlantic Water Flow (LC 417) | Medium | Multi-source DFS | 20 min |
| 3 | Is Graph Bipartite? (LC 785) | Medium | BFS/DFS Coloring | 15 min |
| 4 | Word Ladder (LC 127) | Hard | BFS | 20 min |
| 5 | Alien Dictionary (LC 269) | Hard | Topological Sort | 20 min |
| 6 | Cheapest Flights (LC 787) | Hard | Bellman-Ford | 20 min |
| 7 | Critical Connections (LC 1192) | Hard | Tarjan's Algorithm | 25 min |

**Total estimated time: ~2.25 hours**

**Suggested order**: Master BFS/DFS on Day 33, then topological sort and Dijkstra on Day 34, and tackle harder Union-Find and advanced problems on Day 35. If short on time, prioritize: LC 200, LC 207, LC 743, LC 127.
