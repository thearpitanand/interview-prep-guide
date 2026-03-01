"""
Palindrome Linked List - Day 17 | Easy | LC 234
https://leetcode.com/problems/palindrome-linked-list/

Pattern: Fast & Slow Pointers + Reversal

Given the head of a singly linked list, return True if it is a
palindrome, False otherwise.

Example:
    Input:  1 -> 2 -> 2 -> 1
    Output: True

    Input:  1 -> 2
    Output: False

Approach:
    1. Find the middle using fast/slow pointers
    2. Reverse the second half of the list
    3. Compare the first half with the reversed second half
    4. (Optional) Restore the list by reversing the second half again

Time:  O(n) - find middle O(n) + reverse O(n/2) + compare O(n/2)
Space: O(1) - in-place reversal
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


def is_palindrome(head: ListNode) -> bool:
    if not head or not head.next:
        return True

    # Step 1: Find the middle (slow will be at start of second half)
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half starting from slow
    prev = None
    curr = slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    # prev is now the head of the reversed second half

    # Step 3: Compare first half and reversed second half
    left = head
    right = prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


if __name__ == "__main__":
    # Test 1: Even palindrome
    head = build([1, 2, 2, 1])
    assert is_palindrome(head) == True, "Expected True for [1,2,2,1]"

    # Test 2: Not palindrome
    head = build([1, 2])
    assert is_palindrome(head) == False, "Expected False for [1,2]"

    # Test 3: Odd palindrome
    head = build([1, 2, 1])
    assert is_palindrome(head) == True, "Expected True for [1,2,1]"

    # Test 4: Single element
    head = build([1])
    assert is_palindrome(head) == True, "Expected True for [1]"

    # Test 5: All same values
    head = build([1, 1, 1, 1])
    assert is_palindrome(head) == True, "Expected True for [1,1,1,1]"

    # Test 6: Not palindrome longer
    head = build([1, 2, 3, 4])
    assert is_palindrome(head) == False, "Expected False for [1,2,3,4]"

    print("All tests passed!")
