"""
Decode String

Day: 21 | Difficulty: Medium | Pattern: Stack
LeetCode 394: https://leetcode.com/problems/decode-string/

Problem:
    Given an encoded string, return its decoded string.

    The encoding rule is: k[encoded_string], where the encoded_string inside
    the square brackets is being repeated exactly k times. Note that k is
    guaranteed to be a positive integer.

    You may assume that the input string is always valid; there are no extra
    white spaces, square brackets are well-formed, etc. Furthermore, you may
    assume that the original data does not contain any digits and that digits
    are only for those repeat numbers, k.

Examples:
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"

    Input: s = "3[a2[c]]"
    Output: "accaccacc"

    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"

Constraints:
    - 1 <= s.length <= 30
    - s consists of lowercase English letters, digits, and square brackets '[]'
    - s is guaranteed to be a valid input
    - All the integers in s are in the range [1, 300]

Hint:
    Use a stack of (current_string, repeat_count) pairs. When you see '[',
    push the current string and current number, then reset both. When you
    see ']', pop the previous string and number, and append current_string
    repeated number times to the previous string.

Pattern:
    Nested Stack
    - Digits -> build up the current number (could be multi-digit like "12")
    - '[' -> push (current_string, current_number), reset both
    - ']' -> pop (prev_string, num), current_string = prev_string + current_string * num
    - Letter -> append to current_string
"""


def decode_string(s: str) -> str:
    pass


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Simple repeat
    assert decode_string("3[a]2[bc]") == "aaabcbc", "Test 1 Failed"

    # Test 2: Nested
    assert decode_string("3[a2[c]]") == "accaccacc", "Test 2 Failed"

    # Test 3: Mixed with plain text
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef", "Test 3 Failed"

    # Test 4: No encoding
    assert decode_string("abc") == "abc", "Test 4 Failed"

    # Test 5: Single repeat
    assert decode_string("1[a]") == "a", "Test 5 Failed"

    # Test 6: Multi-digit number
    assert decode_string("10[a]") == "aaaaaaaaaa", "Test 6 Failed"

    # Test 7: Deeply nested
    assert decode_string("2[a2[b3[c]]]") == "abcccbcccabcccbccc", "Test 7 Failed"

    print("All test cases passed!")
