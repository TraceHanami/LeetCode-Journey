# 121 — Best Time to Buy and Sell Stock

## Problem

Track minimum price seen so far; max profit = current price minus that minimum.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)**

---

## Approach 1 — Single pass greedy ✅

**Idea:** min_price tracks lowest so far. profit = price - min_price. Update both each step.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Kadane's variant

**Idea:** Convert to daily differences array. Max subarray sum = max profit.

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
