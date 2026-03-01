"""
Problem: Max Sum Absolute Difference (GFG) | Optional | Medium
Topic: Greedy

Given an array, find the maximum sum of |arr[i] - arr[i+1]| for a circular
arrangement (rearrange elements to maximize).

Example 1:
  Input: arr = [1, 2, 4, 8]
  Output: 18  # arrange as [1,8,2,4] → |1-8|+|8-2|+|2-4|+|4-1| = 7+6+2+3=18

Constraints:
  - 1 <= n <= 10^5

Hint: Sort, interleave smallest and largest. Or: answer = 2*(sum of larger half - sum of smaller half).
Pattern: Greedy / Sorting
"""


def max_sum_abs_diff(arr: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_sum_abs_diff([1, 2, 4, 8]) == 18
    assert max_sum_abs_diff([1, 2, 3]) == 4
    print("All tests passed!")
