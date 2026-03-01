# Trie (Prefix Tree) - Day 40

## 1. What is a Trie?

A **Trie** (pronounced "try") is a tree-like data structure used to efficiently store and retrieve strings. It is also called a **prefix tree** because it organizes words by their shared prefixes.

Each node in a trie represents a single character. A path from the root to a node marked as `is_end = True` represents a complete word. Every node has:
- A **children** dictionary mapping characters to child nodes
- An **is_end** boolean flag indicating if a valid word ends at this node

### Trie After Inserting "apple", "app", "banana"

```mermaid
graph TD
    ROOT["root"]

    ROOT --> A1["a"]
    A1 --> P1["p"]
    P1 --> P2["p"]
    P2 -->|"is_end=True<br/>(app)"| L1["l"]
    L1 --> E1["e<br/>is_end=True<br/>(apple)"]

    ROOT --> B1["b"]
    B1 --> A2["a"]
    A2 --> N1["n"]
    N1 --> A3["a"]
    A3 --> N2["n"]
    N2 --> A4["a<br/>is_end=True<br/>(banana)"]

    style ROOT fill:#2d2d2d,stroke:#fff,color:#fff
    style P2 fill:#4a6,stroke:#fff,color:#fff
    style E1 fill:#4a6,stroke:#fff,color:#fff
    style A4 fill:#4a6,stroke:#fff,color:#fff
```

**Key insight**: Words sharing a common prefix share the same path in the trie. "apple" and "app" share the path `a -> p -> p`.

---

## 2. How It Works

### Insertion: Inserting "cat" Character by Character

```mermaid
graph LR
    subgraph Step1["Step 1: Insert 'c'"]
        R1["root"] --> C1["c"]
    end

    subgraph Step2["Step 2: Insert 'a'"]
        R2["root"] --> C2["c"] --> A2["a"]
    end

    subgraph Step3["Step 3: Insert 't' + mark end"]
        R3["root"] --> C3["c"] --> A3["a"] --> T3["t<br/>is_end=True"]
    end

    Step1 -.-> Step2 -.-> Step3

    style T3 fill:#4a6,stroke:#fff,color:#fff
```

**Insertion Algorithm:**
1. Start at the root node
2. For each character in the word:
   - If the character exists in current node's children, move to that child
   - If not, create a new node and add it as a child
3. After the last character, mark the node's `is_end = True`

### Search: Searching for "cat"

```mermaid
graph TD
    subgraph Search["Search 'cat'"]
        direction LR
        S1["root<br/>look for 'c'"] -->|"found"| S2["c<br/>look for 'a'"]
        S2 -->|"found"| S3["a<br/>look for 't'"]
        S3 -->|"found"| S4["t<br/>is_end=True?<br/>YES -> return True"]
    end

    style S4 fill:#4a6,stroke:#fff,color:#fff
```

**Search Algorithm:**
1. Start at the root node
2. For each character in the word:
   - If the character exists in children, move to that child
   - If not, return `False` (word not in trie)
3. After traversing all characters, return the value of `is_end`

**Prefix Search (startsWith):** Same as search, but return `True` after traversing all prefix characters regardless of `is_end`.

---

## 3. TrieNode & Trie Implementation in Python

```python
class TrieNode:
    def __init__(self):
        self.children = {}   # char -> TrieNode
        self.is_end = False  # marks end of a complete word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        """Return True if the word is in the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        """Return True if any word in the trie starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

### How the Node Structure Looks in Memory

```mermaid
graph TD
    subgraph TrieNode["TrieNode Structure"]
        N["TrieNode"]
        C["children: dict"]
        E["is_end: bool"]
        N --> C
        N --> E
    end

    subgraph Example["Example: After insert('go', 'got')"]
        ROOT["root<br/>is_end=False"]
        G["'g'<br/>is_end=False"]
        O["'o'<br/>is_end=True"]
        T["'t'<br/>is_end=True"]
        ROOT -->|"children['g']"| G
        G -->|"children['o']"| O
        O -->|"children['t']"| T
    end

    style O fill:#4a6,stroke:#fff,color:#fff
    style T fill:#4a6,stroke:#fff,color:#fff
```

---

## 4. Operations & Time Complexities

| Operation | Time Complexity | Description |
|-----------|----------------|-------------|
| Insert | O(L) | Traverse/create L nodes for a word of length L |
| Search | O(L) | Traverse L nodes to check if word exists |
| Prefix Search (startsWith) | O(L) | Traverse L nodes to check if prefix exists |
| Delete | O(L) | Traverse L nodes, unmark/remove as needed |
| Autocomplete (all words with prefix) | O(L + K) | L to reach prefix node, K = total chars in all matching words |

**Space Complexity:** O(N * L) in the worst case, where N = number of words, L = average word length. In practice, shared prefixes significantly reduce this.

| Scenario | Space |
|----------|-------|
| No shared prefixes | O(N * L) - worst case |
| Many shared prefixes | Much less than O(N * L) |
| All words identical | O(L) - best case |

---

## 5. Key Patterns

### Pattern 1: Basic Trie (Medium)

The foundation pattern. Implement a trie with `insert`, `search`, and `startsWith`.

```mermaid
graph TD
    ROOT["root"]
    ROOT --> H["h"]
    H --> E1["e"]
    E1 --> L["l"]
    L --> L2["l"]
    L2 --> O["o<br/>is_end=True<br/>(hello)"]

    ROOT --> H2["h"]

    E1 --> A["a"]
    A --> P["p<br/>is_end=True<br/>(heap)"]

    ROOT --> W["w"]
    W --> O2["o"]
    O2 --> R["r"]
    R --> D["d<br/>is_end=True<br/>(word)"]

    style O fill:#4a6,stroke:#fff,color:#fff
    style P fill:#4a6,stroke:#fff,color:#fff
    style D fill:#4a6,stroke:#fff,color:#fff
```

**When to use:** Any problem that asks you to store strings and query them by prefix.

**Problems:** LC 208 (Implement Trie)

---

### Pattern 2: Autocomplete / Prefix Search (Medium)

After reaching the prefix node, run DFS to collect all complete words below it.

```mermaid
graph TD
    subgraph DFS["DFS from prefix 'ap'"]
        ROOT["root"] --> A["a"]
        A --> P["p<br/>(prefix ends here)"]
        P --> P2["p"]
        P2 -->|"is_end"| WORD1["'app'"]
        P2 --> L["l"]
        L --> E["e"]
        E -->|"is_end"| WORD2["'apple'"]
        P --> E2["e"]
        E2 -->|"is_end"| WORD3["'ape'"]
    end

    style P fill:#f96,stroke:#fff,color:#fff
    style WORD1 fill:#4a6,stroke:#fff,color:#fff
    style WORD2 fill:#4a6,stroke:#fff,color:#fff
    style WORD3 fill:#4a6,stroke:#fff,color:#fff
```

**Algorithm:**
1. Navigate to the prefix node
2. Run DFS from that node
3. Whenever you reach a node with `is_end = True`, add the accumulated word to results

**When to use:** Autocomplete systems, finding all words with a given prefix.

**Problems:** LC 648 (Replace Words), LC 677 (Map Sum Pairs), LC 211 (Add and Search Word)

---

### Pattern 3: Word Search in Grid (Hard)

Combine a trie with backtracking to efficiently search for multiple words in a 2D grid.

```mermaid
graph TD
    subgraph Approach["Trie + Backtracking"]
        BUILD["1. Build trie from<br/>word list"]
        ITERATE["2. For each cell in grid,<br/>start DFS if char<br/>matches trie root child"]
        EXPLORE["3. Explore 4 directions,<br/>follow trie path"]
        FOUND["4. If is_end=True,<br/>add word to result"]
        PRUNE["5. Prune trie node<br/>after finding word<br/>(optimization)"]

        BUILD --> ITERATE --> EXPLORE --> FOUND --> PRUNE
    end

    style FOUND fill:#4a6,stroke:#fff,color:#fff
    style PRUNE fill:#f96,stroke:#fff,color:#fff
```

**Why trie?** Without a trie, you would need to search for each word separately (N * M * 4^L). With a trie, you search for all words simultaneously during a single traversal.

**Problems:** LC 212 (Word Search II)

---

### Pattern 4: XOR Trie / Binary Trie (Hard)

Store numbers in binary form (bit by bit) in a trie. Used for maximum XOR problems.

```mermaid
graph TD
    subgraph BinaryTrie["Binary Trie for [3, 5, 8]"]
        ROOT["root"]
        ROOT -->|"0"| Z1["0"]
        ROOT -->|"1"| O1["1"]

        Z1 -->|"0"| Z2["0"]
        Z1 -->|"1"| O2["0"]

        Z2 -->|"1"| Z3["1"]
        Z3 -->|"1"| V3["1<br/>(3=0011)"]

        O2 -->|"0"| O3["0"]
        O3 -->|"1"| V5["1<br/>(5=0101)"]

        O1 -->|"0"| O4["0"]
        O4 -->|"0"| O5["0"]
        O5 -->|"0"| V8["0<br/>(8=1000)"]
    end

    style V3 fill:#4a6,stroke:#fff,color:#fff
    style V5 fill:#4a6,stroke:#fff,color:#fff
    style V8 fill:#4a6,stroke:#fff,color:#fff
```

**Algorithm for Maximum XOR:**
1. Insert all numbers into a binary trie (MSB to LSB)
2. For each number, greedily traverse the trie choosing the opposite bit at each level to maximize XOR
3. Track the maximum XOR found

**Problems:** LC 421 (Maximum XOR of Two Numbers in an Array)

---

## 6. Trie vs Hash Set

```mermaid
graph TD
    subgraph TrieAdv["Trie"]
        T1["Prefix queries: O(L)"]
        T2["Autocomplete support"]
        T3["Lexicographic ordering"]
        T4["Memory: shared prefixes save space"]
        T5["Wildcard search possible"]
    end

    subgraph HashAdv["Hash Set / Hash Map"]
        H1["Exact match: O(1) average"]
        H2["Simpler implementation"]
        H3["Lower overhead for small datasets"]
        H4["No prefix query support"]
        H5["Better for exact lookups"]
    end

    style TrieAdv fill:#1a3a5c,stroke:#fff,color:#fff
    style HashAdv fill:#5c1a3a,stroke:#fff,color:#fff
```

| Feature | Trie | Hash Set |
|---------|------|----------|
| Exact search | O(L) | O(L) average (hashing takes O(L)) |
| Prefix search | O(L) | O(N*L) - must check all strings |
| Autocomplete | Natural support | Not supported |
| Memory (many shared prefixes) | Efficient | Wasteful (stores full strings) |
| Memory (few shared prefixes) | Overhead per node | More compact |
| Implementation | More complex | Simple |
| Wildcard search | Possible with DFS | Requires regex/iteration |

**Rule of thumb:**
- Need prefix queries, autocomplete, or wildcard search? Use a **Trie**.
- Only need exact match lookups? Use a **Hash Set**.

---

## 7. Which Pattern to Use?

```mermaid
flowchart TD
    START["String/Word Problem?"] -->|Yes| Q1{"Need prefix<br/>operations?"}
    START -->|No| OTHER["Consider other<br/>data structures"]

    Q1 -->|Yes| Q2{"Single word<br/>or multiple?"}
    Q1 -->|No| Q3{"Need exact<br/>match only?"}

    Q2 -->|"Single word<br/>prefix check"| BASIC["Pattern 1:<br/>Basic Trie<br/>(LC 208)"]
    Q2 -->|"Find all words<br/>with prefix"| AUTO["Pattern 2:<br/>Autocomplete<br/>(LC 648, 677, 211)"]

    Q3 -->|Yes| HASH["Use Hash Set<br/>instead"]
    Q3 -->|No| Q4{"Search words<br/>in 2D grid?"}

    Q4 -->|Yes| GRID["Pattern 3:<br/>Word Search + Trie<br/>(LC 212)"]
    Q4 -->|No| Q5{"XOR / bit<br/>manipulation?"}

    Q5 -->|Yes| XOR["Pattern 4:<br/>Binary Trie<br/>(LC 421)"]
    Q5 -->|No| Q6{"Wildcard<br/>matching?"}

    Q6 -->|Yes| WILD["Trie + DFS<br/>(LC 211)"]
    Q6 -->|No| BASIC

    style BASIC fill:#4a6,stroke:#fff,color:#fff
    style AUTO fill:#4a6,stroke:#fff,color:#fff
    style GRID fill:#f96,stroke:#fff,color:#fff
    style XOR fill:#f96,stroke:#fff,color:#fff
    style WILD fill:#4a6,stroke:#fff,color:#fff
    style HASH fill:#888,stroke:#fff,color:#fff
```

---

## 8. Common Mistakes

### Mistake 1: Forgetting the `is_end` Flag
```python
# WRONG: search returns True for any prefix
def search(self, word):
    node = self.root
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    return True  # BUG: "app" returns True even if only "apple" was inserted

# CORRECT: check is_end
def search(self, word):
    node = self.root
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    return node.is_end  # Only True if a word actually ends here
```

### Mistake 2: Not Handling Empty Trie / Empty String
```python
# Always consider edge cases:
# - Searching in an empty trie -> should return False
# - Inserting/searching empty string -> depends on problem constraints
# - The root node itself can have is_end=True (if empty string is inserted)
```

### Mistake 3: Memory Overhead Unawareness
- Each TrieNode creates a new dictionary object, which has overhead in Python
- For large datasets, consider using arrays of size 26 (for lowercase letters) instead of dicts
- For competitive programming, array-based tries are faster

### Mistake 4: Not Pruning in Word Search II (LC 212)
```python
# Without pruning, you re-search for words already found
# After finding a word, remove it from the trie to avoid duplicates
# and improve performance
node.is_end = False  # Unmark to avoid duplicate results
# Optionally remove empty branches (advanced optimization)
```

### Mistake 5: Off-by-One in Binary Trie
```python
# When building a binary trie, always use a fixed bit width
# e.g., 32 bits for integers
for i in range(31, -1, -1):  # MSB to LSB
    bit = (num >> i) & 1
```

---

## 9. Day Schedule

### Day 40: Trie + Final Revision

| Time Block | Task | Problems |
|-----------|------|----------|
| Morning (2h) | Learn Trie concepts, implement basic trie | LC 208, LC 14 (trie variant) |
| Afternoon (2h) | Medium trie problems with patterns | LC 211, LC 648, LC 677 |
| Evening (2h) | Hard trie problems | LC 212, LC 336, LC 421 |
| Night (1h) | Review all 40 days, identify weak areas | Revision |

### Problem Checklist

| # | Problem | Difficulty | Pattern | Status |
|---|---------|-----------|---------|--------|
| 1 | LC 208 - Implement Trie | Easy | Basic Trie | [ ] |
| 2 | LC 14 - Longest Common Prefix (Trie) | Easy | Basic Trie | [ ] |
| 3 | LC 211 - Add and Search Word | Medium | Trie + DFS | [ ] |
| 4 | LC 648 - Replace Words | Medium | Trie Prefix | [ ] |
| 5 | LC 677 - Map Sum Pairs | Medium | Trie Prefix | [ ] |
| 6 | LC 212 - Word Search II | Hard | Trie + Backtracking | [ ] |
| 7 | LC 336 - Palindrome Pairs | Hard | Trie | [ ] |
| 8 | LC 421 - Maximum XOR | Hard | Binary Trie | [ ] |

### Final Revision Strategy

After completing all 40 days:
1. **Revisit weak topics** - Go through problems you struggled with
2. **Pattern recognition drill** - Given a problem description, identify which pattern applies without coding
3. **Speed rounds** - Solve easy/medium problems within time limits (15 min easy, 25 min medium)
4. **Mock interviews** - Pick 2 random problems and solve them as if in an interview
5. **Spaced repetition** - Revisit problems after 1 day, 3 days, 7 days, 14 days
