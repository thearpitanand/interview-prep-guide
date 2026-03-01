"""
Problem: K Largest Elements from Array (GFG) | Optional | Easy
Topic: Heap

Return the k largest elements from an unsorted array.

Example 1:
  Input: arr = [1, 23, 12, 9, 30, 2, 50], k = 3
  Output: [50, 30, 23]

Constraints:
  - 1 <= k <= n <= 10^5

Hint: Use min-heap of size k. Push elements, pop if size > k.
Pattern: Min-Heap
"""


def k_largest(arr: list[int], k: int) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert sorted(k_largest([1, 23, 12, 9, 30, 2, 50], 3), reverse=True) == [50, 30, 23]
    assert k_largest([5, 3, 1], 1) == [5]
    print("All tests passed!")
