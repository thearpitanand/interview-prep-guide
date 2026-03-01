"""
Problem: Lemonade Change
Day: 29 | Difficulty: Easy | Topic: Greedy
Link: https://leetcode.com/problems/lemonade-change/

Description:
    At a lemonade stand, each lemonade costs $5. Customers stand in a queue
    and order one at a time. Each customer pays with a $5, $10, or $20 bill.
    You must provide the correct change to each customer so that the net
    transaction is that they pay $5. You start with no change.
    Return True if you can provide every customer with correct change.

Examples:
    Input: bills = [5, 5, 5, 10, 20]
    Output: True
    Explanation: First 3 give $5 (no change). 4th gives $10, change $5.
                 5th gives $20, change $10 + $5.

    Input: bills = [5, 5, 10, 10, 20]
    Output: False
    Explanation: For the last customer ($20), we need $15 change but only
                 have one $10 and one $5.

Constraints:
    - 1 <= bills.length <= 10^5
    - bills[i] is either 5, 10, or 20

Hint:
    Track the count of $5 and $10 bills. For $20, prefer giving one $10 + one $5
    over three $5 bills (greedy: preserve $5 bills since they are more flexible).

Pattern: Greedy simulation - always prefer to give larger bills as change to
    preserve smaller, more flexible bills.
"""

from typing import List


def lemonade_change(bills: List[int]) -> bool:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"bills": [5, 5, 5, 10, 20], "expected": True},
        {"bills": [5, 5, 10, 10, 20], "expected": False},
        {"bills": [5, 5, 10], "expected": True},
        {"bills": [10], "expected": False},
        {"bills": [5], "expected": True},
        {"bills": [5, 5, 5, 5, 10, 5, 10, 10, 10, 20], "expected": True},
        {"bills": [5, 5, 5, 10, 5, 5, 10, 20, 20, 20], "expected": False},
    ]

    for i, t in enumerate(tests):
        result = lemonade_change(t["bills"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
