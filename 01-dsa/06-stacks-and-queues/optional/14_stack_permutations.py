"""
Problem: Stack Permutations (GFG) | Optional | Medium
Topic: Stacks and Queues

Given two arrays of unique elements, check if the second array is a valid
stack permutation of the first (using push/pop on a single stack).

Example 1:
  Input: input = [1, 2, 3], output = [2, 1, 3]
  Output: True

Constraints:
  - 1 <= n <= 10^3

Hint: Simulate: push from input, pop when top matches expected output.
Pattern: Stack Simulation
"""


def is_stack_permutation(inp: list[int], out: list[int]) -> bool:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert is_stack_permutation([1, 2, 3], [2, 1, 3]) == True
    assert is_stack_permutation([1, 2, 3], [3, 1, 2]) == False
    print("All tests passed!")
