"""
Network Delay Time (LC 743)

Day: 34 | Difficulty: Medium | Pattern: Dijkstra's Algorithm

You are given a network of n nodes, labeled from 1 to n. You are given times,
a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is
the source, vi is the target, and wi is the time it takes for a signal to
travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes
for all n nodes to receive the signal. If it's impossible for all nodes to
receive the signal, return -1.

Examples:
    Input: times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2
    Output: 2
    Explanation: Signal from 2 reaches 1 in 1, reaches 3 in 1, reaches 4 in 2.

    Input: times=[[1,2,1]], n=2, k=2
    Output: -1
    Explanation: Node 1 can never be reached from node 2.

    Input: times=[[1,2,1]], n=2, k=1
    Output: 1

Constraints:
    - 1 <= k <= n <= 100
    - 1 <= times.length <= 6000
    - times[i].length == 3
    - 1 <= ui, vi <= n
    - ui != vi
    - 0 <= wi <= 100
    - All pairs (ui, vi) are unique

Hint:
    This is a classic single-source shortest path problem. Use Dijkstra's
    algorithm from node k. The answer is the maximum distance to any node.
    If any node is unreachable (distance = inf), return -1.

Pattern: Dijkstra's shortest path - find shortest distances from source to
all nodes, then return the maximum distance (the bottleneck).
"""

import heapq
from collections import defaultdict
from typing import List


def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    """Dijkstra's algorithm to find when all nodes receive the signal."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Standard case
    result = network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
    assert result == 2, f"Expected 2, got {result}"

    # Test 2: Unreachable node
    result = network_delay_time([[1, 2, 1]], 2, 2)
    assert result == -1, f"Expected -1, got {result}"

    # Test 3: Direct connection
    result = network_delay_time([[1, 2, 1]], 2, 1)
    assert result == 1, f"Expected 1, got {result}"

    # Test 4: Single node
    result = network_delay_time([], 1, 1)
    assert result == 0, f"Expected 0, got {result}"

    # Test 5: Multiple paths, shortest wins
    result = network_delay_time([[1, 2, 10], [1, 3, 1], [3, 2, 1]], 3, 1)
    assert result == 2, f"Expected 2, got {result}"

    # Test 6: All nodes reachable with different distances
    result = network_delay_time(
        [[1, 2, 1], [1, 3, 4], [2, 3, 2]], 3, 1
    )
    assert result == 3, f"Expected 3, got {result}"

    print("All tests passed!")
