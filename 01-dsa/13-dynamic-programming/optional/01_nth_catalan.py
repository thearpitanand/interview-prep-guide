"""
Problem: Nth Catalan Number (GFG) | Optional | Easy
Topic: Dynamic Programming

Find the nth Catalan number. C(n) = sum(C(i)*C(n-1-i)) for i in 0..n-1.

Example 1:
  Input: n = 5
  Output: 42

Constraints:
  - 0 <= n <= 100

Hint: DP: C[0]=1, C[i] = sum(C[j]*C[i-1-j]).
Pattern: DP
"""


def catalan(n: int) -> int:
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    assert catalan(0) == 1
    assert catalan(5) == 42
    assert catalan(3) == 5
    print("All tests passed!")
