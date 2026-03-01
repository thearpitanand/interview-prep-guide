"""
Problem: Rearrange Alternating Positive & Negative (GFG) | Optional | Easy
Topic: Arrays

Given an array of positive and negative numbers, arrange them in alternate
fashion: positive at even indices, negative at odd indices (or vice versa).
If extra positives/negatives remain, append them at the end.

Example 1:
  Input: arr = [1, 2, 3, -4, -1, 4]
  Output: [-4, 1, -1, 2, 3, 4] (or any valid alternating arrangement)

Constraints:
  - 1 <= n <= 10^6

Hint: Separate positives and negatives, then interleave.
Pattern: Array Rearrangement
"""


def rearrange_alternate(arr: list[int]) -> list[int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = rearrange_alternate([1, 2, 3, -4, -1, 4])
    # Verify alternating pattern as much as possible
    assert len(result) == 6
    print("All tests passed!")
