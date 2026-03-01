"""
Problem: Find Pair with Given Difference (LC 532) | Optional | Easy
Topic: Searching and Sorting

Given an unsorted array and a number k, find if there exists a pair with difference k.

Example 1:
  Input: arr = [5, 20, 3, 2, 50, 80], k = 78
  Output: True  # (2, 80)

Constraints:
  - 1 <= n <= 10^5

Hint: Sort + two pointers, or use a hash set.
Pattern: Two Pointers / Hashing
"""


def pair_with_diff(arr: list[int], k: int) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert pair_with_diff([5, 20, 3, 2, 50, 80], 78) == True
    assert pair_with_diff([90, 70, 20, 80, 50], 45) == False
    print("All tests passed!")
