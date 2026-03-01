"""
Problem: Maximize Consecutive Differences Circular (GFG) | Optional | Medium
Topic: Greedy

Rearrange array elements in circular fashion to maximize the sum of consecutive
absolute differences.

Example 1:
  Input: arr = [4, 2, 1, 8]
  Output: 18

Constraints:
  - 1 <= n <= 10^5

Hint: Same as max sum abs diff circular. Sort, place small and large alternately.
Pattern: Greedy / Sorting
"""


def max_consecutive_diff(arr: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_consecutive_diff([4, 2, 1, 8]) == 18
    assert max_consecutive_diff([1, 1, 1]) == 0
    print("All tests passed!")
