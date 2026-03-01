"""
Problem: Assign Cookies
Day: 29 | Difficulty: Easy | Topic: Greedy + Sort
Link: https://leetcode.com/problems/assign-cookies/

Description:
    Assume you are an awesome parent and want to give your children some cookies.
    Each child i has a greed factor g[i], which is the minimum size of a cookie
    that the child will be content with. Each cookie j has a size s[j].
    If s[j] >= g[i], we can assign cookie j to child i, and the child will be content.
    Maximize the number of content children.

Examples:
    Input: g = [1, 2, 3], s = [1, 1]
    Output: 1
    Explanation: Child with greed 1 gets a size-1 cookie. Only 1 child is content.

    Input: g = [1, 2], s = [1, 2, 3]
    Output: 2
    Explanation: Both children can be satisfied.

Constraints:
    - 1 <= g.length <= 3 * 10^4
    - 0 <= s.length <= 3 * 10^4
    - 1 <= g[i], s[j] <= 2^31 - 1

Hint:
    Sort both arrays. Use two pointers - try to satisfy the least greedy child
    with the smallest sufficient cookie.

Pattern: Sort both arrays, then use two pointers to greedily match smallest
    cookie to least greedy child.
"""

from typing import List


def find_content_children(g: List[int], s: List[int]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"g": [1, 2, 3], "s": [1, 1], "expected": 1},
        {"g": [1, 2], "s": [1, 2, 3], "expected": 2},
        {"g": [1, 2, 3], "s": [3], "expected": 1},
        {"g": [10, 9, 8, 7], "s": [5, 6, 7, 8], "expected": 2},
        {"g": [], "s": [1, 2, 3], "expected": 0},
        {"g": [1, 2, 3], "s": [], "expected": 0},
    ]

    for i, t in enumerate(tests):
        result = find_content_children(t["g"], t["s"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
