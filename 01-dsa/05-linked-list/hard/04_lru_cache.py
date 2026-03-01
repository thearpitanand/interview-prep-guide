"""
LRU Cache - Day 19 | Hard | LC 146
https://leetcode.com/problems/lru-cache/

Pattern: Doubly Linked List + Hash Map

Design a data structure that follows the Least Recently Used (LRU)
cache eviction policy.

Operations:
    - get(key): Return the value if key exists, otherwise -1.
      Mark as recently used.
    - put(key, value): Insert or update. If capacity exceeded,
      evict the least recently used item.

Both operations must run in O(1) time.

Example:
    cache = LRUCache(2)
    cache.put(1, 1)    # cache: {1=1}
    cache.put(2, 2)    # cache: {1=1, 2=2}
    cache.get(1)       # returns 1, cache: {2=2, 1=1}
    cache.put(3, 3)    # evicts key 2, cache: {1=1, 3=3}
    cache.get(2)       # returns -1 (not found)

Approach:
    - Hash map: key -> doubly linked list node (O(1) lookup)
    - Doubly linked list: maintains usage order
      - Head = most recently used
      - Tail = least recently used
    - On access: move node to head
    - On insert at capacity: remove tail, add new node at head

Why doubly linked list?
    - O(1) removal of any node (don't need to find previous)
    - O(1) insertion at head/tail

Time:  O(1) for both get and put
Space: O(capacity) for the cache
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


class DLLNode:
    """Doubly linked list node for LRU Cache."""
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> DLLNode

        # Dummy head and tail to avoid edge cases
        self.head = DLLNode()  # most recently used side
        self.tail = DLLNode()  # least recently used side
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: DLLNode):
        """Remove a node from the doubly linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: DLLNode):
        """Add a node right after the dummy head (most recent position)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _move_to_front(self, node: DLLNode):
        """Move an existing node to the front (mark as most recently used)."""
        self._remove(node)
        self._add_to_front(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            node.val = value
            self._move_to_front(node)
        else:
            # Create new node
            if len(self.cache) >= self.capacity:
                # Evict least recently used (node before tail)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

            new_node = DLLNode(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)


if __name__ == "__main__":
    # Test 1: Basic operations from LC example
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1, f"Expected 1, got {cache.get(1)}"
    cache.put(3, 3)       # evicts key 2
    assert cache.get(2) == -1, f"Expected -1, got {cache.get(2)}"
    cache.put(4, 4)       # evicts key 1
    assert cache.get(1) == -1, f"Expected -1, got {cache.get(1)}"
    assert cache.get(3) == 3, f"Expected 3, got {cache.get(3)}"
    assert cache.get(4) == 4, f"Expected 4, got {cache.get(4)}"

    # Test 2: Update existing key
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)      # update key 1
    assert cache.get(1) == 10, f"Expected 10, got {cache.get(1)}"
    cache.put(3, 3)       # should evict key 2 (not 1, since 1 was recently updated)
    assert cache.get(2) == -1, f"Expected -1, got {cache.get(2)}"

    # Test 3: Capacity of 1
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)       # evicts key 1
    assert cache.get(1) == -1, f"Expected -1"
    assert cache.get(2) == 2, f"Expected 2"

    # Test 4: Get makes it recently used
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)          # makes key 1 recently used
    cache.put(3, 3)       # should evict key 2 (least recently used)
    assert cache.get(2) == -1, "Key 2 should have been evicted"
    assert cache.get(1) == 1, "Key 1 should still exist"
    assert cache.get(3) == 3, "Key 3 should exist"

    # Test 5: Miss returns -1
    cache = LRUCache(3)
    assert cache.get(99) == -1, "Non-existent key should return -1"

    print("All tests passed!")
