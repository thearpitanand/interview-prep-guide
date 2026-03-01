"""
Problem: Heap Sort Implementation (GFG) | Day 28 | Medium
Topic: Heap

Implement heap sort algorithm to sort an array in ascending order.

Example 1:
  Input: arr = [12, 11, 13, 5, 6, 7]
  Output: [5, 6, 7, 11, 12, 13]

Constraints:
  - 1 <= n <= 10^5

Hint: Build max-heap, then repeatedly extract max and place at end.
Pattern: Heap Sort
"""


def heap_sort(arr: list[int]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert heap_sort([12, 11, 13, 5, 6, 7]) == [5, 6, 7, 11, 12, 13]
    assert heap_sort([3, 1, 2]) == [1, 2, 3]
    assert heap_sort([1]) == [1]
    print("All tests passed!")
