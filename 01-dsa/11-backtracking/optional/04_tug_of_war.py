"""
Problem: Tug of War (GFG) | Optional | Hard
Topic: Backtracking

Given a set of n integers, divide into two subsets of sizes n/2 (or n/2 and
n/2+1 if odd) such that the absolute difference of sums is minimized.

Example 1:
  Input: arr = [3, 4, 5, -3, 100, 1, 89, 54, 23, 20]
  Output: min difference

Constraints:
  - 1 <= n <= 20

Hint: Backtrack: try including each element in subset1 (of size n/2).
Pattern: Backtracking
"""


def tug_of_war(arr: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert tug_of_war([3, 4, 5, -3, 100, 1, 89, 54, 23, 20]) == 0  # or some small value
    assert tug_of_war([1, 2, 3]) == 0  # [3] vs [1,2]
    print("All tests passed!")
