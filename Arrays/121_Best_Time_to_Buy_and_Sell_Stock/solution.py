from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Track Minimum Seen So Far
# Why: Only need to remember the lowest price so far and check the profit if selling today.
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        best = 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > best:
                best = p - min_price
        return best


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        best_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            best_profit = max(best_profit, price - min_price)
        return best_profit

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
