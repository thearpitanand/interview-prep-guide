"""
Problem: Partition Labels
Day: 30 | Difficulty: Medium | Topic: Greedy
Link: https://leetcode.com/problems/partition-labels/

Description:
    You are given a string s. We want to partition the string into as many
    parts as possible so that each letter appears in at most one part.
    Note that the partition is done so that after concatenating all the parts
    in order, the resultant string should be s.
    Return a list of integers representing the size of these parts.

Examples:
    Input: s = "ababcbacadefegdehijhklij"
    Output: [9, 7, 8]
    Explanation: The partition is "ababcbaca", "defegde", "hijhklij".
                 Each letter appears in at most one part.

    Input: s = "eccbbbbdec"
    Output: [10]

Constraints:
    - 1 <= s.length <= 500
    - s consists of lowercase English letters

Hint:
    First, find the last occurrence of each character. Then iterate through
    the string, tracking the farthest last occurrence of any character seen
    so far. When the current index equals this farthest point, you've found
    a partition boundary.

Pattern: Greedy - extend the current partition to include the last occurrence
    of every character encountered. Cut when current index reaches the boundary.
"""


from typing import List


def partition_labels(s: str) -> List[int]:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"s": "ababcbacadefegdehijhklij", "expected": [9, 7, 8]},
        {"s": "eccbbbbdec", "expected": [10]},
        {"s": "abc", "expected": [1, 1, 1]},
        {"s": "a", "expected": [1]},
        {"s": "abab", "expected": [4]},
        {"s": "caedbdedda", "expected": [1, 9]},
    ]

    for i, t in enumerate(tests):
        result = partition_labels(t["s"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
