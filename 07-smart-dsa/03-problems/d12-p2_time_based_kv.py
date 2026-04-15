"""
Problem: Time Based Key-Value Store (LC 981) | Smart-DSA Day 12 | Medium
Pattern: Binary Search
Time target: 30 minutes

Design a time-based key-value data structure that can store multiple values
for the same key at different timestamps and retrieve the value at a given
timestamp.

Implement TimeMap:
  - TimeMap() initializes the object.
  - set(key, value, timestamp) stores the key-value pair at the given timestamp.
  - get(key, timestamp) returns the value stored at the largest timestamp
    <= the given timestamp, or "" if no such value exists.

Timestamps in set are strictly increasing.

Example:
  tm = TimeMap()
  tm.set("foo", "bar", 1)
  tm.get("foo", 1)   → "bar"
  tm.get("foo", 3)   → "bar"
  tm.set("foo", "bar2", 4)
  tm.get("foo", 4)   → "bar2"
  tm.get("foo", 5)   → "bar2"

Constraints:
  - 1 <= key.length, value.length <= 100
  - 1 <= timestamp <= 10^7
  - All timestamps in set are strictly increasing for a given key.
  - At most 2 * 10^5 calls total to set and get.

Hint (⚠ read only after time budget is blown):
  Store list of (timestamp, value) pairs per key. On get, binary search for
  the largest timestamp <= queried timestamp (upper bound - 1 style).
"""


class TimeMap:
    def __init__(self) -> None:
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass


if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"
    tm.set("foo", "bar2", 4)
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"
    assert tm.get("foo", 0) == ""
    print("All tests passed!")
