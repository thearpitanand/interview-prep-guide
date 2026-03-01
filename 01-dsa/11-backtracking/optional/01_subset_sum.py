"""
Problem: Subset Sum Problem (GFG) | Optional | Medium
Topic: Backtracking

Given a set of non-negative integers and a target sum, check if there is a
subset with the given sum.

Example 1:
  Input: arr = [3, 34, 4, 12, 5, 2], target = 9
  Output: True  # subset [4, 5]

Constraints:
  - 1 <= n <= 25
  - 1 <= arr[i] <= 10^5

Hint: Backtrack: include or exclude each element.
Pattern: Backtracking / DP
"""


def subset_sum(arr: list[int], target: int) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert subset_sum([3, 34, 4, 12, 5, 2], 9) == True
    assert subset_sum([3, 34, 4, 12, 5, 2], 30) == False
    assert subset_sum([1, 2, 3], 6) == True
    print("All tests passed!")
