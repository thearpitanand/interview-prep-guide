"""
Problem: Minimize Max Difference Between Heights (GFG) | Optional | Medium
Topic: Arrays

Given heights of n towers and a value K, either increase or decrease the height
of every tower by K (only once). Find the minimum possible difference between
the tallest and shortest tower after modifications.

Example 1:
  Input: arr = [1, 15, 10], k = 6
  Output: 5  # [7, 9, 4] -> max-min = 9-4 = 5

Constraints:
  - 1 <= n <= 10^5
  - 1 <= k <= 10^4
  - 1 <= arr[i] <= 10^5

Hint: Sort, then for each split point try +K for left part and -K for right part.
Pattern: Greedy + Sorting
"""


def minimize_max_diff(arr: list[int], k: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert minimize_max_diff([1, 15, 10], 6) == 5
    assert minimize_max_diff([1, 5, 8, 10], 2) == 5
    print("All tests passed!")
