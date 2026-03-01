"""
Merge k Sorted Lists - Day 19 | Hard | LC 23
https://leetcode.com/problems/merge-k-sorted-lists/

Pattern: Heap (Priority Queue) + Merge

Merge k sorted linked lists and return it as one sorted list.

Example:
    Input:  [[1,4,5], [1,3,4], [2,6]]
    Output: [1,1,2,3,4,4,5,6]

Approach (Min-Heap):
    1. Push the head of each list into a min-heap
    2. Pop the smallest node, add it to result
    3. If the popped node has a next, push that next node
    4. Repeat until heap is empty

    We use a counter to break ties in the heap since ListNode
    objects are not comparable.

Alternative: Divide and conquer merge (merge pairs repeatedly)

Time:  O(N log k) - N total nodes, each heap operation is O(log k)
Space: O(k) - heap holds at most k nodes
"""

import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(arr):
    dummy = ListNode(0)
    curr = dummy
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def merge_k_lists(lists: list) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    heap = []
    counter = 0  # tiebreaker for nodes with same value

    # Initialize heap with head of each list
    for head in lists:
        if head:
            heapq.heappush(heap, (head.val, counter, head))
            counter += 1

    while heap:
        val, _, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, counter, node.next))
            counter += 1

    return dummy.next


if __name__ == "__main__":
    # Test 1: Three sorted lists
    lists = [build([1, 4, 5]), build([1, 3, 4]), build([2, 6])]
    result = merge_k_lists(lists)
    assert to_list(result) == [1, 1, 2, 3, 4, 4, 5, 6], \
        f"Expected [1,1,2,3,4,4,5,6], got {to_list(result)}"

    # Test 2: Empty input
    result = merge_k_lists([])
    assert to_list(result) == [], f"Expected [], got {to_list(result)}"

    # Test 3: List of empty lists
    result = merge_k_lists([None, None])
    assert to_list(result) == [], f"Expected [], got {to_list(result)}"

    # Test 4: Single list
    result = merge_k_lists([build([1, 2, 3])])
    assert to_list(result) == [1, 2, 3], f"Expected [1,2,3], got {to_list(result)}"

    # Test 5: Two lists
    lists = [build([1, 3, 5]), build([2, 4, 6])]
    result = merge_k_lists(lists)
    assert to_list(result) == [1, 2, 3, 4, 5, 6], \
        f"Expected [1,2,3,4,5,6], got {to_list(result)}"

    print("All tests passed!")
