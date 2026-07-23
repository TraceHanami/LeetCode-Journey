# 121 — Best Time to Buy and Sell Stock

## Problem
Given an array of daily stock prices, find the maximum profit from buying on one day and selling on a later day.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)**

**Examples:**
```text
Input: prices = [7,1,5,3,6,4]
Output: 5
```

---

## My Approaches
### Attempt 1 — Track Minimum Seen So Far ✅ Final Accepted Solution
**Why I used it:**
Only need to remember the lowest price so far and check the profit if selling today.

```python
def maxProfit(self, prices: List[int]) -> int:
    min_price = float('inf')
    best = 0
    for p in prices:
        if p < min_price:
            min_price = p
        elif p - min_price > best:
            best = p - min_price
    return best
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Walk through prices once, keeping the lowest price seen so far. At each day, the best possible profit if selling today is today's price minus that running minimum — track the max of those.

```python
def maxProfit(self, prices: List[int]) -> int:
    min_price = float('inf')
    best_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        best_profit = max(best_profit, price - min_price)
    return best_profit
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Track Minimum Seen So Far) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
A single pass tracking the running minimum buy price is all that's needed — no need to check every buy/sell pair.

---

## Reference
- LeetCode #121 — Best Time to Buy and Sell Stock
