"""
Problem: Maximum XOR of Two Numbers in an Array (LC 421) | Day 40 | Hard
Topic: Binary Trie

Given an integer array nums, return the maximum result of nums[i] XOR nums[j],
where 0 <= i <= j < n.

Example 1:
  Input:  [3, 10, 5, 25, 2, 8]
  Output: 28
  Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:
  Input:  [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
  Output: 127

Example 3:
  Input:  [0]
  Output: 0

Constraints:
  - 1 <= nums.length <= 2 * 10^5
  - 0 <= nums[i] <= 2^31 - 1

Hint: Build a binary trie storing each number bit by bit (from MSB to LSB).
      For each number, greedily traverse the trie choosing the opposite bit
      at each level to maximize XOR. Track the maximum XOR value found.
Pattern: Binary Trie (XOR Trie)
"""

from typing import List


class TrieNode:
    def __init__(self):
        # Write your implementation here
        pass


class Solution:
    def find_maximum_xor(self, nums: List[int]) -> int:
        pass


# --- Tests ---
if __name__ == "__main__":
    sol = Solution()

    assert sol.find_maximum_xor([3, 10, 5, 25, 2, 8]) == 28
    assert sol.find_maximum_xor([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]) == 127
    assert sol.find_maximum_xor([0]) == 0
    assert sol.find_maximum_xor([1, 2]) == 3
    assert sol.find_maximum_xor([4, 6, 7]) == 3
    assert sol.find_maximum_xor([8, 10, 2]) == 10
    assert sol.find_maximum_xor([2, 4]) == 6

    print("All tests passed!")
