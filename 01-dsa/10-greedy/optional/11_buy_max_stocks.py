"""
Problem: Buy Max Stocks (GFG) | Optional | Medium
Topic: Greedy

Given stock prices for N days and a budget K, on day i you can buy at most i
stocks at price[i] each. Find max stocks you can buy.

Example 1:
  Input: prices = [10, 7, 19], k = 45
  Output: 4  # Day2: buy 2 at 7 each (14), Day1: buy 1 at 10 (10), Day3: buy 1 at 19 (19) → total=43, stocks=4

Constraints:
  - 1 <= n <= 10^3

Hint: Sort by price. Greedily buy from cheapest day, up to day-limit.
Pattern: Greedy / Sorting
"""


def buy_max_stocks(prices: list[int], k: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert buy_max_stocks([10, 7, 19], 45) == 4
    assert buy_max_stocks([7, 10, 4], 100) == 6
    print("All tests passed!")
