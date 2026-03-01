"""
Problem: Max Length Chain of Pairs (GFG) | Optional | Medium
Topic: Dynamic Programming

Given pairs of (a, b) where a < b, find the longest chain where for
consecutive pairs (c,d) and (e,f), d < e.

Example 1:
  Input: pairs = [(5,24),(39,60),(15,28),(27,40),(50,90)]
  Output: 3  # (5,24) -> (27,40) -> (50,90)

Constraints:
  - 1 <= n <= 10^3

Hint: Sort by second element. Greedy (like activity selection) or DP like LIS.
Pattern: Greedy / DP
"""


def max_chain_pairs(pairs: list[tuple[int, int]]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_chain_pairs([(5,24),(39,60),(15,28),(27,40),(50,90)]) == 3
    assert max_chain_pairs([(1,2),(3,4)]) == 2
    print("All tests passed!")
