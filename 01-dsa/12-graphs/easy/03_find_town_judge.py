"""
Find the Town Judge (LC 997)

Day: 33 | Difficulty: Easy | Pattern: Graph Property (In-degree / Out-degree)

In a town, there are n people labeled from 1 to n. There is a rumor that one
of these people is secretly the town judge. If the town judge exists:
  1. The town judge trusts nobody.
  2. Everybody (except the judge) trusts the judge.
  3. There is exactly one person that satisfies both conditions.

You are given an array trust where trust[i] = [ai, bi] means person ai trusts
person bi. Return the label of the town judge if they exist, otherwise return -1.

Examples:
    Input: n=2, trust=[[1,2]]
    Output: 2

    Input: n=3, trust=[[1,3],[2,3]]
    Output: 3

    Input: n=3, trust=[[1,3],[2,3],[3,1]]
    Output: -1

Constraints:
    - 1 <= n <= 1000
    - 0 <= trust.length <= 10^4
    - trust[i].length == 2
    - All pairs trust[i] are unique
    - ai != bi
    - 1 <= ai, bi <= n

Hint:
    The judge has in-degree n-1 (everyone trusts them) and out-degree 0 (they
    trust nobody). Track a net trust score: +1 for being trusted, -1 for
    trusting someone. The judge will have score n-1.

Pattern: Graph degree counting - model trust as directed edges and count
in-degree minus out-degree for each person.
"""

from typing import List


def find_judge(n: int, trust: List[List[int]]) -> int:
    """Find the town judge using in-degree and out-degree counting."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Simple case with 2 people
    result = find_judge(2, [[1, 2]])
    assert result == 2, f"Expected 2, got {result}"

    # Test 2: Judge is person 3
    result = find_judge(3, [[1, 3], [2, 3]])
    assert result == 3, f"Expected 3, got {result}"

    # Test 3: No judge exists (judge trusts someone)
    result = find_judge(3, [[1, 3], [2, 3], [3, 1]])
    assert result == -1, f"Expected -1, got {result}"

    # Test 4: Single person (they are the judge)
    result = find_judge(1, [])
    assert result == 1, f"Expected 1, got {result}"

    # Test 5: Everyone trusts each other, no judge
    result = find_judge(3, [[1, 2], [2, 3], [3, 1]])
    assert result == -1, f"Expected -1, got {result}"

    # Test 6: Multiple trust relationships
    result = find_judge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])
    assert result == 3, f"Expected 3, got {result}"

    print("All tests passed!")
