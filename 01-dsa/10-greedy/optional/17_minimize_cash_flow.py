"""
Problem: Minimize Cash Flow Among Friends (GFG) | Optional | Hard
Topic: Greedy

Given a group of friends who owe each other money, minimize the total number
of transactions to settle all debts.

Example 1:
  Input: graph = [[0,1000,2000],[0,0,5000],[0,0,0]]
  Output: minimized transactions

Constraints:
  - 1 <= n <= 100

Hint: Compute net balance for each person. Max creditor pays max debtor.
Pattern: Greedy
"""


def minimize_cash_flow(graph: list[list[int]]) -> list[tuple[int, int, int]]:
    # Returns list of (from, to, amount) transactions
    # Write your solution here
    pass


# --- Tests ---
if __name__ == "__main__":
    result = minimize_cash_flow([[0,1000,2000],[0,0,5000],[0,0,0]])
    # Total flow should equal net balances
    assert len(result) >= 1
    print("All tests passed!")
