"""
Problem: Best Time to Buy and Sell Stock (LC 121) | Smart-DSA Day 8 | Easy
Pattern: Sliding Window (Single pass)
Time target: 15 minutes

You are given an array prices where prices[i] is the price of a stock on day i.
Maximize your profit by choosing a single day to buy and a later day to sell.
Return the maximum profit; return 0 if no profit is possible.

Example 1:
  Input: prices = [7, 1, 5, 3, 6, 4]
  Output: 5  (buy at 1, sell at 6)

Example 2:
  Input: prices = [7, 6, 4, 3, 1]
  Output: 0

Constraints:
  - 1 <= prices.length <= 10^5
  - 0 <= prices[i] <= 10^4

Hint (⚠ read only after time budget is blown):
  Track the running minimum price seen so far. At each step, compare
  current price minus running min to the best profit seen so far.
"""


def max_profit(prices: list[int]) -> int:
    pass


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([1, 2]) == 1
    assert max_profit([2, 4, 1]) == 2
    print("All tests passed!")
