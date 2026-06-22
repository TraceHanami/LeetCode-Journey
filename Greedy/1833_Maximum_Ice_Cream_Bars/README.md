# 1833 — Maximum Ice Cream Bars

## Problem

A boy wants to buy as many ice cream bars as possible. Given an array `costs` where `costs[i]` is the price of the `i`th bar, and an integer `coins` representing the total coins he has, return the **maximum number of bars** he can buy. He can buy the bars in any order.

**Difficulty:** Medium | **Topic:** Greedy / Sorting

**[View on LeetCode](https://leetcode.com/problems/maximum-ice-cream-bars/)**

**Examples:**
```
costs = [1,3,2,4,1], coins = 7  →  4
costs = [10,6,8,7,7,8], coins = 5  →  0
costs = [1,6,3,1,2,5], coins = 20  →  6
```

---

## Approach 1 — Greedy: Sort and Buy Cheapest First ✅

**Idea:** To maximize the number of bars, always buy the cheapest available bar first. Sort costs in ascending order and greedily purchase until coins run out.

```python
class Solution1:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for cost in costs:
            if coins >= cost:
                coins -= cost
                count += 1
            else:
                break
        return count
```

**Complexity:**
- Time: O(n log n)
- Space: O(1)

---

## Approach 2 — Counting Sort

**Idea:** Since costs are bounded (1 ≤ cost ≤ 10^5), use a frequency array. Iterate price by price, buying as many bars at each price as affordable. Avoids the overhead of comparison-based sort.

```python
class Solution2:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        freq = [0] * (max_cost + 1)
        for cost in costs:
            freq[cost] += 1

        count = 0
        for price in range(1, max_cost + 1):
            if coins < price:
                break
            can_buy = min(freq[price], coins // price)
            count += can_buy
            coins -= can_buy * price

        return count
```

**Complexity:**
- Time: O(n + max_cost)
- Space: O(max_cost)

---

## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Greedy Sort | O(n log n) | O(1) | ✅ Yes |
| 2 — Counting Sort | O(n + max_cost) | O(max_cost) | No |

**Note:** Approach 2 is technically faster for large inputs with bounded values, but Approach 1 is cleaner and the expected interview answer.

---

## Reference

[LeetCode #1833 — Maximum Ice Cream Bars](https://leetcode.com/problems/maximum-ice-cream-bars/)
