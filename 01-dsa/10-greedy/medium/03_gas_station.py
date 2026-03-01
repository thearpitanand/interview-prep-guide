"""
Problem: Gas Station
Day: 29 | Difficulty: Medium | Topic: Circular Greedy
Link: https://leetcode.com/problems/gas-station/

Description:
    There are n gas stations along a circular route, where the amount of gas
    at the ith station is gas[i]. You have a car with an unlimited gas tank
    and it costs cost[i] of gas to travel from the ith station to its next
    (i + 1)th station. You begin the journey with an empty tank at one of
    the gas stations.
    Given two integer arrays gas and cost, return the starting gas station's
    index if you can travel around the circuit once in the clockwise direction,
    otherwise return -1. If there exists a solution, it is guaranteed to be unique.

Examples:
    Input: gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]
    Output: 3
    Explanation: Start at station 3 (gas=4). Tank = 0+4-1 = 3.
                 Go to station 4: tank = 3+5-2 = 6.
                 Go to station 0: tank = 6+1-3 = 4.
                 Go to station 1: tank = 4+2-4 = 2.
                 Go to station 2: tank = 2+3-5 = 0. Back to station 3.

    Input: gas = [2, 3, 4], cost = [3, 4, 3]
    Output: -1

Constraints:
    - n == gas.length == cost.length
    - 1 <= n <= 10^5
    - 0 <= gas[i], cost[i] <= 10^4

Hint:
    Key insight: if total gas >= total cost, a solution exists. Track the
    current tank surplus. Whenever it drops below 0, reset the starting
    station to the next station.

Pattern: Greedy - if the cumulative tank goes negative at station i, then no
    station from current start to i can be the answer. Start fresh from i+1.
"""

from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"gas": [1, 2, 3, 4, 5], "cost": [3, 4, 5, 1, 2], "expected": 3},
        {"gas": [2, 3, 4], "cost": [3, 4, 3], "expected": -1},
        {"gas": [5, 1, 2, 3, 4], "cost": [4, 4, 1, 5, 1], "expected": 4},
        {"gas": [3, 1, 1], "cost": [1, 2, 2], "expected": 0},
        {"gas": [1], "cost": [1], "expected": 0},
        {"gas": [1, 2], "cost": [2, 1], "expected": 1},
    ]

    for i, t in enumerate(tests):
        result = can_complete_circuit(t["gas"], t["cost"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
