"""
Problem: Celebrity Problem (LC 277 / GFG) | Day 21 | Medium
Topic: Stacks and Queues

In a party of N people, a celebrity is someone who is known by everyone but
doesn't know anyone. Given a matrix M where M[i][j] = 1 means i knows j,
find the celebrity. Return -1 if none.

Example 1:
  Input: M = [[0,1,0],[0,0,0],[0,1,0]]
  Output: 1  # person 1 is known by 0 and 2, knows nobody

Constraints:
  - 1 <= n <= 10^3

Hint: Use stack: push all people, pop two, eliminate one who knows the other. Verify final candidate.
Pattern: Stack Elimination
"""


def find_celebrity(M: list[list[int]], n: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert find_celebrity([[0,1,0],[0,0,0],[0,1,0]], 3) == 1
    assert find_celebrity([[0,1],[1,0]], 2) == -1
    assert find_celebrity([[0,0,1,0],[0,0,1,0],[0,0,0,0],[0,0,1,0]], 4) == 2
    print("All tests passed!")
