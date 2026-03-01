"""
Problem: Max Difference of Zeros and Ones (GFG) | Optional | Easy
Topic: Dynamic Programming

Given a binary string, find the maximum difference between count of 0s and 1s
in any substring (count of 0s - count of 1s).

Example 1:
  Input: s = "11000010001"
  Output: 6

Constraints:
  - 1 <= len(s) <= 10^5

Hint: Convert: 0→+1, 1→-1. Find max subarray sum (Kadane's).
Pattern: Kadane's Algorithm
"""


def max_diff_zeros_ones(s: str) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_diff_zeros_ones("11000010001") == 6
    assert max_diff_zeros_ones("111") == -1
    assert max_diff_zeros_ones("000") == 3
    print("All tests passed!")
