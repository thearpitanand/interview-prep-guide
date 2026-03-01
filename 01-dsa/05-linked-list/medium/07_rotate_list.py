"""
Rotate List - Day 19 | Medium | LC 61
https://leetcode.com/problems/rotate-list/

Pattern: Two Pointers / Cycle then Cut

Rotate the list to the right by k places.

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5, k = 2
    Output: 4 -> 5 -> 1 -> 2 -> 3

Approach:
    1. Find the length of the list
    2. k = k % length (handle k >= length)
    3. Connect tail to head (make it circular)
    4. Move (length - k) steps from head to find the new tail
    5. The node after new tail is the new head
    6. Break the cycle

Time:  O(n) - two passes at most
Space: O(1)
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


def rotate_right(head: ListNode, k: int) -> ListNode:
    if not head or not head.next or k == 0:
        return head

    # Step 1: Find length and tail
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: Normalize k
    k = k % length
    if k == 0:
        return head

    # Step 3: Make it circular
    tail.next = head

    # Step 4: Find the new tail (length - k steps from head)
    steps_to_new_tail = length - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next

    # Step 5: New head is after new tail
    new_head = new_tail.next

    # Step 6: Break the cycle
    new_tail.next = None

    return new_head


if __name__ == "__main__":
    # Test 1: Normal rotation
    head = build([1, 2, 3, 4, 5])
    result = rotate_right(head, 2)
    assert to_list(result) == [4, 5, 1, 2, 3], f"Expected [4,5,1,2,3], got {to_list(result)}"

    # Test 2: k > length
    head = build([0, 1, 2])
    result = rotate_right(head, 4)  # 4 % 3 = 1
    assert to_list(result) == [2, 0, 1], f"Expected [2,0,1], got {to_list(result)}"

    # Test 3: k = 0
    head = build([1, 2, 3])
    result = rotate_right(head, 0)
    assert to_list(result) == [1, 2, 3], f"Expected [1,2,3], got {to_list(result)}"

    # Test 4: Single element
    head = build([1])
    result = rotate_right(head, 5)
    assert to_list(result) == [1], f"Expected [1], got {to_list(result)}"

    # Test 5: k = length (full rotation = no change)
    head = build([1, 2, 3])
    result = rotate_right(head, 3)
    assert to_list(result) == [1, 2, 3], f"Expected [1,2,3], got {to_list(result)}"

    print("All tests passed!")
