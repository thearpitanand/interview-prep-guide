"""
Problem: Coin Change (LC 322) | Smart-DSA Day 43 | Medium
Pattern: Dynamic Programming — Unbounded Knapsack
Time target: 30 minutes

You are given an integer array coins representing coin denominations and an
integer amount. Return the fewest number of coins needed to make up that
amount. If no combination can make amount, return -1. You may use each
coin denomination an unlimited number of times.

Example 1:
  Input: coins = [1, 5, 11], amount = 15
  Output: 3  (11 + 3×1 would be 4; but 5+5+5 = 3 coins — wait, no 5+5+5=15 ✓)

Example 2:
  Input: coins = [2], amount = 3
  Output: -1

Example 3:
  Input: coins = [1], amount = 0
  Output: 0

Constraints:
  - 1 <= coins.length <= 12
  - 1 <= coins[i] <= 2^31 - 1
  - 0 <= amount <= 10^4

Hint (⚠ read only after time budget is blown):
  Build dp[0..amount]. dp[0] = 0, rest = infinity. For each amount i,
  try every coin c where c <= i: dp[i] = min(dp[i], dp[i - c] + 1).
  Answer is dp[amount] if finite, else -1. This is unbounded because
  you re-use coins — the coin loop is not bounded by an "items used" axis.
"""


def coin_change(coins: list[int], amount: int) -> int:
    pass


if __name__ == "__main__":
    assert coin_change([1, 5, 11], 15) == 3   # 5 + 5 + 5
    assert coin_change([1, 5, 11], 11) == 1   # 11
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([1, 2, 5], 11) == 3    # 5 + 5 + 1
    print("All tests passed!")
