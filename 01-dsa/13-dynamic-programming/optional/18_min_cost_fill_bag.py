"""
Problem: Minimum Cost to Fill Bag (GFG) | Optional | Medium
Topic: Dynamic Programming

Given a bag of capacity W and N packets of different sizes and costs,
find the minimum cost to fill the bag exactly. If impossible, return -1.

Example 1:
  Input: W = 5, packets = [(1,2),(2,3),(3,4)]  # (size, cost)
  Output: 6  # two packets of size 2 + one of size 1

Constraints:
  - 1 <= W <= 10^3

Hint: Unbounded knapsack minimization variant.
Pattern: DP (Unbounded Knapsack)
"""


def min_cost_fill_bag(W: int, packets: list[tuple[int, int]]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert min_cost_fill_bag(5, [(1, 2), (2, 3), (3, 4)]) == 7  # 2+2+3 for sizes 1+1+3 or similar
    assert min_cost_fill_bag(3, [(5, 10)]) == -1
    print("All tests passed!")
