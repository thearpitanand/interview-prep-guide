"""
Reorganize String

Day: 28
Difficulty: Medium
Topic: Max Heap
Link: https://leetcode.com/problems/reorganize-string/
Pattern: Max Heap (Greedy with Priority Queue)

Description:
    Given a string s, rearrange the characters of s so that any two adjacent
    characters are not the same.

    Return any possible rearrangement of s or return "" if not possible.

Examples:
    Input: s = "aab"
    Output: "aba"

    Input: s = "aaab"
    Output: ""
    Explanation: No valid arrangement exists since 'a' appears 3 times
                 but there are only 4 characters total (need at most
                 (4+1)//2 = 2 of any character, but 'a' has 3).

Constraints:
    - 1 <= s.length <= 500
    - s consists of lowercase English letters.

Hint:
    Use a max-heap of (-count, char). Greedily pick the most frequent
    character that is NOT the same as the previous character.

    Algorithm:
    1. Count character frequencies.
    2. Check if any frequency > (len(s) + 1) // 2 -> impossible.
    3. Build a max-heap with (-count, char).
    4. Pop the most frequent char. If it matches previous, pop next most
       frequent instead, use it, then push the first one back.
    5. Repeat until heap is empty.

Pattern:
    Max Heap - Always place the character with the highest remaining count,
    ensuring it differs from the previously placed character. The heap
    naturally gives us the best candidate at each step.
"""

import heapq
from collections import Counter


def reorganize_string(s: str) -> str:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    # Helper to verify no two adjacent chars are the same
    def is_valid(result: str, original: str) -> bool:
        if result == "":
            return True  # Empty means impossible, checked separately
        if sorted(result) != sorted(original):
            return False  # Must use same characters
        for i in range(1, len(result)):
            if result[i] == result[i - 1]:
                return False
        return True

    # Test 1: Standard case
    result = reorganize_string("aab")
    assert is_valid(result, "aab"), f"Test 1 Failed: got '{result}'"

    # Test 2: Impossible case
    assert reorganize_string("aaab") == "", "Test 2 Failed"

    # Test 3: Single character
    assert reorganize_string("a") == "a", "Test 3 Failed"

    # Test 4: Two different characters
    result = reorganize_string("ab")
    assert is_valid(result, "ab"), f"Test 4 Failed: got '{result}'"

    # Test 5: All same characters
    assert reorganize_string("aaa") == "", "Test 5 Failed"

    # Test 6: Longer valid string
    result = reorganize_string("aabb")
    assert is_valid(result, "aabb"), f"Test 6 Failed: got '{result}'"

    # Test 7: Complex case
    result = reorganize_string("aaabbc")
    assert is_valid(result, "aaabbc"), f"Test 7 Failed: got '{result}'"

    # Test 8: Edge case - just barely possible
    result = reorganize_string("aabbc")
    assert is_valid(result, "aabbc"), f"Test 8 Failed: got '{result}'"

    print("All test cases passed!")
