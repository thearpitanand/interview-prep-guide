"""
Problem: Coin Game Winner (GFG) | Optional | Medium
Topic: Dynamic Programming

Two players play a coin game. N coins in a line. Each turn a player picks
1, 2, or 3 coins. The player who picks the last coin wins. Determine winner.

Example 1:
  Input: n = 5
  Output: "First"  # First picks 1, then mirror opponent's move

Constraints:
  - 1 <= n <= 10^6

Hint: If n % 4 == 0, second player wins; otherwise first player wins.
Pattern: Game Theory / DP
"""


def coin_game_winner(n: int) -> str:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert coin_game_winner(5) == "First"
    assert coin_game_winner(4) == "Second"
    assert coin_game_winner(1) == "First"
    print("All tests passed!")
