"""
Problem: Smallest Number with n Trailing Zeroes (GFG) | Optional | Medium
Topic: Searching and Sorting

Given a number n, find the smallest number whose factorial has at least n trailing zeroes.

Example 1:
  Input: n = 1
  Output: 5  # 5! = 120 has 1 trailing zero

Constraints:
  - 1 <= n <= 10^4

Hint: Binary search on answer. Count trailing zeros via floor(x/5) + floor(x/25) + ...
Pattern: Binary Search on Answer
"""


def smallest_with_n_trailing_zeroes(n: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert smallest_with_n_trailing_zeroes(1) == 5
    assert smallest_with_n_trailing_zeroes(2) == 10
    assert smallest_with_n_trailing_zeroes(6) == 25
    print("All tests passed!")
