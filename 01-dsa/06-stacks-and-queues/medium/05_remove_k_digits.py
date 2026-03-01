"""
Remove K Digits

Day: 21 | Difficulty: Medium | Pattern: Monotonic Stack
LeetCode 402: https://leetcode.com/problems/remove-k-digits/

Problem:
    Given string num representing a non-negative integer num, and an integer k,
    return the smallest possible integer after removing k digits from num.

Examples:
    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove 4, 3, and 2 to form "1219" which is the smallest.

    Input: num = "10200", k = 1
    Output: "200"

    Input: num = "10", k = 2
    Output: "0"

Constraints:
    - 1 <= k <= num.length <= 10^5
    - num consists of only digits
    - num does not have any leading zeroes except for the zero itself

Hint:
    Use a monotonic increasing stack. For each digit, while the stack's top is
    greater than the current digit and k > 0, pop the top (remove that digit).
    After processing, if k > 0, remove from the end. Strip leading zeros.

Pattern:
    Monotonic Stack (Increasing)
    - Greedily remove digits from left that are larger than the next digit
    - This ensures the leftmost digits are as small as possible
    - After iteration, if k > 0, remove the last k digits
    - Handle edge cases: leading zeros, result is "0"
"""


def remove_k_digits(num: str, k: int) -> str:
    pass


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Basic removal
    assert remove_k_digits("1432219", 3) == "1219", "Test 1 Failed"

    # Test 2: Leading zero after removal
    assert remove_k_digits("10200", 1) == "200", "Test 2 Failed"

    # Test 3: Remove all digits
    assert remove_k_digits("10", 2) == "0", "Test 3 Failed"

    # Test 4: Remove from end
    assert remove_k_digits("12345", 2) == "123", "Test 4 Failed"

    # Test 5: Single digit
    assert remove_k_digits("9", 1) == "0", "Test 5 Failed"

    # Test 6: Already smallest
    assert remove_k_digits("112", 1) == "11", "Test 6 Failed"

    # Test 7: Multiple leading zeros
    assert remove_k_digits("10001", 1) == "1", "Test 7 Failed"

    print("All test cases passed!")
