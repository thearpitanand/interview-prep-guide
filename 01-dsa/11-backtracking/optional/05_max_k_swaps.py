"""
Problem: Max Number by K Swaps (GFG) | Optional | Hard
Topic: Backtracking

Given a number string and K, find the maximum number obtainable by performing
at most K swaps of digits.

Example 1:
  Input: s = "7599", k = 2
  Output: "9975"

Constraints:
  - 1 <= len(s) <= 30
  - 1 <= k <= 10

Hint: Backtrack: for each position, try swapping with all larger digits to its right.
Pattern: Backtracking
"""


def max_by_k_swaps(s: str, k: int) -> str:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_by_k_swaps("7599", 2) == "9975"
    assert max_by_k_swaps("1234567", 4) == "7654321"
    assert max_by_k_swaps("129814999", 4) == "999984211"
    print("All tests passed!")
