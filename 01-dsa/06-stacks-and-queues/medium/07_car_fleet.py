"""
Car Fleet

Day: 22 | Difficulty: Medium | Pattern: Stack / Sort
LeetCode 853: https://leetcode.com/problems/car-fleet/

Problem:
    There are n cars going to the same destination along a one-lane road.
    The destination is target miles away.

    You are given two integer arrays position and speed, both of length n,
    where position[i] is the position of the ith car and speed[i] is the
    speed of the ith car (in miles per hour).

    A car can never pass another car ahead of it, but it can catch up to it
    and drive bumper to bumper at the same speed. The faster car will slow
    down to match the slower car's speed.

    A car fleet is some non-empty set of cars driving at the same position
    and same speed. Note that a single car is also a car fleet.

    If a car catches up to a car fleet right at the destination point, it
    is still considered as one car fleet.

    Return the number of car fleets that will arrive at the destination.

Examples:
    Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
    Output: 3
    Explanation:
        - Cars at 10 (speed 2) and 8 (speed 4) become a fleet, reaching 12 at time 1.
        - Car at 0 (speed 1) does not catch anyone.
        - Cars at 5 (speed 1) and 3 (speed 3) become a fleet at position 6, then reach 12 at time 7.
        So there are 3 fleets.

    Input: target = 10, position = [3], speed = [3]
    Output: 1

Constraints:
    - n == position.length == speed.length
    - 1 <= n <= 10^5
    - 0 < target <= 10^6
    - 0 <= position[i] < target
    - 0 < speed[i] <= 10^6
    - All the values of position are unique

Hint:
    Sort cars by position in descending order (closest to target first).
    Calculate the time each car takes to reach the target. If a car behind
    takes less or equal time than the car ahead, they form a fleet.
    Use a stack: push time if it's greater than the stack top (new fleet).

Pattern:
    Stack + Sort
    - Sort by position descending (process cars closest to target first)
    - Calculate time to target: (target - position) / speed
    - If current car's time > stack top, it can't catch up -> new fleet (push)
    - If current car's time <= stack top, it merges into the fleet ahead
    - Answer = stack size = number of fleets
"""

from typing import List


def car_fleet(target: int, position: List[int], speed: List[int]) -> int:
    pass


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Multiple fleets
    assert car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3, "Test 1 Failed"

    # Test 2: Single car
    assert car_fleet(10, [3], [3]) == 1, "Test 2 Failed"

    # Test 3: All become one fleet
    assert car_fleet(100, [0, 2, 4], [4, 2, 1]) == 1, "Test 3 Failed"

    # Test 4: No merging
    assert car_fleet(10, [0, 4, 2], [1, 1, 1]) == 3, "Test 4 Failed"

    # Test 5: Two cars merging at target
    assert car_fleet(10, [6, 8], [3, 2]) == 2, "Test 5 Failed"

    # Test 6: Empty
    assert car_fleet(10, [], []) == 0, "Test 6 Failed"

    print("All test cases passed!")
