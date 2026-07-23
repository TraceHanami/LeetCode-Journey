# 1833 — Maximum Ice Cream Bars

## Problem
Given the cost of each ice cream bar and a total amount of coins, return the maximum number of bars you can buy.

**Difficulty:** Medium | **Topic:** Greedy
**[View on LeetCode](https://leetcode.com/problems/maximum-ice-cream-bars/)**

**Examples:**
```text
Input: costs = [1,3,2,4,1], coins = 7
Output: 4
```

---

## My Approaches
### Attempt 1 — Sort, Buy Cheapest First ✅ Final Accepted Solution
**Why I used it:**
To maximize the count of bars bought, always buy the cheapest ones first.

```python
def maxIceCream(self, costs: List[int], coins: int) -> int:
    costs.sort()
    count = 0
    for c in costs:
        if coins >= c:
            coins -= c
            count += 1
        else:
            break
    return count
```

**Complexity:**
- Time: O(n log n)
- Space: O(1) extra

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Sorting by price and greedily buying the cheapest bars first is provably optimal: for a fixed budget, buying more cheaper items always allows at least as many total items as buying fewer expensive ones.

```python
def maxIceCream(self, costs: List[int], coins: int) -> int:
    costs.sort()
    count = 0
    for cost in costs:
        if cost > coins:
            break
        coins -= cost
        count += 1
    return count
```

### Complexity
- Time: O(n log n)
- Space: O(1) extra

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Sort, Buy Cheapest First) | O(n log n) | O(1) extra | ✅ |
| Standard Approach 1 | O(n log n) | O(1) extra | ✅ |


---

## Key Takeaway
When the goal is 'maximize count under a budget', sorting cheapest-first and buying greedily is the standard optimal strategy.

---

## Reference
- LeetCode #1833 — Maximum Ice Cream Bars
