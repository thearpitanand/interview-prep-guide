"""
Problem: Interleaving String
Day: 39 | Difficulty: Hard | Topic: 2D DP
Link: https://leetcode.com/problems/interleaving-string/

Description:
    Given strings s1, s2, and s3, find whether s3 is formed by an
    interleaving of s1 and s2. An interleaving of two strings s and t uses
    all characters of s and t while preserving their individual left-to-right
    order.

Examples:
    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
    Output: True

    Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
    Output: False

    Input: s1 = "", s2 = "", s3 = ""
    Output: True

Constraints:
    - 0 <= s1.length, s2.length <= 100
    - 0 <= s3.length <= 200
    - s1, s2, and s3 consist of lowercase English letters

Hint:
    If len(s1) + len(s2) != len(s3), return False immediately.
    dp[i][j] = True if s3[0..i+j-1] can be formed by interleaving
    s1[0..i-1] and s2[0..j-1].
    dp[0][0] = True.
    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or
               (dp[i][j-1] and s2[j-1] == s3[i+j-1])
    We either take the next char from s1 or from s2.

Pattern: 2D boolean DP on two strings. dp[i][j] represents matching
    i chars from s1 and j chars from s2 against s3. Can be space-optimized
    to O(n) using a 1D array.
"""


def is_interleave(s1: str, s2: str, s3: str) -> bool:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"s1": "aabcc", "s2": "dbbca", "s3": "aadbbcbcac", "expected": True},
        {"s1": "aabcc", "s2": "dbbca", "s3": "aadbbbaccc", "expected": False},
        {"s1": "", "s2": "", "s3": "", "expected": True},
        {"s1": "a", "s2": "", "s3": "a", "expected": True},
        {"s1": "", "s2": "b", "s3": "b", "expected": True},
        {"s1": "a", "s2": "b", "s3": "ab", "expected": True},
        {"s1": "a", "s2": "b", "s3": "ba", "expected": True},
        {"s1": "a", "s2": "b", "s3": "c", "expected": False},
    ]

    for i, t in enumerate(tests):
        result = is_interleave(t["s1"], t["s2"], t["s3"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
