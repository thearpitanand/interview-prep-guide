"""
Problem: Kth Largest Sum Contiguous Subarrays (GFG) | Optional | Medium
Topic: Heap

Given an array, find the kth largest sum among all contiguous subarrays.

Example 1:
  Input: arr = [20, -5, -1], k = 3
  Output: 15  # sums: 20, 15, 14, -5, -6, -1 → 3rd largest = 14

Constraints:
  - 1 <= n <= 10^3
  - 1 <= k <= n*(n+1)/2

Hint: Generate all subarray sums, use min-heap of size k.
Pattern: Min-Heap
"""


def kth_largest_sum(arr: list[int], k: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert kth_largest_sum([20, -5, -1], 3) == 14
    assert kth_largest_sum([10, -10, 20, -40], 6) == -10
    print("All tests passed!")
