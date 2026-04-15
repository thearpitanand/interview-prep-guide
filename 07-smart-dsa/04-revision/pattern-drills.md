# Pattern-Recognition Drills

Four blind quizzes. One at the end of each of Weeks 2, 4, 6, and 8.

**How to take a drill:**

1. Set a timer for 15 minutes (90 seconds per problem × 10 problems).
2. Read each problem statement once. Write down: (a) the pattern name, and (b) a 2-sentence plan — one sentence for the approach, one for the key data structure or invariant.
3. No coding. No looking at notes or pattern guides.
4. After 15 minutes, stop. Check the answer key below the delimiter.
5. Score yourself: 1 point per correct pattern name. Partial credit for the plan is your call.
6. **Score ≥ 7/10:** pass. Move to the next week.
7. **Score < 7/10:** re-read `../01-method/pattern-recognition.md` before starting Week N+1. Do not skip this — a < 7 score means the pattern-matching reflex is not yet automatic.

These problems are **outside the 60-day schedule** — they test recognition, not memory of a problem you have already solved.

---

## Drill 1 — End of Week 2

*Patterns covered so far: Arrays / Hashing, Two Pointers, Sliding Window, Binary Search*

**Start timer before reading problem 1.**

---

**Problem 1.**
Given an array of integers and a target sum, return `true` if any two distinct elements sum to the target. The array is unsorted and may contain duplicates.

**Problem 2.**
Given a sorted array of integers, find the starting and ending index of a given target value. If not found, return `[-1, -1]`. Your solution must run in O(log n) time.

**Problem 3.**
Given a string, find the length of the longest substring that contains at most two distinct characters.

**Problem 4.**
Given a sorted array of integers where every element appears twice except for one, find the single non-duplicate element. Time complexity must be O(log n).

**Problem 5.**
Given an array of positive integers representing the heights of people in a line, count the number of pairs of people where the shorter person can see the taller person (the taller person must be to the right and no one taller stands between them). *(Focus on pattern identification, not the full algorithm.)*

**Problem 6.**
You are given a 2D matrix of 0s and 1s sorted row-wise and column-wise. Find whether a target value exists in the matrix. Each row is sorted left to right and the first integer of each row is greater than the last integer of the previous row.

**Problem 7.**
Given a string of lowercase letters, find the minimum number of characters you need to delete so that no two adjacent characters are the same. *(Identify pattern and key observation only.)*

**Problem 8.**
Given an array of integers, find the maximum sum of any contiguous subarray of length exactly `k`.

**Problem 9.**
Given a sorted array, determine if there exist three integers a, b, c in the array such that a + b + c = 0. Return all unique triplets.

**Problem 10.**
You have a list of words and need to find all words that are anagrams of each other, grouped together. The input list can be large.

---

--- ANSWERS ---

| # | Pattern | 2-Sentence Plan |
|---|---------|----------------|
| 1 | Arrays / Hashing | Use a hash set to store seen values. For each element x, check if `target - x` is in the set before inserting x. |
| 2 | Binary Search | Run two separate binary searches: one to find the leftmost index, one to find the rightmost. Use the standard binary search template with the condition adjusted to continue right (or left) when the target is found. |
| 3 | Sliding Window (variable window) | Expand the right pointer and track distinct characters in a hash map. When distinct count exceeds 2, shrink from the left until it is valid again; track the maximum window length throughout. |
| 4 | Binary Search | The invariant is that the single element is always on the side where the pair pattern breaks. Compare `mid` with `mid+1`; if they match, the single is to the right, otherwise it is to the left or at mid. |
| 5 | Monotonic Stack | A decreasing monotonic stack tracks candidates who can be seen from a given position. Pop and count when a taller person is encountered; this is a classic "next greater element" variant. |
| 6 | Binary Search (on 2D matrix treated as flat array) | Treat the m×n matrix as a sorted array of m×n elements. Map a flat index `mid` to row `mid // n` and column `mid % n` and apply standard binary search. |
| 7 | Two Pointers / Greedy scan | Scan with a pointer and compare each character to its neighbor. Every time two adjacent characters match, increment a delete counter and skip past the duplicate (greedy: remove one of each matching pair). |
| 8 | Sliding Window (fixed window) | Use a fixed-size window of length k. Compute the sum of the first k elements, then slide right: add the new element and subtract the element leaving the window. Track the maximum. |
| 9 | Two Pointers | Sort the array. Fix each element with an outer loop, then use a two-pointer scan on the remaining subarray to find pairs that sum to the negation of the fixed element. Skip duplicates at both levels. |
| 10 | Arrays / Hashing | Use a hash map where the key is a canonical form of each word (sorted characters as a tuple or string). Append each word to the list at its canonical key; return all value lists. |

---
---

## Drill 2 — End of Week 4

*Adds: Stack, Monotonic Stack, Linked List, Trees DFS / BFS, BST*

**Start timer before reading problem 1.**

---

**Problem 1.**
Given a binary tree, find the path from root to a leaf that has the maximum sum. Return the sum.

**Problem 2.**
Given a string with brackets `()[]{}`, find the minimum number of bracket removals needed to make the string valid.

**Problem 3.**
Given the head of a singly linked list, return the node where a cycle begins. If there is no cycle, return null.

**Problem 4.**
Given a binary search tree and a target value, return the value in the BST that is closest to the target.

**Problem 5.**
Given a binary tree, return the zigzag level order traversal: left to right for level 1, right to left for level 2, alternating.

**Problem 6.**
Given an array representing daily stock prices, find the length of the longest period where prices are strictly increasing.

**Problem 7.**
Given a linked list and a value k, reverse only the nodes of the list from position k to the end. Leave nodes before position k unchanged.

**Problem 8.**
Given a BST, find all pairs of nodes whose values sum to a target k.

**Problem 9.**
Given a binary tree, count the number of paths (not necessarily from root to leaf) where the values along the path sum to a target. Paths must go downward only.

**Problem 10.**
Given an array of integers, for each element find the index of the nearest smaller element to the left. Return -1 if none exists.

---

--- ANSWERS ---

| # | Pattern | 2-Sentence Plan |
|---|---------|----------------|
| 1 | Tree DFS (post-order) | Recursively compute the max-sum path for each subtree, returning the running total to the parent. At each node, the answer is node value + max of left and right child results; the overall max is updated at each call. |
| 2 | Stack | Use a stack to track unmatched open brackets. For each close bracket, pop if the top matches; otherwise push the close bracket as unmatched. The answer is the total size of the remaining stack. |
| 3 | Linked List — Fast / Slow Pointers (Floyd's cycle detection) | Run a slow pointer (one step) and a fast pointer (two steps) until they meet; this confirms a cycle. Reset one pointer to head and advance both one step at a time; the node where they meet again is the cycle entry. |
| 4 | BST Traversal / Binary Search | Exploit BST ordering: at each node compare the absolute difference with the current best. Go left if target < node value, right if target > node value, exactly like binary search. No full traversal needed. |
| 5 | Tree BFS (level order with alternating direction) | BFS level by level using a queue; track a direction flag. Append each level's nodes to a list normally or reversed based on the flag, then toggle the flag after each level. |
| 6 | Arrays — Linear Scan / Two Pointers | Scan with a counter that resets when the strictly-increasing condition breaks. Track the maximum counter seen. This is a sliding window with a trivial shrink condition. |
| 7 | Linked List — Pointer Manipulation | Walk to node k-1 to find the tail of the unchanged prefix, then reverse the rest of the list in place. Reconnect the prefix tail to the new head of the reversed portion. |
| 8 | BST + Hash Set (or Two Pointers on in-order array) | An in-order traversal of a BST produces a sorted array. Run two-pointer sum on that array, or traverse in-order and use a hash set to check for the complement of each value. |
| 9 | Tree DFS + Prefix Sum Hash Map | Track running path sums from root to current node and store counts in a hash map. At each node, check if `current_sum - target` exists in the map; if so, those many paths end here. This is the subarray-sum-equals-k idea applied to a tree. |
| 10 | Monotonic Stack (nearest smaller to left) | Maintain a decreasing stack. For each element, pop all stack elements ≥ the current element; the top after popping is the nearest smaller to the left (or -1 if the stack is empty). Push the current element and record the result. |

---
---

## Drill 3 — End of Week 6

*Adds: Heap / Top-K, Backtracking, Graphs, 1D DP*

**Start timer before reading problem 1.**

---

**Problem 1.**
Given a list of integers, find the k numbers closest to a given value x. Return them sorted.

**Problem 2.**
Given an m×n grid of 0s and 1s, count the number of distinct regions where 1s are connected (4-directional). Each region is a group of connected 1s.

**Problem 3.**
Given a set of distinct positive integers, find all subsets that sum to a target value.

**Problem 4.**
Given a list of courses where `courses[i] = [a, b]` means course a must be taken before course b, determine a valid order to take all courses. If impossible, return an empty array.

**Problem 5.**
Given an array of non-negative integers, find the minimum number of jumps to reach the last index from the first. Each element represents the maximum jump length from that position.

**Problem 6.**
Given a string, find the number of distinct palindromic substrings.

**Problem 7.**
You have `n` ropes of different lengths. At each step you can connect two ropes; the cost is the sum of their lengths. Find the minimum total cost to connect all ropes into one.

**Problem 8.**
Given a graph where edges have weights, find the minimum cost to connect all nodes (minimum spanning tree).

**Problem 9.**
Given a list of words, find all words that can be formed by starting from any cell in a board of characters and moving to adjacent (4-directional) cells, never reusing the same cell.

**Problem 10.**
You are given weights and values of items and a knapsack of capacity W. Each item can be picked at most once. Maximize the value you can carry.

---

--- ANSWERS ---

| # | Pattern | 2-Sentence Plan |
|---|---------|----------------|
| 1 | Heap / Top-K | Use a max-heap of size k keyed on absolute difference from x; iterate through all elements, pushing to the heap and popping when size exceeds k. The k remaining elements are the answer. Alternatively, binary search for x and expand outward with two pointers. |
| 2 | Graph DFS / BFS on grid | Iterate every cell; when an unvisited 1 is found, increment the region count and flood-fill (DFS or BFS) to mark all connected 1s as visited. The final count is the number of distinct regions. |
| 3 | Backtracking | Sort the array then recurse: at each step either include the current element (add to path, recurse with reduced target) or skip it. Prune branches where remaining elements cannot reach the target. |
| 4 | Topological Sort (Kahn's BFS algorithm) | Build an adjacency list and in-degree array. Start BFS from all nodes with in-degree 0; as each node is processed, decrement its neighbors' in-degrees and enqueue any that reach 0. If the output order has n nodes, a valid order exists. |
| 5 | Greedy (or 1D DP) | Track the current reachable boundary and the farthest point reachable from any position in the current window. Each time you reach the boundary, increment the jump count and extend the boundary to the farthest point seen. |
| 6 | Dynamic Programming — Expand Around Center (or 2D DP) | For each character (and each pair of adjacent characters), expand outward as long as the substring is a palindrome, counting each distinct palindromic substring. Use a set to avoid counting duplicates. |
| 7 | Heap / Greedy (minimum cost to merge) | Use a min-heap. Repeatedly extract the two smallest ropes, add their sum as the cost, and push the merged rope back. The total accumulated cost is minimized because shorter ropes are merged first. |
| 8 | Graph — Minimum Spanning Tree (Prim's or Kruskal's) | Kruskal: sort all edges by weight and greedily add each edge if it does not form a cycle (use Union-Find to check). Prim: grow a tree from any starting node, always adding the cheapest edge that connects a new node. |
| 9 | Backtracking on Grid + Trie | Build a Trie from the word list for fast prefix checking. At each cell, DFS through the grid: if the current path is a Trie prefix, continue; if it is a full word, record it. Mark cells visited and unmark on backtrack. |
| 10 | 0/1 Knapsack DP | Build a 2D dp table where `dp[i][w]` = max value using the first i items with capacity w. For each item, either skip it (`dp[i-1][w]`) or include it if it fits (`dp[i-1][w-weight[i]] + value[i]`); take the max. Can be space-optimized to 1D by iterating capacity in reverse. |

---
---

## Drill 4 — End of Week 8

*Full mix — any pattern from Weeks 1–8*

**Start timer before reading problem 1.**

---

**Problem 1.**
Given an array of integers, find the length of the longest subarray where the absolute difference between any two elements is at most 1.

**Problem 2.**
Given a matrix of integers, find the length of the longest increasing path starting from any cell. You can move in four directions and cannot revisit a cell.

**Problem 3.**
Given a string and a dictionary of words, return all possible sentences formed by inserting spaces into the string so that each word is in the dictionary.

**Problem 4.**
Given a list of intervals, find the minimum number of intervals to remove so that the rest are non-overlapping.

**Problem 5.**
Given a directed graph, determine if there is a path between two given nodes.

**Problem 6.**
Given an integer array, find the number of triplets `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`.

**Problem 7.**
Given a binary tree, find the maximum width of the tree. Width is the number of nodes between the leftmost and rightmost nodes at each level, including nulls in between.

**Problem 8.**
Given a stream of integers, design a data structure that supports inserting a number and finding the median of all inserted numbers in O(log n) per operation.

**Problem 9.**
Given an m×n grid where each cell is either land or water, find the cell that minimizes the maximum Manhattan distance to any land cell.

**Problem 10.**
Given an array of distinct integers, return all possible permutations in any order.

---

--- ANSWERS ---

| # | Pattern | 2-Sentence Plan |
|---|---------|----------------|
| 1 | Sliding Window + Hash Map | Use a sliding window and a frequency map to count element occurrences. When an element outside the allowed range enters (absolute difference > 1 from any current element), shrink the window from the left until valid; track max length. |
| 2 | DFS + Memoization (DP on DAG) | At each cell, DFS in all four directions and return 1 + max of valid (increasing) neighbors. Memoize results per cell so each cell is computed at most once; the answer is the global maximum. |
| 3 | Backtracking + Hash Set (or DP) | Use backtracking: at each position in the string, try all prefixes that are valid dictionary words, recurse on the suffix, and collect full solutions when the suffix is empty. Memoize suffix → sentences to avoid recomputation. |
| 4 | Greedy — Interval Scheduling (minimum removals = n minus max non-overlapping) | Sort intervals by end time. Greedily pick the interval with the earliest end time that does not overlap the previous; count how many you can keep. Removals = total intervals − kept intervals. |
| 5 | Graph BFS or DFS (reachability) | Standard BFS or DFS from the source node, marking visited nodes. If the destination is reached, return true; if the traversal exhausts without reaching it, return false. |
| 6 | DP or Binary Search (LIS variant / count increasing triplets) | For each index j, count elements smaller than `nums[j]` to its left (call it `left[j]`) and elements larger than `nums[j]` to its right (call it `right[j]`). The answer is the sum of `left[j] * right[j]` over all j. Each `left` and `right` array can be computed with a BIT or sorted list. |
| 7 | Tree BFS with position indexing | BFS level by level, labeling each node with a positional index (left child = 2*parent, right child = 2*parent+1). Width of each level = last index − first index + 1. Track maximum width across all levels. |
| 8 | Heap — Two Heaps (Median from Data Stream) | Maintain a max-heap for the lower half and a min-heap for the upper half of the stream. After each insert, rebalance so the heaps differ in size by at most 1. The median is the top of the larger heap (or average of both tops). |
| 9 | Graphs — Multi-Source BFS | Add all land cells to the BFS queue simultaneously as sources. BFS outward, marking each water cell with the distance from the nearest land cell. The last cell reached has the maximum distance; return that distance (or -1 if no water or no land). |
| 10 | Backtracking | Use a used-flag array or swap-based approach. At each recursion depth, try placing each unused element at the current position, recurse, then undo the choice. Base case: when depth equals array length, record the permutation. |
