"""
Problem: Maximize Array Sum After K Negations (LC 1005) | Optional | Easy
Topic: Greedy

Given an array and K, negate any element K times to maximize the sum.

Example 1:
  Input: arr = [3, -1, 0, 2], k = 3
  Output: 6  # negate -1 three times → [3,1,0,2] wait, negate -1→1, then negate 0→0, then 0→0 → sum=6

Constraints:
  - 1 <= n <= 10^4
  - 1 <= k <= 10^4

Hint: Sort. Negate smallest (most negative) first. If k remains and is odd, negate smallest positive.
Pattern: Greedy / Sorting
"""


def maximize_sum_negations(arr: list[int], k: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert maximize_sum_negations([3, -1, 0, 2], 3) == 6
    assert maximize_sum_negations([2, -3, -1, 5, -4], 2) == 13
    print("All tests passed!")
