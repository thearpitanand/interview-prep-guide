"""
Problem: Maximum Product Subset (GFG) | Optional | Medium
Topic: Greedy

Find the maximum product possible from a subset of the given array.

Example 1:
  Input: arr = [-1, -1, -2, 4, 3]
  Output: 24  # (-1)*(-2)*4*3 = 24

Constraints:
  - 1 <= n <= 20

Hint: Count negatives. If odd count, exclude the largest (closest to 0) negative. Handle zeros.
Pattern: Greedy
"""


def max_product_subset(arr: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_product_subset([-1, -1, -2, 4, 3]) == 24
    assert max_product_subset([0, 0, 0]) == 0
    assert max_product_subset([-1]) == -1
    print("All tests passed!")
