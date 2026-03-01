"""
Last Stone Weight

Day: 28
Difficulty: Easy
Topic: Max Heap
Link: https://leetcode.com/problems/last-stone-weight/
Pattern: Max Heap (negate values for Python heapq)

Description:
    You are given an array of integers 'stones' where stones[i] is the weight
    of the i-th stone.

    We are playing a game with the stones. On each turn, we choose the two
    heaviest stones and smash them together. Suppose the heaviest two stones
    have weights x and y with x <= y. The result of this smash is:
        - If x == y, both stones are destroyed.
        - If x != y, the stone of weight x is destroyed, and the stone of
          weight y has new weight y - x.

    At the end of the game, there is at most one stone left. Return the weight
    of the last remaining stone. If there are no stones left, return 0.

Examples:
    Input: stones = [2, 7, 4, 1, 8, 1]
    Output: 1
    Explanation:
        Smash 8 and 7 -> 1, stones = [2, 4, 1, 1, 1]
        Smash 4 and 2 -> 2, stones = [1, 1, 2, 1]
        Smash 2 and 1 -> 1, stones = [1, 1, 1]
        Smash 1 and 1 -> 0, stones = [1]
        Return 1

    Input: stones = [1]
    Output: 1

Constraints:
    - 1 <= stones.length <= 30
    - 1 <= stones[i] <= 1000

Hint:
    Python heapq is a min-heap. To simulate a max-heap, negate all values
    before pushing and negate again when popping.

Pattern:
    Max Heap - Repeatedly extract two largest, push back difference.
    Use negative values with Python's heapq to simulate max-heap.
"""

import heapq
from typing import List


def last_stone_weight(stones: List[int]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    # Test 1: General case
    assert last_stone_weight([2, 7, 4, 1, 8, 1]) == 1, "Test 1 Failed"

    # Test 2: Single stone
    assert last_stone_weight([1]) == 1, "Test 2 Failed"

    # Test 3: Two equal stones
    assert last_stone_weight([3, 3]) == 0, "Test 3 Failed"

    # Test 4: Two different stones
    assert last_stone_weight([3, 7]) == 4, "Test 4 Failed"

    # Test 5: All same stones (even count)
    assert last_stone_weight([5, 5, 5, 5]) == 0, "Test 5 Failed"

    # Test 6: All same stones (odd count)
    assert last_stone_weight([5, 5, 5]) == 5, "Test 6 Failed"

    print("All test cases passed!")
