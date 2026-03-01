"""
Asteroid Collision

Day: 21 | Difficulty: Medium | Pattern: Stack
LeetCode 735: https://leetcode.com/problems/asteroid-collision/

Problem:
    We are given an array asteroids of integers representing asteroids in a row.

    For each asteroid, the absolute value represents its size, and the sign
    represents its direction (positive = right, negative = left). Each asteroid
    moves at the same speed.

    Find out the state of the asteroids after all collisions. If two asteroids
    meet, the smaller one will explode. If both are the same size, both will
    explode. Two asteroids moving in the same direction will never meet.

Examples:
    Input: asteroids = [5,10,-5]
    Output: [5,10]
    Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

    Input: asteroids = [8,-8]
    Output: []
    Explanation: The 8 and -8 collide exploding each other.

    Input: asteroids = [10,2,-5]
    Output: [10]
    Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Constraints:
    - 2 <= asteroids.length <= 10^4
    - -1000 <= asteroids[i] <= 1000
    - asteroids[i] != 0

Hint:
    Use a stack. For each asteroid: if it's moving right (positive) or the stack
    is empty, push it. If it's moving left (negative) and the top of the stack
    is positive, they collide. Handle three outcomes: top explodes (pop),
    current explodes (skip), or both explode (pop and skip).

Pattern:
    Stack Simulation
    - Collision only happens when stack top is positive AND current is negative
    - Keep resolving collisions until current asteroid is destroyed or no collision
    - If current survives all collisions, push it onto the stack
"""

from typing import List


def asteroid_collision(asteroids: List[int]) -> List[int]:
    pass


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Larger survives
    assert asteroid_collision([5, 10, -5]) == [5, 10], "Test 1 Failed"

    # Test 2: Equal size both explode
    assert asteroid_collision([8, -8]) == [], "Test 2 Failed"

    # Test 3: Chain collision
    assert asteroid_collision([10, 2, -5]) == [10], "Test 3 Failed"

    # Test 4: No collision (all same direction)
    assert asteroid_collision([1, 2, 3]) == [1, 2, 3], "Test 4 Failed"

    # Test 5: No collision (negative then positive)
    assert asteroid_collision([-2, -1, 1, 2]) == [-2, -1, 1, 2], "Test 5 Failed"

    # Test 6: Multiple collisions
    assert asteroid_collision([1, -1, -2, -3]) == [-2, -3], "Test 6 Failed"

    # Test 7: Large destroys multiple
    assert asteroid_collision([5, 2, 3, -10]) == [-10], "Test 7 Failed"

    print("All test cases passed!")
