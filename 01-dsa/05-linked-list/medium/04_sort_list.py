"""
Sort List - Day 18 | Medium | LC 148
https://leetcode.com/problems/sort-list/

Pattern: Merge Sort (Divide and Conquer)

Sort a linked list in O(n log n) time and O(log n) space (recursion stack).

Example:
    Input:  4 -> 2 -> 1 -> 3
    Output: 1 -> 2 -> 3 -> 4

Approach (Top-Down Merge Sort):
    1. Find the middle of the list using fast/slow pointers
    2. Split the list into two halves
    3. Recursively sort each half
    4. Merge the two sorted halves

Why merge sort for linked lists?
    - No random access needed (unlike quicksort)
    - Split at middle is O(n) but merge is O(n) with O(1) extra space
    - Total: O(n log n) time, O(log n) space for recursion

Time:  O(n log n) - standard merge sort
Space: O(log n) - recursion stack depth
"""


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


def sort_list(head: ListNode) -> ListNode:
    # Base case: empty or single node
    if not head or not head.next:
        return head

    # Step 1: Find middle and split
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None  # cut the list in two

    # Step 2: Recursively sort both halves
    left = sort_list(head)
    right = sort_list(mid)

    # Step 3: Merge sorted halves
    return merge(left, right)


def merge(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    curr.next = l1 or l2
    return dummy.next


if __name__ == "__main__":
    # Test 1: Unsorted list
    head = build([4, 2, 1, 3])
    result = sort_list(head)
    assert to_list(result) == [1, 2, 3, 4], f"Expected [1,2,3,4], got {to_list(result)}"

    # Test 2: Reverse sorted
    head = build([5, 4, 3, 2, 1])
    result = sort_list(head)
    assert to_list(result) == [1, 2, 3, 4, 5], f"Expected [1,2,3,4,5], got {to_list(result)}"

    # Test 3: Already sorted
    head = build([1, 2, 3])
    result = sort_list(head)
    assert to_list(result) == [1, 2, 3], f"Expected [1,2,3], got {to_list(result)}"

    # Test 4: Empty list
    result = sort_list(None)
    assert to_list(result) == [], f"Expected [], got {to_list(result)}"

    # Test 5: With duplicates
    head = build([3, 1, 2, 3, 1])
    result = sort_list(head)
    assert to_list(result) == [1, 1, 2, 3, 3], f"Expected [1,1,2,3,3], got {to_list(result)}"

    print("All tests passed!")
