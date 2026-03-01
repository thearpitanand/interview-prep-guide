"""
Problem: Binomial Coefficient (GFG) | Optional | Easy
Topic: Dynamic Programming

Compute C(n, k) = n! / (k! * (n-k)!).

Example 1:
  Input: n = 5, k = 2
  Output: 10

Constraints:
  - 0 <= k <= n <= 1000

Hint: Pascal's triangle: C[i][j] = C[i-1][j-1] + C[i-1][j].
Pattern: DP (Pascal's Triangle)
"""


def binomial(n: int, k: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert binomial(5, 2) == 10
    assert binomial(10, 0) == 1
    assert binomial(10, 10) == 1
    print("All tests passed!")
