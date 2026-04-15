"""
Problem: Find Median from Data Stream (LC 295) | Smart-DSA Day 31 | Hard
Pattern: Two Heaps
Time target: 40 minutes

Design a data structure that supports:
  - addNum(num): add an integer from the data stream.
  - findMedian(): return the median of all elements added so far.

If the total count is even, the median is the average of the two middle values.

Example:
  addNum(1)      → [1]           → findMedian() == 1.0
  addNum(2)      → [1, 2]        → findMedian() == 1.5
  addNum(3)      → [1, 2, 3]     → findMedian() == 2.0

Constraints:
  - -10^5 <= num <= 10^5
  - At least one element will have been added before findMedian() is called.
  - At most 5 * 10^4 calls will be made to addNum and findMedian.

Hint (⚠ read only after time budget is blown):
  Split the stream at the median: lower half in a max-heap (negate values),
  upper half in a min-heap. After each insert, rebalance so sizes differ by
  at most 1. The median is the root of the larger heap (odd count) or the
  average of both roots (even count).
"""
import heapq


class MedianFinder:
    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    assert mf.findMedian() == 1.0
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0

    mf2 = MedianFinder()
    mf2.addNum(6)
    assert mf2.findMedian() == 6.0
    mf2.addNum(10)
    assert mf2.findMedian() == 8.0
    mf2.addNum(2)
    assert mf2.findMedian() == 6.0
    mf2.addNum(6)
    assert mf2.findMedian() == 6.0
    print("All tests passed!")
