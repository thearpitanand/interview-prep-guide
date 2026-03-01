"""
Problem: Find Max and Min Element in Array (GFG) | Optional | Easy
Topic: Arrays

Find the maximum and minimum element in an array using minimum comparisons.

Example 1:
  Input: arr = [3, 5, 4, 1, 9]
  Output: (1, 9)

Constraints:
  - 1 <= n <= 10^5

Hint: Tournament method — compare in pairs to reduce comparisons.
Pattern: Divide and Conquer
"""


def find_max_min(arr: list[int]) -> tuple[int, int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert find_max_min([3, 5, 4, 1, 9]) == (1, 9)
    assert find_max_min([1]) == (1, 1)
    assert find_max_min([2, 1]) == (1, 2)
    print("All tests passed!")
