"""
Problem: Best Time to Buy and Sell Stock (LC 121) | Day 4 | Easy
Topic: Arrays

Find the maximum profit from buying and selling a stock once.

Example 1:
  Input: prices = [7,1,5,3,6,4]
  Output: 5 (buy at 1, sell at 6)

Example 2:
  Input: prices = [7,6,4,3,1]
  Output: 0 (no profit possible)

Constraints:
  - 1 <= prices.length <= 10^5
  - 0 <= prices[i] <= 10^4

Hint: Track the minimum price seen so far.
Pattern: Greedy / Kadane's variant
"""


def max_profit(prices: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([1, 2]) == 1
    print("All tests passed!")
