"""
Online Stock Span

Day: 22 | Difficulty: Medium | Pattern: Monotonic Stack
LeetCode 901: https://leetcode.com/problems/online-stock-span/

Problem:
    Design an algorithm that collects daily price quotes for some stock and
    returns the span of that stock's price for the current day.

    The span of the stock's price in one day is the maximum number of
    consecutive days (starting from that day and going backward) for which
    the stock price was less than or equal to that day's price.

    For example, if the prices of the stock in the last four days is [7,2,1,2]
    and the price of the stock today is 2, then the span of today is 4 because
    starting from today, the price of the stock was less than or equal 2 for
    4 consecutive days.

    Also, if the prices of the stock in the last four days is [7,34,1,2] and
    the price of the stock today is 8, then the span of today is 3 because
    starting from today, the price of the stock was less than or equal 8 for
    3 consecutive days.

Examples:
    Input: prices = [100, 80, 60, 70, 60, 75, 85]
    Output: spans = [1, 1, 1, 2, 1, 4, 6]

Constraints:
    - 1 <= price <= 10^5
    - At most 10^4 calls will be made to next

Hint:
    Use a monotonic decreasing stack that stores (price, span) pairs. When a
    new price comes in, pop all entries with price <= current price and
    accumulate their spans. Push the current price with the accumulated span.

Pattern:
    Monotonic Stack (Decreasing)
    - Stack stores (price, span) in decreasing order of price
    - When new price >= stack top price, pop and add span to current span
    - This efficiently computes how many consecutive previous days had
      price <= today's price
    - Each element is pushed and popped at most once -> amortized O(1)
"""


class StockSpanner:
    def __init__(self):
        pass

    def next(self, price: int) -> int:
        pass


# -------------------- Test Cases --------------------

if __name__ == "__main__":
    # Test 1: Example from problem
    spanner = StockSpanner()
    results = []
    for price in [100, 80, 60, 70, 60, 75, 85]:
        results.append(spanner.next(price))
    assert results == [1, 1, 1, 2, 1, 4, 6], f"Test 1 Failed: {results}"

    # Test 2: All increasing
    spanner2 = StockSpanner()
    results2 = []
    for price in [1, 2, 3, 4, 5]:
        results2.append(spanner2.next(price))
    assert results2 == [1, 2, 3, 4, 5], f"Test 2 Failed: {results2}"

    # Test 3: All decreasing
    spanner3 = StockSpanner()
    results3 = []
    for price in [5, 4, 3, 2, 1]:
        results3.append(spanner3.next(price))
    assert results3 == [1, 1, 1, 1, 1], f"Test 3 Failed: {results3}"

    # Test 4: All same
    spanner4 = StockSpanner()
    results4 = []
    for price in [3, 3, 3, 3]:
        results4.append(spanner4.next(price))
    assert results4 == [1, 2, 3, 4], f"Test 4 Failed: {results4}"

    # Test 5: Single element
    spanner5 = StockSpanner()
    assert spanner5.next(42) == 1, "Test 5 Failed"

    print("All test cases passed!")
