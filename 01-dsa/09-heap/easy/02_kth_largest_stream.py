"""
Kth Largest Element in a Stream

Day: 28
Difficulty: Easy
Topic: Min Heap
Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
Pattern: Min Heap of size K

Description:
    Design a class to find the kth largest element in a stream. Note that it
    is the kth largest element in the sorted order, not the kth distinct
    element.

    Implement KthLargest class:
        - KthLargest(int k, int[] nums) Initializes the object with the
          integer k and the stream of integers nums.
        - int add(int val) Appends the integer val to the stream and returns
          the element representing the kth largest element in the stream.

Examples:
    Input:
        ["KthLargest", "add", "add", "add", "add", "add"]
        [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    Output:
        [null, 4, 5, 5, 8, 8]
    Explanation:
        KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2])
        kthLargest.add(3)  -> returns 4  (stream: [2,3,4,5,8], 3rd largest = 4)
        kthLargest.add(5)  -> returns 5  (stream: [2,3,4,5,5,8], 3rd largest = 5)
        kthLargest.add(10) -> returns 5  (stream: [2,3,4,5,5,8,10], 3rd largest = 5)
        kthLargest.add(9)  -> returns 8  (stream: [2,3,4,5,5,8,9,10], 3rd largest = 8)
        kthLargest.add(4)  -> returns 8  (stream: [2,3,4,4,5,5,8,9,10], 3rd largest = 8)

Constraints:
    - 1 <= k <= 10^4
    - 0 <= nums.length <= 10^4
    - -10^4 <= nums[i] <= 10^4
    - -10^4 <= val <= 10^4
    - At most 10^4 calls will be made to add.
    - It is guaranteed that there will be at least k elements when you
      search for the kth element.

Hint:
    Maintain a min-heap of size k. The root of the heap is always the kth
    largest element. When adding a new value, push it to the heap and pop
    if size exceeds k.

Pattern:
    Min Heap of size K - The smallest element in a min-heap of K elements
    is the Kth largest overall.
"""

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass


# ---- Test Cases ----
if __name__ == "__main__":
    # Test 1: Standard case from example
    kl = KthLargest(3, [4, 5, 8, 2])
    assert kl.add(3) == 4, "Test 1a Failed"
    assert kl.add(5) == 5, "Test 1b Failed"
    assert kl.add(10) == 5, "Test 1c Failed"
    assert kl.add(9) == 8, "Test 1d Failed"
    assert kl.add(4) == 8, "Test 1e Failed"

    # Test 2: k=1 (always return max)
    kl2 = KthLargest(1, [])
    assert kl2.add(3) == 3, "Test 2a Failed"
    assert kl2.add(5) == 5, "Test 2b Failed"
    assert kl2.add(2) == 5, "Test 2c Failed"

    # Test 3: Starting with empty nums
    kl3 = KthLargest(2, [])
    assert kl3.add(1) is not None or True  # Only 1 element, k=2 not yet reachable
    kl3.add(2)
    assert kl3.add(3) == 2, "Test 3 Failed"

    # Test 4: All same values
    kl4 = KthLargest(2, [5, 5, 5])
    assert kl4.add(5) == 5, "Test 4 Failed"

    print("All test cases passed!")
