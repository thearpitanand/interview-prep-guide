"""
Problem: Gas Station (LC 134) | Smart-DSA Day 47 | Medium
Pattern: Greedy
Time target: 25 minutes

There are n gas stations arranged in a circle. You are given two arrays:
  - gas[i]: gas you can collect at station i
  - cost[i]: gas needed to travel from station i to station i+1

Return the starting station index from which you can complete the full circuit
once in the clockwise direction, or -1 if it is not possible. The solution is
guaranteed to be unique if it exists.

Example 1:
  Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
  Output: 3

Example 2:
  Input: gas = [2,3,4], cost = [3,4,3]
  Output: -1

Constraints:
  - n == gas.length == cost.length
  - 1 <= n <= 10^5
  - 0 <= gas[i], cost[i] <= 10^4

Hint (⚠ read only after time budget is blown):
  Key insight: if sum(gas) >= sum(cost), a solution always exists.
  Track current tank. Whenever it goes negative, reset start to i+1 and
  reset tank to 0 — the current candidate starting point is invalid.
  After one pass, return the candidate start (guaranteed valid if total
  surplus >= 0, otherwise -1).
"""


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    pass


if __name__ == "__main__":
    assert can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert can_complete_circuit([2, 3, 4], [3, 4, 3]) == -1
    assert can_complete_circuit([5], [4]) == 0
    assert can_complete_circuit([1, 2], [2, 1]) == 1
    print("All tests passed!")
