# 121 — Best Time to Buy and Sell Stock

## Problem

Track minimum price seen so far; max profit = current price minus that minimum.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)**

**Examples:**
```
prices = [7,1,5,3,6,4] -> 5
prices = [7,6,4,3,1] -> 0
```
---

## Approach 1 — Single pass greedy ✅

**Idea:** min_price tracks lowest so far. profit = price - min_price. Update both each step.

```python
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
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Kadane's variant

**Idea:** Convert to daily differences array. Max subarray sum = max profit.

```python
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = curr = 0
        for i in range(1, len(prices)):
            curr = max(0, curr + prices[i] - prices[i-1])
            max_profit = max(max_profit, curr)
        return max_profit
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Single pass greedy | O(n) | O(1) | ✅ Yes |
| 2 — Kadane's variant | O(n) | O(1) | No |

---

## Reference

[LeetCode #121 — Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
