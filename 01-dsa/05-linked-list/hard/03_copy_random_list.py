"""
Copy List with Random Pointer - Day 19 | Hard | LC 138
https://leetcode.com/problems/copy-list-with-random-pointer/

Pattern: Hash Map

A linked list has nodes with an additional random pointer that can
point to any node in the list or None. Construct a deep copy of this list.

Example:
    Input:  [[7,null],[13,0],[11,4],[10,2],[1,0]]
    Each element is [val, random_index].
    Output: Deep copy of the entire structure.

Approach (Hash Map):
    1. First pass: create a copy of each node, store in hash map
       {original_node: copy_node}
    2. Second pass: set next and random pointers using the hash map
    3. Return the copy of the head

Alternative: Interleaving approach (O(1) space) - insert copies between
originals, set random pointers, then separate the two lists.

Time:  O(n) - two passes
Space: O(n) - hash map storing n node mappings
"""


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def build_random_list(values, random_indices):
    """
    Build a linked list with random pointers.
    values: list of node values
    random_indices: list of indices (or None) for each node's random pointer
    """
    if not values:
        return None

    nodes = [Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, idx in enumerate(random_indices):
        if idx is not None:
            nodes[i].random = nodes[idx]

    return nodes[0]


def to_list_with_random(head):
    """Convert to list of (val, random_val_or_None) for verification."""
    result = []
    node_to_index = {}
    curr = head
    idx = 0
    while curr:
        node_to_index[curr] = idx
        curr = curr.next
        idx += 1

    curr = head
    while curr:
        random_idx = node_to_index[curr.random] if curr.random else None
        result.append((curr.val, random_idx))
        curr = curr.next
    return result


def copy_random_list(head: Node) -> Node:
    if not head:
        return None

    # Pass 1: Create copy nodes and map original -> copy
    old_to_new = {}
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    # Pass 2: Set next and random pointers
    curr = head
    while curr:
        copy = old_to_new[curr]
        copy.next = old_to_new.get(curr.next)
        copy.random = old_to_new.get(curr.random)
        curr = curr.next

    return old_to_new[head]


if __name__ == "__main__":
    # Test 1: List with random pointers
    # [7,None], [13,0], [11,4], [10,2], [1,0]
    head = build_random_list([7, 13, 11, 10, 1], [None, 0, 4, 2, 0])
    copy = copy_random_list(head)

    # Verify it's a deep copy (different objects, same structure)
    original_repr = to_list_with_random(head)
    copy_repr = to_list_with_random(copy)
    assert original_repr == copy_repr, f"Expected {original_repr}, got {copy_repr}"

    # Verify it's truly a deep copy (different node objects)
    curr_orig = head
    curr_copy = copy
    while curr_orig:
        assert curr_orig is not curr_copy, "Copy should be different objects"
        curr_orig = curr_orig.next
        curr_copy = curr_copy.next

    # Test 2: Single node pointing to itself
    head = Node(1)
    head.random = head
    copy = copy_random_list(head)
    assert copy.val == 1, f"Expected val 1, got {copy.val}"
    assert copy.random is copy, "Random should point to itself"
    assert copy is not head, "Should be a different object"

    # Test 3: Empty list
    assert copy_random_list(None) is None, "Expected None for empty list"

    # Test 4: Two nodes, random pointers to each other
    head = build_random_list([1, 2], [1, 0])
    copy = copy_random_list(head)
    assert copy.val == 1 and copy.next.val == 2
    assert copy.random is copy.next, "Node 1 random should point to node 2"
    assert copy.next.random is copy, "Node 2 random should point to node 1"

    print("All tests passed!")
