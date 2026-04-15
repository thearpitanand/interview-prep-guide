"""
Problem: Kth Largest Element in Array (LC 215) | Smart-DSA Day 29 | Medium
Pattern: Heap / Top-K
Time target: 20 minutes

Find the kth largest element in an unsorted array.
Note: it is the kth largest in sorted order, not the kth distinct element.

Example 1:
  Input: nums = [3, 2, 1, 5, 6, 4], k = 2
  Output: 5

Example 2:
  Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
  Output: 4

Constraints:
  - 1 <= k <= nums.length <= 10^5
  - -10^4 <= nums[i] <= 10^4

Hint (⚠ read only after time budget is blown):
  Maintain a min-heap of size k. When the heap exceeds k elements, pop the
  smallest. After processing all elements, the heap root is the kth largest.
"""
import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    pass


if __name__ == "__main__":
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest([1], 1) == 1
    print("All tests passed!")
