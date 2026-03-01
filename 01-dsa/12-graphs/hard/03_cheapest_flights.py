"""
Cheapest Flights Within K Stops (LC 787)

Day: 35 | Difficulty: Hard | Pattern: Dijkstra / Bellman-Ford

There are n cities connected by some number of flights. You are given an array
flights where flights[i] = [fromi, toi, pricei] indicates there is a flight
from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k. Return the cheapest price
from src to dst with at most k stops. If there is no such route, return -1.

Examples:
    Input: n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
           src=0, dst=3, k=1
    Output: 700
    Explanation: 0 -> 1 -> 3 costs 100 + 600 = 700 (1 stop).
                 0 -> 1 -> 2 -> 3 costs 400 but needs 2 stops.

    Input: n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=1
    Output: 200
    Explanation: 0 -> 1 -> 2 costs 200 (1 stop, within limit).

    Input: n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=0
    Output: 500
    Explanation: Only direct flights allowed (0 stops). 0 -> 2 costs 500.

Constraints:
    - 1 <= n <= 100
    - 0 <= flights.length <= n * (n - 1) / 2
    - flights[i].length == 3
    - 0 <= fromi, toi < n
    - fromi != toi
    - 1 <= pricei <= 10^4
    - No multiple flights between the same two cities
    - 0 <= src, dst, k < n
    - src != dst

Hint:
    Modified Bellman-Ford: Run k+1 rounds of relaxation (k stops = k+1 edges).
    In each round, use the distances from the PREVIOUS round (not current) to
    avoid using more edges than allowed. Alternatively, use BFS with pruning
    or modified Dijkstra with a stops counter.

Pattern: Constrained shortest path - Bellman-Ford limited to k+1 relaxation
rounds, or modified Dijkstra tracking (cost, node, stops_remaining).
"""

import heapq
from collections import defaultdict
from typing import List


def find_cheapest_price_bellman(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    """Modified Bellman-Ford with k+1 relaxation rounds."""
    pass


def find_cheapest_price_dijkstra(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    """Modified Dijkstra tracking stops remaining."""
    pass


# --- Tests ---

if __name__ == "__main__":
    # Test 1: Standard case with k=1
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    result = find_cheapest_price_bellman(4, flights, 0, 3, 1)
    assert result == 700, f"Expected 700, got {result}"

    # Test 2: Cheaper with more stops
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    result = find_cheapest_price_bellman(3, flights, 0, 2, 1)
    assert result == 200, f"Expected 200, got {result}"

    # Test 3: Direct flight only (k=0)
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    result = find_cheapest_price_bellman(3, flights, 0, 2, 0)
    assert result == 500, f"Expected 500, got {result}"

    # Test 4: No route possible
    result = find_cheapest_price_bellman(3, [[0, 1, 100]], 0, 2, 1)
    assert result == -1, f"Expected -1, got {result}"

    # Test 5: Dijkstra approach
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    result = find_cheapest_price_dijkstra(4, flights, 0, 3, 1)
    assert result == 700, f"Expected 700, got {result}"

    # Test 6: k=0, must be direct flight
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    result = find_cheapest_price_dijkstra(3, flights, 0, 2, 0)
    assert result == 500, f"Expected 500, got {result}"

    print("All tests passed!")
