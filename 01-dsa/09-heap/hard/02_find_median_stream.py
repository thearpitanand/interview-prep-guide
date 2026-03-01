"""
Find Median from Data Stream

Day: 28
Difficulty: Hard
Topic: Two Heaps
Link: https://leetcode.com/problems/find-median-from-data-stream/
Pattern: Two Heaps (Max-Heap for lower half + Min-Heap for upper half)

Description:
    The median is the middle value in an ordered integer list. If the size
    of the list is even, there is no middle value, and the median is the
    mean of the two middle values.

    For example:
        - [2, 3, 4] -> median is 3
        - [2, 3] -> median is (2 + 3) / 2 = 2.5

    Implement the MedianFinder class:
        - MedianFinder() initializes the MedianFinder object.
        - void addNum(int num) adds the integer num to the data structure.
        - double findMedian() returns the median of all elements so far.

Examples:
    Input:
        ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
        [[], [1], [2], [], [3], []]
    Output:
        [null, null, null, 1.5, null, 2.0]
    Explanation:
        MedianFinder medianFinder = new MedianFinder()
        medianFinder.addNum(1)    -> [1]
        medianFinder.addNum(2)    -> [1, 2]
        medianFinder.findMedian() -> 1.5  (median of [1, 2])
        medianFinder.addNum(3)    -> [1, 2, 3]
        medianFinder.findMedian() -> 2.0  (median of [1, 2, 3])

Constraints:
    - -10^5 <= num <= 10^5
    - There will be at least one element before calling findMedian.
    - At most 5 * 10^4 calls will be made to addNum and findMedian.

Hint:
    Maintain two heaps:
    - max_heap (negate values): stores the LOWER half of numbers
    - min_heap: stores the UPPER half of numbers

    Invariants:
    1. All elements in max_heap <= all elements in min_heap
    2. len(max_heap) == len(min_heap) or len(max_heap) == len(min_heap) + 1

    addNum: Push to max_heap first, then rebalance.
    findMedian: If odd total -> max_heap root. If even -> average of both roots.

Pattern:
    Two Heaps - Split the stream into two halves. The max-heap holds the
    smaller half, the min-heap holds the larger half. The median is always
    accessible from the roots of the heaps in O(1).
"""

import heapq


class MedianFinder:
    def __init__(self):
        pass

    def add_num(self, num: int) -> None:
        pass

    def find_median(self) -> float:
        pass


# ---- Test Cases ----
if __name__ == "__main__":
    # Test 1: Basic example from problem
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    assert mf.find_median() == 1.5, "Test 1a Failed"
    mf.add_num(3)
    assert mf.find_median() == 2.0, "Test 1b Failed"

    # Test 2: Single element
    mf2 = MedianFinder()
    mf2.add_num(5)
    assert mf2.find_median() == 5.0, "Test 2 Failed"

    # Test 3: Two elements
    mf3 = MedianFinder()
    mf3.add_num(1)
    mf3.add_num(2)
    assert mf3.find_median() == 1.5, "Test 3 Failed"

    # Test 4: Descending order
    mf4 = MedianFinder()
    mf4.add_num(5)
    assert mf4.find_median() == 5.0, "Test 4a Failed"
    mf4.add_num(3)
    assert mf4.find_median() == 4.0, "Test 4b Failed"
    mf4.add_num(1)
    assert mf4.find_median() == 3.0, "Test 4c Failed"

    # Test 5: Same elements
    mf5 = MedianFinder()
    mf5.add_num(1)
    mf5.add_num(1)
    mf5.add_num(1)
    assert mf5.find_median() == 1.0, "Test 5 Failed"

    # Test 6: Negative numbers
    mf6 = MedianFinder()
    mf6.add_num(-1)
    mf6.add_num(-2)
    assert mf6.find_median() == -1.5, "Test 6a Failed"
    mf6.add_num(-3)
    assert mf6.find_median() == -2.0, "Test 6b Failed"

    # Test 7: Mixed positive and negative
    mf7 = MedianFinder()
    mf7.add_num(-5)
    mf7.add_num(10)
    assert mf7.find_median() == 2.5, "Test 7a Failed"
    mf7.add_num(0)
    assert mf7.find_median() == 0.0, "Test 7b Failed"

    print("All test cases passed!")
