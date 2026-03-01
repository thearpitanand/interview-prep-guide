"""
Problem: LRU Page Replacement (GFG) | Optional | Medium
Topic: Greedy

Given memory capacity and page references, find the number of page faults
using LRU (Least Recently Used) page replacement algorithm.

Example 1:
  Input: pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2], capacity = 4
  Output: 6

Constraints:
  - 1 <= n <= 10^4

Hint: Use OrderedDict as LRU cache. Move to end on access, pop first on eviction.
Pattern: LRU Cache
"""


def lru_page_faults(pages: list[int], capacity: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert lru_page_faults([7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2], 4) == 6
    assert lru_page_faults([1, 2, 3, 4, 1, 2], 3) == 5
    print("All tests passed!")
