from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Single Pass Greedy (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

# ─────────────────────────────────────────────────
# APPROACH 2: Kadane's Variant (Max Subarray on Differences)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = curr = 0
        for i in range(1, len(prices)):
            curr = max(0, curr + prices[i] - prices[i-1])
            max_profit = max(max_profit, curr)
        return max_profit
