"""
Problem: Min and Max Amount to Buy All Candies (GFG) | Optional | Easy
Topic: Greedy

A shop has N candies. When you buy one, you get up to K candies free. Find
the minimum and maximum amount to buy all candies.

Example 1:
  Input: prices = [3, 2, 1, 4], k = 2
  Output: min=3, max=7

Constraints:
  - 1 <= n <= 10^5
  - 0 <= k <= n

Hint: Sort prices. For min: buy cheapest, get most expensive free. For max: buy most expensive, get cheapest free.
Pattern: Greedy / Sorting
"""


def min_max_candies(prices: list[int], k: int) -> tuple[int, int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert min_max_candies([3, 2, 1, 4], 2) == (3, 7)
    assert min_max_candies([1, 2, 3, 4], 1) == (3, 7)
    print("All tests passed!")
