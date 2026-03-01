"""
Intersection of Two Linked Lists - Day 18 | Medium | LC 160
https://leetcode.com/problems/intersection-of-two-linked-lists/

Pattern: Two Pointers

Given the heads of two singly linked lists, return the node at which
the two lists intersect. If they don't intersect, return None.

Example:
    List A: 4 -> 1 ─┐
                      → 8 -> 4 -> 5
    List B: 5 -> 6 -> 1 ─┘
    Output: Node with value 8

Approach:
    - Use two pointers starting at each head
    - When pointer A reaches the end, redirect to headB
    - When pointer B reaches the end, redirect to headA
    - They will meet at the intersection (or both reach None)

Why it works:
    - After one switch, both pointers have traveled the same total distance
    - len(A-only) + len(shared) + len(B-only) == len(B-only) + len(shared) + len(A-only)
    - So they align at the intersection point

Time:  O(n + m) - each pointer traverses both lists
Space: O(1) - two pointers
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


def get_intersection_node(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None

    ptrA = headA
    ptrB = headB

    # Each pointer traverses its own list, then the other list
    # They meet at the intersection or both become None
    while ptrA is not ptrB:
        ptrA = ptrA.next if ptrA else headB
        ptrB = ptrB.next if ptrB else headA

    return ptrA  # either the intersection node or None


if __name__ == "__main__":
    # Test 1: Lists intersect
    # A: 4 -> 1 -> [8 -> 4 -> 5]
    # B: 5 -> 6 -> 1 -> [8 -> 4 -> 5]
    shared = build([8, 4, 5])
    headA = ListNode(4, ListNode(1, shared))
    headB = ListNode(5, ListNode(6, ListNode(1, shared)))
    result = get_intersection_node(headA, headB)
    assert result is shared, f"Expected intersection at node 8"
    assert result.val == 8, f"Expected value 8, got {result.val}"

    # Test 2: No intersection
    headA = build([1, 2, 3])
    headB = build([4, 5, 6])
    result = get_intersection_node(headA, headB)
    assert result is None, "Expected None for non-intersecting lists"

    # Test 3: Intersect at first node of shorter list
    shared = build([1, 2, 3])
    headA = shared
    headB = ListNode(0, shared)
    result = get_intersection_node(headA, headB)
    assert result is shared, "Expected intersection at head of A"

    # Test 4: One list is empty
    headA = build([1, 2])
    result = get_intersection_node(headA, None)
    assert result is None, "Expected None when one list is empty"

    print("All tests passed!")
