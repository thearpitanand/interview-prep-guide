"""
Problem: Kth Smallest from Unsorted Array (GFG) | Optional | Easy
Topic: Heap

Find the kth smallest element in an unsorted array.

Example 1:
  Input: arr = [7, 10, 4, 3, 20, 15], k = 3
  Output: 7

Constraints:
  - 1 <= k <= n <= 10^5

Hint: Use max-heap of size k, or quickselect.
Pattern: Max-Heap / Quickselect
"""


def kth_smallest(arr: list[int], k: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert kth_smallest([7, 10, 4, 3, 20, 15], 3) == 7
    assert kth_smallest([1, 2, 3], 1) == 1
    assert kth_smallest([5], 1) == 5
    print("All tests passed!")
