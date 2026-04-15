"""
Problem: LRU Cache (LC 146) | Smart-DSA Day 20 | Medium
Pattern: Hash Map + Doubly Linked List
Time target: 35 minutes

Design a data structure that follows the Least Recently Used (LRU) cache
eviction policy.

Implement the LRUCache class:
  - LRUCache(capacity) — initializes with positive capacity.
  - get(key) — returns the value if the key exists, else -1. Marks as recently used.
  - put(key, value) — updates or inserts. If capacity exceeded, evict the LRU key.

Both operations must run in O(1) average time.

Example 1:
  Input:  ["LRUCache","put","put","get","put","get","put","get","get","get"]
          [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
  Output: [null,null,null,1,null,-1,null,-1,3,4]

Constraints:
  - 1 <= capacity <= 3000
  - 0 <= key <= 10^4
  - 0 <= value <= 10^5
  - At most 2 * 10^5 calls to get and put.

Hint (⚠ read only after time budget is blown):
  Use a dict mapping key -> doubly linked list node. Maintain dummy head and
  tail sentinels. On every access move the node to just before the tail
  (most recent). On eviction remove the node just after the head (least recent).
"""


class LRUCache:
    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1      # returns 1, key 1 is now most recent
    cache.put(3, 3)               # evicts key 2 (LRU)
    assert cache.get(2) == -1     # key 2 was evicted
    cache.put(4, 4)               # evicts key 1 (LRU — key 3 was just used)
    assert cache.get(1) == -1     # key 1 evicted
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    cache2 = LRUCache(1)
    cache2.put(2, 1)
    assert cache2.get(2) == 1
    cache2.put(3, 2)
    assert cache2.get(2) == -1
    assert cache2.get(3) == 2

    print("All tests passed!")
