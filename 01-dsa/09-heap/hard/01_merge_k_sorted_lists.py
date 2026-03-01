"""
Merge K Sorted Lists

Day: 28
Difficulty: Hard
Topic: Min Heap
Link: https://leetcode.com/problems/merge-k-sorted-lists/
Pattern: Merge K Sorted (Min Heap tracking heads)

Description:
    You are given an array of k linked-lists lists, each linked-list is
    sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.

    For simplicity, we use Python lists instead of linked lists in this
    implementation.

Examples:
    Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    Output: [1, 1, 2, 3, 4, 4, 5, 6]
    Explanation: Merging all sorted lists into one sorted list.

    Input: lists = []
    Output: []

    Input: lists = [[]]
    Output: []

Constraints:
    - k == lists.length
    - 0 <= k <= 10^4
    - 0 <= lists[i].length <= 500
    - -10^4 <= lists[i][j] <= 10^4
    - lists[i] is sorted in ascending order.
    - The sum of lists[i].length will not exceed 10^4.

Hint:
    Use a min-heap to track the current smallest element across all lists.
    Push (value, list_index, element_index) into the heap.
    Pop the smallest, add it to the result, and push the next element from
    the same list.

    Time: O(N log K) where N is total elements, K is number of lists.
    Space: O(K) for the heap.

Pattern:
    Merge K Sorted - Use a min-heap of size K. Initialize with the first
    element from each list. Pop the minimum, push the next element from
    that same list. Repeat until the heap is empty.
"""

import heapq
from typing import List


def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    # Test 1: Standard case
    assert merge_k_sorted_lists([[1, 4, 5], [1, 3, 4], [2, 6]]) == [
        1, 1, 2, 3, 4, 4, 5, 6
    ], "Test 1 Failed"

    # Test 2: Empty input
    assert merge_k_sorted_lists([]) == [], "Test 2 Failed"

    # Test 3: Single empty list
    assert merge_k_sorted_lists([[]]) == [], "Test 3 Failed"

    # Test 4: Single non-empty list
    assert merge_k_sorted_lists([[1, 2, 3]]) == [1, 2, 3], "Test 4 Failed"

    # Test 5: Two lists
    assert merge_k_sorted_lists([[1, 3, 5], [2, 4, 6]]) == [
        1, 2, 3, 4, 5, 6
    ], "Test 5 Failed"

    # Test 6: Lists with different lengths
    assert merge_k_sorted_lists([[1], [2, 3, 4], [5, 6]]) == [
        1, 2, 3, 4, 5, 6
    ], "Test 6 Failed"

    # Test 7: Lists with duplicates
    assert merge_k_sorted_lists([[1, 1, 1], [1, 1], [1]]) == [
        1, 1, 1, 1, 1, 1
    ], "Test 7 Failed"

    # Test 8: Negative numbers
    assert merge_k_sorted_lists([[-3, -1, 2], [-2, 0, 4]]) == [
        -3, -2, -1, 0, 2, 4
    ], "Test 8 Failed"

    # Test 9: Mix of empty and non-empty lists
    assert merge_k_sorted_lists([[], [1], [], [2, 3], []]) == [
        1, 2, 3
    ], "Test 9 Failed"

    print("All test cases passed!")
