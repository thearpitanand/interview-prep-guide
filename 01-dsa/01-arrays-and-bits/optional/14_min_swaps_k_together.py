"""
Problem: Min Swaps to Bring Elements <= K Together (GFG) | Optional | Medium
Topic: Arrays

Given an array and a number K, find the minimum number of swaps required to
bring all elements <= K together.

Example 1:
  Input: arr = [2, 1, 5, 6, 3], k = 3
  Output: 1  # swap 5 and 3 -> [2, 1, 3, 6, 5]

Constraints:
  - 1 <= n <= 10^5

Hint: Count elements <= K. Use sliding window of that size, find window with max such elements.
Pattern: Sliding Window
"""


def min_swaps_k_together(arr: list[int], k: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert min_swaps_k_together([2, 1, 5, 6, 3], 3) == 1
    assert min_swaps_k_together([2, 7, 9, 5, 8, 7, 4], 5) == 2
    print("All tests passed!")
