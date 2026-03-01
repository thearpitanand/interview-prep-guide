"""
Course Schedule (LC 207)

Day: 34 | Difficulty: Medium | Pattern: Topological Sort / Cycle Detection

There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where
prerequisites[i] = [ai, bi] indicates that you must take course bi before
course ai.

Return true if you can finish all courses, otherwise return false.

Examples:
    Input: numCourses=2, prerequisites=[[1,0]]
    Output: True
    Explanation: Take course 0, then course 1.

    Input: numCourses=2, prerequisites=[[1,0],[0,1]]
    Output: False
    Explanation: Circular dependency - can't finish both.

Constraints:
    - 1 <= numCourses <= 2000
    - 0 <= prerequisites.length <= 5000
    - prerequisites[i].length == 2
    - 0 <= ai, bi < numCourses
    - All pairs prerequisites[i] are unique

Hint:
    This is a cycle detection problem on a directed graph. If the prerequisite
    graph has a cycle, you cannot finish all courses. Use topological sort
    (Kahn's algorithm) -- if all nodes are processed, there's no cycle.

Pattern: Topological Sort / Cycle Detection - build a directed graph from
prerequisites and check if a valid topological ordering exists (no cycles).
"""

from collections import defaultdict, deque
from typing import List


def can_finish_bfs(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """Kahn's algorithm (BFS) - check if topological sort is possible."""
    pass


def can_finish_dfs(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """DFS coloring approach - detect cycle in directed graph."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Simple prerequisite chain
    result = can_finish_bfs(2, [[1, 0]])
    assert result == True, f"Expected True, got {result}"

    # Test 2: Circular dependency
    result = can_finish_bfs(2, [[1, 0], [0, 1]])
    assert result == False, f"Expected False, got {result}"

    # Test 3: No prerequisites
    result = can_finish_bfs(3, [])
    assert result == True, f"Expected True, got {result}"

    # Test 4: Diamond dependency (no cycle)
    result = can_finish_bfs(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert result == True, f"Expected True, got {result}"

    # Test 5: DFS approach
    result = can_finish_dfs(2, [[1, 0]])
    assert result == True, f"Expected True, got {result}"

    # Test 6: DFS - circular dependency
    result = can_finish_dfs(2, [[1, 0], [0, 1]])
    assert result == False, f"Expected False, got {result}"

    # Test 7: Single course
    result = can_finish_bfs(1, [])
    assert result == True, f"Expected True, got {result}"

    print("All tests passed!")
