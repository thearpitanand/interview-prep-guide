"""
Problem: Edit Distance
Day: 39 | Difficulty: Hard | Topic: String DP
Link: https://leetcode.com/problems/edit-distance/

Description:
    Given two strings word1 and word2, return the minimum number of
    operations required to convert word1 to word2. You have the following
    three operations permitted on a word:
    - Insert a character
    - Delete a character
    - Replace a character

Examples:
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation: horse -> rorse (replace h with r) -> rose (remove r)
    -> ros (remove e)

    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation: intention -> inention (remove t) -> enention (replace i with e)
    -> exention (replace n with x) -> exection (replace n with c)
    -> execution (insert u)

Constraints:
    - 0 <= word1.length, word2.length <= 500
    - word1 and word2 consist of lowercase English letters

Hint:
    dp[i][j] = min operations to convert word1[0..i-1] to word2[0..j-1].
    Base cases: dp[i][0] = i (delete all), dp[0][j] = j (insert all).
    If word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1] (no cost).
    Else: dp[i][j] = 1 + min(dp[i-1][j-1] (replace),
                              dp[i-1][j] (delete),
                              dp[i][j-1] (insert))

Pattern: Classic 2D string DP. Three operations map to three directions in
    the DP table: diagonal (replace), up (delete), left (insert).
"""


def min_distance(word1: str, word2: str) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"word1": "horse", "word2": "ros", "expected": 3},
        {"word1": "intention", "word2": "execution", "expected": 5},
        {"word1": "", "word2": "", "expected": 0},
        {"word1": "abc", "word2": "", "expected": 3},
        {"word1": "", "word2": "abc", "expected": 3},
        {"word1": "abc", "word2": "abc", "expected": 0},
        {"word1": "a", "word2": "b", "expected": 1},
        {"word1": "dinitrophenylhydrazine", "word2": "acetylaminophenol", "expected": 14},
    ]

    for i, t in enumerate(tests):
        result = min_distance(t["word1"], t["word2"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
