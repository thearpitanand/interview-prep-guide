"""
Problem: Regular Expression Matching
Day: 39 | Difficulty: Hard | Topic: String DP
Link: https://leetcode.com/problems/regular-expression-matching/

Description:
    Given an input string s and a pattern p, implement regular expression
    matching with support for '.' and '*' where:
    - '.' Matches any single character.
    - '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).

Examples:
    Input: s = "aa", p = "a*"
    Output: True
    Explanation: '*' means zero or more of 'a'. "a*" matches "aa".

    Input: s = "ab", p = ".*"
    Output: True
    Explanation: ".*" means zero or more of any character.

    Input: s = "aa", p = "a"
    Output: False
    Explanation: "a" does not match the entire string "aa".

Constraints:
    - 1 <= s.length <= 20
    - 1 <= p.length <= 20
    - s contains only lowercase English letters
    - p contains only lowercase English letters, '.', and '*'
    - It is guaranteed for each '*', there is a valid preceding character

Hint:
    dp[i][j] = True if s[0..i-1] matches p[0..j-1].
    Base case: dp[0][0] = True. dp[0][j] can be True if p[j-1] == '*'
    and dp[0][j-2] is True (star matches zero occurrences).
    If p[j-1] == '*':
        dp[i][j] = dp[i][j-2] (zero occurrences)
                   or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
    Else:
        dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')

Pattern: 2D string DP. Handle '*' specially -- it pairs with the character
    before it and can match zero or more of that character.
"""


def is_match(s: str, p: str) -> bool:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"s": "aa", "p": "a*", "expected": True},
        {"s": "ab", "p": ".*", "expected": True},
        {"s": "aa", "p": "a", "expected": False},
        {"s": "aab", "p": "c*a*b", "expected": True},
        {"s": "mississippi", "p": "mis*is*p*.", "expected": False},
        {"s": "", "p": "a*", "expected": True},
        {"s": "a", "p": "ab*", "expected": True},
        {"s": "aaa", "p": "a*a", "expected": True},
    ]

    for i, t in enumerate(tests):
        result = is_match(t["s"], t["p"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
