"""
Next Greater Element I

Day: 20 | Difficulty: Easy | Pattern: Monotonic Stack
LeetCode 496: https://leetcode.com/problems/next-greater-element-i/

Problem:
    The next greater element of some element x in an array is the first greater
    element that is to the right of x in the same array.

    You are given two distinct 0-indexed integer arrays nums1 and nums2, where
    nums1 is a subset of nums2.

    For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j]
    and determine the next greater element of nums2[j] in nums2. If there is no
    next greater element, then the answer for this query is -1.

    Return an array ans of length nums1.length such that ans[i] is the next greater
    element as described above.

Examples:
    Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
    Output: [-1,3,-1]
    Explanation:
        - 4 is in nums2 at index 2, no greater element to its right -> -1
        - 1 is in nums2 at index 0, next greater element is 3
        - 2 is in nums2 at index 3, no greater element to its right -> -1

    Input: nums1 = [2,4], nums2 = [1,2,3,4]
    Output: [3,-1]

Constraints:
    - 1 <= nums1.length <= nums2.length <= 1000
    - 0 <= nums1[i], nums2[i] <= 10^4
    - All integers in nums1 and nums2 are unique
    - All the integers of nums1 also appear in nums2

Hint:
    Use a monotonic stack on nums2 to find the next greater element for every
    element in nums2. Store results in a hash map. Then look up each element
    in nums1.

Pattern:
    Monotonic Stack + Hash Map
    - Iterate through nums2 with a decreasing stack
    - When nums2[i] > stack top, pop and record: popped -> nums2[i]
    - Store results in a dict, then look up each nums1[i]
"""

from typing import List


def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    pass


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Mixed results
    assert next_greater_element([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1], "Test 1 Failed"

    # Test 2: All have next greater
    assert next_greater_element([2, 4], [1, 2, 3, 4]) == [3, -1], "Test 2 Failed"

    # Test 3: Single element
    assert next_greater_element([1], [1]) == [-1], "Test 3 Failed"

    # Test 4: All same result
    assert next_greater_element([1, 3, 5], [1, 3, 5]) == [3, 5, -1], "Test 4 Failed"

    # Test 5: Decreasing array
    assert next_greater_element([3, 2, 1], [3, 2, 1]) == [-1, -1, -1], "Test 5 Failed"

    print("All test cases passed!")
