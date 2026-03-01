"""
Problem: Max Sum Possible Equal Sum of Three Stacks (GFG) | Optional | Easy
Topic: Greedy

Given three stacks of positive numbers, find the maximum possible equal sum
of the three stacks (remove from top until equal).

Example 1:
  Input: s1 = [3, 2, 1, 1, 1], s2 = [4, 3, 2], s3 = [1, 1, 4, 1]
  Output: 5

Constraints:
  - 1 <= n1, n2, n3 <= 10^5

Hint: Compute prefix sums. Decrease the largest sum by removing top element.
Pattern: Greedy
"""


def max_equal_sum(s1: list[int], s2: list[int], s3: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_equal_sum([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1]) == 5
    assert max_equal_sum([1], [1], [1]) == 1
    print("All tests passed!")
