"""
Problem: Top K Frequent Elements (LC 347) | Smart-DSA Day 2 | Medium
Pattern: Arrays & Hashing
Time target: 25 minutes

Given an integer array nums and integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
  Input: nums = [1, 1, 1, 2, 2, 3], k = 2
  Output: [1, 2]

Example 2:
  Input: nums = [1], k = 1
  Output: [1]

Constraints:
  - 1 <= nums.length <= 10^5
  - k is in the range [1, number of unique elements].
  - The answer is guaranteed to be unique.

Hint (⚠ read only after time budget is blown):
  Count frequencies, then use a min-heap of size k or bucket sort by frequency.
  Bucket sort gives O(n) — buckets indexed by frequency 1..n.
"""


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    pass


if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert sorted(top_k_frequent([4, 4, 4, 6, 6, 7], 2)) == [4, 6]
    print("All tests passed!")
