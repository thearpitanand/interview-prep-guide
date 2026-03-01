"""
Problem: Maximize Sum of arr[i]*i (GFG) | Optional | Easy
Topic: Greedy

Given an array, rearrange elements to maximize sum of arr[i]*i.

Example 1:
  Input: arr = [1, 2, 3, 4]
  Output: 20  # sorted: [1,2,3,4], sum = 0*1+1*2+2*3+3*4 = 20

Constraints:
  - 1 <= n <= 10^5

Hint: Sort in ascending order so largest values are multiplied by largest indices.
Pattern: Greedy / Sorting
"""


def maximize_sum(arr: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert maximize_sum([1, 2, 3, 4]) == 20
    assert maximize_sum([5, 3, 2, 4, 1]) == 40
    print("All tests passed!")
