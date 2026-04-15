# Linked List

## Recognition Signals (how to spot this in <90s)
- Input is explicitly a linked list (nodes with `.next` pointers)
- Problem asks to **reverse**, **merge**, **reorder**, or **split** a list
- You need to detect or find the **start of a cycle**
- Problem asks for the **k-th from end**, **middle node**, or **intersection**
- You need O(1) extra space — ruling out converting to an array first

## Mental Model

Linked list problems almost always reduce to one of two skills: pointer manipulation or the two-pointer (fast/slow) technique. Pointer manipulation is surgical: you redirect `.next` pointers one at a time, keeping enough temporary variables so you never lose a node. The golden rule is to draw a small example (3–4 nodes) and simulate the pointer moves on paper before writing a single line of code. If you code it from memory without drawing, you will hit a null pointer error or create a cycle.

The fast/slow pointer (Floyd's algorithm) is a completely different tool. You run two pointers through the same list at different speeds — one moves one step at a time, the other moves two. Their relative motion reveals hidden structure: if there is a cycle, the fast pointer laps the slow one and they meet. If there is no cycle, fast reaches the end. This same two-speed trick finds the middle of a list, the start of a cycle, and the k-th from end — three different problems, one mental model.

## Reusable Python Template

```python
from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


# --- Iterative Reversal ---
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev: Optional[ListNode] = None
    curr = head
    while curr:
        nxt = curr.next   # save next before overwriting
        curr.next = prev  # reverse the pointer
        prev = curr       # advance prev
        curr = nxt        # advance curr
    return prev           # prev is the new head


# --- Fast / Slow Pointer ---
def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next        # type: ignore[assignment]
        fast = fast.next.next   # type: ignore[union-attr]
    return slow  # slow lands on middle (or right-middle for even length)


def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next        # type: ignore[assignment]
        fast = fast.next.next   # type: ignore[union-attr]
        if slow is fast:
            return True
    return False


# --- Merge Two Sorted Lists ---
def merge_two_lists(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2   # attach the remaining list
    return dummy.next
```

## Common Mistakes

- **Losing the next pointer**: In reversal, always save `nxt = curr.next` BEFORE writing `curr.next = prev`. Forgetting this severs the rest of the list.
- **Off-by-one in fast/slow termination**: The while condition must be `while fast and fast.next` — not just `while fast`. If `fast.next` is None, accessing `fast.next.next` crashes.
- **Mutating the input list unexpectedly**: Some problems expect the original nodes to remain intact. Use a dummy head and build a new chain when in doubt.
- **Forgetting the dummy head trick**: When the head node itself might change (reversal, remove-nth-from-end), add `dummy = ListNode(0); dummy.next = head` at the start. Return `dummy.next` at the end. This eliminates all special-case logic for the head.
- **Cycle detection: checking value equality vs. identity**: Use `slow is fast` (identity), not `slow.val == fast.val`. Two different nodes can share a value; you need the same object.

## Watch Me Solve (I do)

**Problem: Reverse Linked List (LC 206)**

Given the head of a singly linked list, reverse the list and return the reversed list's head.

---

I see "linked list" and "reverse" — this is pure pointer manipulation. My goal is to make every `.next` pointer point backwards.

I need three variables: `prev` (what the current node should now point to), `curr` (the node I'm currently processing), and `nxt` (a saved reference to the next node before I destroy it).

Let me trace through `1 → 2 → 3 → 4 → 5 → None`:

**Before loop:** `prev = None`, `curr = 1`

- Iteration 1: `nxt = 2`. Set `1.next = None`. Now `prev = 1`, `curr = 2`.
- Iteration 2: `nxt = 3`. Set `2.next = 1`. Now `prev = 2`, `curr = 3`.
- Iteration 3: `nxt = 4`. Set `3.next = 2`. Now `prev = 3`, `curr = 4`.
- Iteration 4: `nxt = 5`. Set `4.next = 3`. Now `prev = 4`, `curr = 5`.
- Iteration 5: `nxt = None`. Set `5.next = 4`. Now `prev = 5`, `curr = None`.

Loop ends because `curr` is None. `prev` is node 5 — the new head. Result: `5 → 4 → 3 → 2 → 1 → None`. ✓

```python
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev: Optional[ListNode] = None
    curr = head

    while curr:
        nxt = curr.next   # 1. save next before we clobber it
        curr.next = prev  # 2. reverse this link
        prev = curr       # 3. slide prev forward
        curr = nxt        # 4. slide curr forward

    return prev  # prev is the new head when curr falls off the end
```

**Complexity:** O(n) time, O(1) space. Every node visited exactly once.

---

**Second example: Linked List Cycle — finding the cycle with fast/slow pointers (LC 141/142)**

The problem: does this list have a cycle? (LC 141). If yes, where does the cycle begin? (LC 142).

The fast/slow trick: put two runners at the head. Slow moves one step, fast moves two. If there is a cycle, fast eventually laps slow and they meet inside the cycle. If no cycle, fast falls off the end.

```python
def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:          # fast.next guards against .next.next crash
        slow = slow.next               # type: ignore[assignment]
        fast = fast.next.next          # type: ignore[union-attr]
        if slow is fast:               # identity check, not value check
            return True
    return False
```

**To find the cycle start (LC 142):** once slow and fast meet, reset one pointer to `head`. Advance both one step at a time. They meet again exactly at the cycle entrance. This works due to a mathematical property of the distances traveled — you don't need to memorize the proof, just the recipe.

```python
def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next               # type: ignore[assignment]
        fast = fast.next.next          # type: ignore[union-attr]
        if slow is fast:
            # reset one pointer to head; advance both at same speed
            slow = head
            while slow is not fast:
                slow = slow.next       # type: ignore[assignment]
                fast = fast.next       # type: ignore[union-attr]
            return slow                # cycle entrance
    return None
```

**Key pattern to internalize:** fast/slow meets `→` reset one to head `→` step both at speed 1 `→` meeting point is the answer. This pattern shows up in interview problems more often than you'd expect.
