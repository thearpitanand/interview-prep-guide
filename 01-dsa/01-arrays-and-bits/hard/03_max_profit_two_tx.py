"""
Problem: Best Time to Buy and Sell Stock III (LC 123) | Day 6 | Hard
Topic: Arrays

Find the maximum profit with at most two transactions.

Example 1:
  Input: prices = [3,3,5,0,0,3,1,4]
  Output: 6 (buy at 0, sell at 3, buy at 1, sell at 4)

Example 2:
  Input: prices = [1,2,3,4,5]
  Output: 4

Hint: Track states: buy1, sell1, buy2, sell2.
Pattern: State Machine / DP
"""


def max_profit(prices: list[int]) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert max_profit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert max_profit([1, 2, 3, 4, 5]) == 4
    assert max_profit([7, 6, 4, 3, 1]) == 0
    print("All tests passed!")
