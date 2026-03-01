"""
Problem: Check if Possible to Survive on Island (GFG) | Optional | Easy
Topic: Greedy

On an island, a shop is open 6 out of 7 days. You need N food items per day
for S days. You can buy at most M items per day. Can you survive?

Example 1:
  Input: S = 10, N = 16, M = 40
  Output: True, buy_days = 2

Constraints:
  - 1 <= S, N, M <= 10^6

Hint: Total needed = S*N. Available buy days = S - S//7. Check if buy_days * M >= total.
Pattern: Math / Greedy
"""


def can_survive(S: int, N: int, M: int) -> tuple[bool, int]:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = can_survive(10, 16, 40)
    assert result[0] == True
    assert can_survive(10, 20, 30)[0] == True
    print("All tests passed!")
