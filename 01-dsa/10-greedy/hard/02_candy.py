"""
Problem: Candy
Day: 30 | Difficulty: Hard | Topic: Greedy (Two Pass)
Link: https://leetcode.com/problems/candy/

Description:
    There are n children standing in a line. Each child is assigned a rating
    value given in the integer array ratings.
    You are giving candies to these children with the following requirements:
        - Each child must have at least one candy.
        - Children with a higher rating get more candies than their neighbors.
    Return the minimum number of candies you need to have to distribute to
    the children.

Examples:
    Input: ratings = [1, 0, 2]
    Output: 5
    Explanation: Candies = [2, 1, 2]. Child 0 has higher rating than child 1,
                 so gets more. Child 2 has higher rating than child 1, so gets more.

    Input: ratings = [1, 2, 2]
    Output: 4
    Explanation: Candies = [1, 2, 1]. Child 1 has higher rating than child 0,
                 so gets more. Child 2 has equal rating to child 1, no constraint.

Constraints:
    - n == ratings.length
    - 1 <= n <= 2 * 10^4
    - 0 <= ratings[i] <= 2 * 10^4

Hint:
    Use two passes. Left-to-right: if ratings[i] > ratings[i-1], give more
    than the left neighbor. Right-to-left: if ratings[i] > ratings[i+1],
    ensure more than the right neighbor. Take the max of both passes.

Pattern: Two-pass greedy. First pass ensures left-neighbor constraint.
    Second pass ensures right-neighbor constraint. Take max at each position.
"""

from typing import List


def candy(ratings: List[int]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"ratings": [1, 0, 2], "expected": 5},
        {"ratings": [1, 2, 2], "expected": 4},
        {"ratings": [1, 2, 3], "expected": 6},
        {"ratings": [3, 2, 1], "expected": 6},
        {"ratings": [1], "expected": 1},
        {"ratings": [1, 3, 2, 2, 1], "expected": 7},
        {"ratings": [1, 2, 87, 87, 87, 2, 1], "expected": 13},
    ]

    for i, t in enumerate(tests):
        result = candy(t["ratings"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
