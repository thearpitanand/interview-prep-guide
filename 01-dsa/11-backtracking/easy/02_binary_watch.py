"""
Binary Watch (LC 401)

Day: 31 | Difficulty: Easy | Pattern: Backtracking

A binary watch has 4 LEDs on the top to represent hours (0-11) and 6 LEDs on
the bottom to represent minutes (0-59). Each LED represents a zero or one,
with the least significant bit on the right.

Given an integer turnedOn which represents the number of LEDs that are currently
on (ignoring the PM), return all possible times the watch could represent.
Return the answer in any order.

The hour must not have a leading zero (e.g., "01:00" is invalid, use "1:00").
The minute must have two digits and may have a leading zero (e.g., "10:02").

Examples:
    Input: turnedOn = 1
    Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

    Input: turnedOn = 9
    Output: [] (impossible, not enough bits)

Constraints:
    - 0 <= turnedOn <= 10

Hint:
    There are only 10 LEDs total (4 for hours, 6 for minutes). You can use
    backtracking to choose which turnedOn LEDs to turn on from the 10 available.
    Alternatively, enumerate all (hour, minute) pairs and count bits.

Pattern: Backtracking - choose which LEDs to turn on, or enumerate all valid
hour/minute combinations and filter by bit count.
"""

from typing import List


def read_binary_watch(turned_on: int) -> List[str]:
    """Return all possible times with the given number of LEDs on using backtracking."""
    pass


def read_binary_watch_enumeration(turned_on: int) -> List[str]:
    """Simpler approach: enumerate all hours and minutes, count set bits."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: One LED on
    result = sorted(read_binary_watch(1))
    expected = sorted(["0:01", "0:02", "0:04", "0:08", "0:16", "0:32",
                       "1:00", "2:00", "4:00", "8:00"])
    assert result == expected, f"Expected {expected}, got {result}"

    # Test 2: Zero LEDs on
    result = read_binary_watch(0)
    assert result == ["0:00"], f"Expected ['0:00'], got {result}"

    # Test 3: Impossible (9 LEDs)
    result = read_binary_watch(9)
    assert result == [], f"Expected [], got {result}"

    # Test 4: Two LEDs on (check a few expected values)
    result = sorted(read_binary_watch(2))
    assert "0:03" in result, f"Expected '0:03' in result"
    assert "1:01" in result, f"Expected '1:01' in result"
    assert "3:00" in result, f"Expected '3:00' in result"

    # Test 5: Enumeration approach
    result = sorted(read_binary_watch_enumeration(1))
    expected = sorted(["0:01", "0:02", "0:04", "0:08", "0:16", "0:32",
                       "1:00", "2:00", "4:00", "8:00"])
    assert result == expected, f"Expected {expected}, got {result}"

    print("All tests passed!")
