"""
Course Schedule II (LC 210)

Day: 34 | Difficulty: Medium | Pattern: Topological Sort

There are a total of numCourses courses you have to take, labeled from 0 to
numCourses - 1. You are given an array prerequisites where
prerequisites[i] = [ai, bi] indicates that you must take course bi before
course ai.

Return the ordering of courses you should take to finish all courses. If there
are multiple valid answers, return any of them. If it is impossible to finish
all courses, return an empty array.

Examples:
    Input: numCourses=2, prerequisites=[[1,0]]
    Output: [0,1]

    Input: numCourses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]]
    Output: [0,1,2,3] or [0,2,1,3]

    Input: numCourses=1, prerequisites=[]
    Output: [0]

Constraints:
    - 1 <= numCourses <= 2000
    - 0 <= prerequisites.length <= numCourses * (numCourses - 1)
    - prerequisites[i].length == 2
    - 0 <= ai, bi < numCourses
    - ai != bi
    - All pairs [ai, bi] are distinct

Hint:
    Use Kahn's algorithm (BFS topological sort). Start with courses that have
    no prerequisites (in-degree 0). Process them, reduce in-degrees of their
    dependents. If all courses are in the result, return it; otherwise return [].

Pattern: Topological Sort - same as Course Schedule I but actually return
the ordering instead of just checking if it exists.
"""

from collections import defaultdict, deque
from typing import List


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """Kahn's algorithm - return topological ordering of courses."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Simple prerequisite
    result = find_order(2, [[1, 0]])
    assert result == [0, 1], f"Expected [0, 1], got {result}"

    # Test 2: Diamond dependency (multiple valid orders)
    result = find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    # Valid: [0,1,2,3] or [0,2,1,3]
    assert len(result) == 4, f"Expected 4 courses, got {len(result)}"
    assert result[0] == 0, f"Course 0 should be first"
    assert result[-1] == 3, f"Course 3 should be last"

    # Test 3: No prerequisites
    result = find_order(1, [])
    assert result == [0], f"Expected [0], got {result}"

    # Test 4: Impossible (cycle)
    result = find_order(2, [[1, 0], [0, 1]])
    assert result == [], f"Expected [], got {result}"

    # Test 5: Three independent courses
    result = find_order(3, [])
    assert len(result) == 3, f"Expected 3 courses, got {len(result)}"
    assert set(result) == {0, 1, 2}, f"Expected courses 0,1,2, got {result}"

    # Test 6: Linear chain
    result = find_order(3, [[1, 0], [2, 1]])
    assert result == [0, 1, 2], f"Expected [0, 1, 2], got {result}"

    print("All tests passed!")
