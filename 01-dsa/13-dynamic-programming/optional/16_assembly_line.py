"""
Problem: Assembly Line Scheduling (GFG) | Optional | Medium
Topic: Dynamic Programming

Given two assembly lines with processing times and transfer costs, find the
minimum time to assemble a product.

Example 1:
  Input: a = [[4,5,3,2],[2,10,1,4]], t = [[0,7,4,5],[0,9,2,8]], e = [10,12], x = [18,7]
  Output: 35

Constraints:
  - 1 <= n <= 10^4

Hint: dp1[i] = min time to reach station i on line 1. dp1[i] = min(dp1[i-1]+a1[i], dp2[i-1]+t2[i]+a1[i]).
Pattern: DP
"""


def assembly_line(a: list[list[int]], t: list[list[int]], e: list[int], x: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    a = [[4,5,3,2],[2,10,1,4]]
    t = [[0,7,4,5],[0,9,2,8]]
    assert assembly_line(a, t, [10,12], [18,7]) == 35
    print("All tests passed!")
