"""
Problem: Minimum Coins for Change (GFG) | Day 29 | Easy
Topic: Greedy

Given coins of denominations and a target amount, find the minimum number
of coins needed (greedy approach works for standard denominations like Indian currency).

Example 1:
  Input: coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000], amount = 93
  Output: 5  # 50+20+20+2+1

Constraints:
  - Standard denominations (greedy is optimal)

Hint: Greedy: pick largest denomination first, subtract, repeat.
Pattern: Greedy
"""


def min_coins(coins: list[int], amount: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    assert min_coins(coins, 93) == 5
    assert min_coins(coins, 1000) == 1
    assert min_coins(coins, 0) == 0
    print("All tests passed!")
