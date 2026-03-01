"""
Problem: Search in Array Where Adjacent Differ by K (GFG) | Optional | Easy
Topic: Searching and Sorting

Given an array where adjacent elements differ by at most k, find target element.

Example 1:
  Input: arr = [2, 4, 5, 7, 7, 6], k = 2, target = 6
  Output: 5

Constraints:
  - Adjacent elements differ by at most k

Hint: Jump by max(1, abs(arr[i]-target)//k) — since adjacent differ by at most k.
Pattern: Jump Search
"""


def search_adjacent_k(arr: list[int], k: int, target: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert search_adjacent_k([2, 4, 5, 7, 7, 6], 2, 6) == 5
    assert search_adjacent_k([20, 40, 50, 70, 70, 60], 20, 60) == 5
    print("All tests passed!")
