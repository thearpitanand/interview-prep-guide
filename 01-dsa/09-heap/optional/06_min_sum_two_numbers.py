"""
Problem: Min Sum of Two Numbers from Digits (GFG) | Optional | Medium
Topic: Heap

Given an array of digits, form two numbers using all digits such that their
sum is minimum.

Example 1:
  Input: arr = [6, 8, 4, 5, 2, 3]
  Output: 604  # numbers: 246 + 358 = 604

Constraints:
  - 1 <= n <= 10^5
  - 0 <= arr[i] <= 9

Hint: Sort digits. Distribute alternately to two numbers.
Pattern: Greedy / Sorting
"""


def min_sum_two_numbers(arr: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert min_sum_two_numbers([6, 8, 4, 5, 2, 3]) == 604
    assert min_sum_two_numbers([5, 3, 0, 7, 4]) == 82  # 35 + 47 = 82 or 30 + 47, etc.
    print("All tests passed!")
