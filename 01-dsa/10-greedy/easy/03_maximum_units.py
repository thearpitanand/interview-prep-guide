"""
Problem: Maximum Units on a Truck
Day: 29 | Difficulty: Easy | Topic: Greedy + Sort
Link: https://leetcode.com/problems/maximum-units-on-a-truck/

Description:
    You are assigned to put some amount of boxes onto one truck. You are
    given a 2D array boxTypes where boxTypes[i] = [numberOfBoxes_i, numberOfUnitsPerBox_i]:
        - numberOfBoxes_i is the number of boxes of type i
        - numberOfUnitsPerBox_i is the number of units in each box of type i
    You are also given an integer truckSize, which is the maximum number of
    boxes that can be put on the truck. Return the maximum total number of
    units that can be put on the truck.

Examples:
    Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
    Output: 8
    Explanation: Take all 1 box of type 1 (3 units), all 2 boxes of type 2
                 (4 units), and 1 box of type 3 (1 unit). Total = 3+4+1 = 8.

    Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
    Output: 91

Constraints:
    - 1 <= boxTypes.length <= 1000
    - 1 <= numberOfBoxes_i, numberOfUnitsPerBox_i <= 1000
    - 1 <= truckSize <= 10^6

Hint:
    Sort box types by units per box in descending order. Greedily pick boxes
    with the most units per box first until the truck is full.

Pattern: Sort by value (units per box) descending, greedily take as many of
    the highest-value boxes as possible.
"""

from typing import List


def maximum_units(boxTypes: List[List[int]], truckSize: int) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {"boxTypes": [[1, 3], [2, 2], [3, 1]], "truckSize": 4, "expected": 8},
        {"boxTypes": [[5, 10], [2, 5], [4, 7], [3, 9]], "truckSize": 10, "expected": 91},
        {"boxTypes": [[1, 1]], "truckSize": 1, "expected": 1},
        {"boxTypes": [[2, 1], [3, 1], [4, 1]], "truckSize": 100, "expected": 9},
        {"boxTypes": [[10, 100]], "truckSize": 5, "expected": 500},
    ]

    for i, t in enumerate(tests):
        result = maximum_units(t["boxTypes"], t["truckSize"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
