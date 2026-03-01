"""
Problem: Fractional Knapsack (GFG) | Day 30 | Medium
Topic: Greedy

Given weights and values of N items, put them in a knapsack of capacity W.
You can break items (take fractions). Maximize total value.

Example 1:
  Input: items = [(60,10), (100,20), (120,30)], W = 50
  Output: 240.0  # Take full item2(100) + full item1(60) + 2/3 of item3(80) = 240

Constraints:
  - 1 <= n <= 10^5
  - 1 <= W <= 10^9

Hint: Sort by value/weight ratio in decreasing order. Greedily pick items.
Pattern: Greedy (Value Density)
"""


def fractional_knapsack(items: list[tuple[int, int]], W: int) -> float:
    # items = list of (value, weight)
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert fractional_knapsack([(60, 10), (100, 20), (120, 30)], 50) == 240.0
    assert fractional_knapsack([(500, 30)], 10) == 500 / 3 * 1  # ~166.67
    print("All tests passed!")
