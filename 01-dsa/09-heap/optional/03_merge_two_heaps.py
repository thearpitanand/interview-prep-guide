"""
Problem: Merge 2 Binary Max Heaps (GFG) | Optional | Medium
Topic: Heap

Given two max heaps, merge them into a single max heap.

Example 1:
  Input: heap1 = [10, 5, 6, 2], heap2 = [12, 7, 9]
  Output: a valid max heap containing all elements

Constraints:
  - 1 <= n, m <= 10^5

Hint: Concatenate arrays, then heapify the combined array.
Pattern: Heapify
"""


def merge_heaps(h1: list[int], h2: list[int]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = merge_heaps([10, 5, 6, 2], [12, 7, 9])
    assert len(result) == 7
    assert result[0] == max(result)  # max-heap property at root
    print("All tests passed!")
