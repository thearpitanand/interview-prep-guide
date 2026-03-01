"""
Problem: Friends Pairing Problem (GFG) | Optional | Easy
Topic: Dynamic Programming

Given n friends, each can remain single or be paired. Count total ways.

Example 1:
  Input: n = 3
  Output: 4  # {1,2,3}, {1,(2,3)}, {2,(1,3)}, {3,(1,2)}

Constraints:
  - 1 <= n <= 10^4

Hint: f(n) = f(n-1) + (n-1)*f(n-2). Either nth person stays single or pairs with one of n-1 others.
Pattern: DP
"""


def friends_pairing(n: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert friends_pairing(3) == 4
    assert friends_pairing(1) == 1
    assert friends_pairing(4) == 10
    print("All tests passed!")
