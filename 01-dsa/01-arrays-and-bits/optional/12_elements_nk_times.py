"""
Problem: Elements Appearing More Than n/k Times (GFG) | Optional | Medium
Topic: Arrays

Given an array of size n, find all elements that appear more than n/k times.

Example 1:
  Input: arr = [3, 1, 2, 2, 1, 2, 3, 3], k = 4
  Output: [2, 3]  # n/k = 8/4 = 2, elements appearing > 2 times

Constraints:
  - 1 <= n <= 10^4
  - 1 <= k <= n

Hint: Extended Boyer-Moore voting for at most k-1 candidates.
Pattern: Boyer-Moore Voting
"""


def elements_nk_times(arr: list[int], k: int) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert sorted(elements_nk_times([3, 1, 2, 2, 1, 2, 3, 3], 4)) == [2, 3]
    assert elements_nk_times([1, 1, 2, 2, 3], 5) == []  # threshold = 1, all appear 1-2 times but not > 1
    print("All tests passed!")
