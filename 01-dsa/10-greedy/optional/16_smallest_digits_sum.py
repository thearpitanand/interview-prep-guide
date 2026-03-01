"""
Problem: Smallest Number with Given Digits and Sum (GFG) | Optional | Medium
Topic: Greedy

Find the smallest number with given number of digits and digit sum.

Example 1:
  Input: digits = 2, sum = 9
  Output: 18

Constraints:
  - 1 <= digits <= 100
  - 1 <= sum <= 900

Hint: Greedily assign 9s from right. First digit gets remainder (at least 1).
Pattern: Greedy
"""


def smallest_number(digits: int, s: int) -> str:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert smallest_number(2, 9) == "18"
    assert smallest_number(3, 20) == "299"
    print("All tests passed!")
