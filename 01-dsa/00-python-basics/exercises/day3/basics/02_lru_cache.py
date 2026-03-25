"""
LRU Cache (Least Recently Used)
================================
LeetCode 146 | Day 3 | Medium

What it does:
    Fixed-size cache that evicts the LEAST recently used item when full.
    - get(key)        -> returns value, marks key as recently used
    - put(key, value) -> inserts/updates key, evicts LRU item if over capacity

Key Insight:
    OrderedDict maintains insertion order. We exploit this:
    - move_to_end(key)     -> marks as "most recently used" (moves to right end)
    - popitem(last=False)  -> evicts "least recently used" (removes from left end)

    Internally: doubly-linked list + hash map = O(1) for both get and put.

Visual Example (capacity=2):
    put(1,1)  -> cache: {1:1}
    put(2,2)  -> cache: {1:1, 2:2}
    get(1)    -> returns 1, cache: {2:2, 1:1}  (1 moved to end = most recent)
    put(3,3)  -> cache full! evict leftmost (2), cache: {1:1, 3:3}
    get(2)    -> returns -1 (was evicted)

Pattern: Hash Map + Doubly Linked List (OrderedDict wraps both)
"""

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)  # mark as most recently used
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)  # existing key -> refresh position

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # evict least recently used (leftmost)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1        # returns 1, key 1 is now most recent
    cache.put(3, 3)                  # evicts key 2 (least recent)
    assert cache.get(2) == -1        # key 2 was evicted
    cache.put(4, 4)                  # evicts key 1
    assert cache.get(1) == -1        # key 1 was evicted
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    print("All tests passed!")
