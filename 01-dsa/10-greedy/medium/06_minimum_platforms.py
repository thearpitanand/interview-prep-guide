"""
Problem: Minimum Platforms
Day: 30 | Difficulty: Medium | Topic: Greedy + Sort
Link: GeeksforGeeks Classic

Description:
    Given arrival and departure times of all trains that reach a railway
    station, find the minimum number of platforms required for the railway
    station so that no train is kept waiting.
    At any given instance of time, the same platform cannot be used for both
    departure of a train and arrival of another train. In such cases, we need
    different platforms.

Examples:
    Input: arr = [900, 940, 950, 1100, 1500, 1800],
           dep = [910, 1200, 1120, 1130, 1900, 2000]
    Output: 3
    Explanation: At time 950, trains arriving at 940 and 950 are still at
                 the station (departing at 1200 and 1120). At time 1100,
                 all three overlap. Maximum overlap = 3.

    Input: arr = [900, 1100, 1235],
           dep = [1000, 1200, 1240]
    Output: 1

Constraints:
    - 1 <= n <= 10^5
    - Times are in 24-hour format (HHMM as integers)
    - arr[i] <= dep[i] for all i

Hint:
    Sort arrivals and departures separately. Use two pointers to simulate
    events in chronological order. When an arrival comes before a departure,
    a new platform is needed. When a departure comes, a platform is freed.

Pattern: Sort + sweep line. Sort arrivals and departures independently. Use
    two pointers to track current platforms needed. Track maximum.
"""

from typing import List


def minimum_platforms(arr: List[int], dep: List[int]) -> int:
    pass


# ---- Test Cases ----
if __name__ == "__main__":
    tests = [
        {
            "arr": [900, 940, 950, 1100, 1500, 1800],
            "dep": [910, 1200, 1120, 1130, 1900, 2000],
            "expected": 3,
        },
        {
            "arr": [900, 1100, 1235],
            "dep": [1000, 1200, 1240],
            "expected": 1,
        },
        {
            "arr": [900, 940],
            "dep": [910, 1200],
            "expected": 1,
        },
        {
            "arr": [100, 200, 300, 400],
            "dep": [500, 600, 700, 800],
            "expected": 4,
        },
        {
            "arr": [900],
            "dep": [1000],
            "expected": 1,
        },
    ]

    for i, t in enumerate(tests):
        result = minimum_platforms(t["arr"], t["dep"])
        status = "PASS" if result == t["expected"] else "FAIL"
        print(f"Test {i+1}: {status} | Expected: {t['expected']}, Got: {result}")
