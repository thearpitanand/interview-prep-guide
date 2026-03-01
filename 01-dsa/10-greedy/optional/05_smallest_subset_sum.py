"""
Problem: Smallest Subset with Sum > All Others (GFG) | Optional | Easy
Topic: Greedy

Find the minimum number of elements such that their sum is greater than
the sum of remaining elements.

Example 1:
  Input: arr = [3, 1, 7, 1]
  Output: 1  # just [7] > 3+1+1=5

Constraints:
  - 1 <= n <= 10^5

Hint: Sort descending. Keep adding until subset sum > remaining.
Pattern: Greedy / Sorting
"""


def smallest_subset(arr: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert smallest_subset([3, 1, 7, 1]) == 1
    assert smallest_subset([1, 1, 1, 1]) == 3
    print("All tests passed!")
