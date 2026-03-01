"""
Problem: Min Swaps for Bracket Balancing (GFG) | Optional | Medium
Topic: Strings

Given a string of '[' and ']', find the minimum number of swaps to make it balanced.

Example 1:
  Input: s = "[]][]["
  Output: 1

Constraints:
  - 2 <= len(s) <= 10^5, even length

Hint: Track imbalance (unmatched closing brackets), swap when needed.
Pattern: Greedy
"""


def min_swaps_brackets(s: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert min_swaps_brackets("[]][][") == 1
    assert min_swaps_brackets("[[][]]") == 0
    print("All tests passed!")
