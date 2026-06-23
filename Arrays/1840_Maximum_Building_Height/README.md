# 1840 — Maximum Building Height

## Problem

Spread height constraints left and right, then find max between adjacent constraints.

**Difficulty:** Hard | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/maximum-building-height/)**

**Examples:**
```
n = 5, restrictions = [[2,1],[4,1]] -> 2
n = 6, restrictions = [] -> 5
n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]] -> 5
```
---

## Approach 1 — Two-pass constraint propagation ✅

**Idea:** Sort restrictions by position. Propagate constraints left-to-right then right-to-left. Find max height between each pair.

```python
class Solution1:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        restrictions.sort()

        # Forward pass: cap each building by previous constraint
        for i in range(1, len(restrictions)):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i-1][1] + restrictions[i][0] - restrictions[i-1][0]
            )

        # Backward pass: cap each building by next constraint
        for i in range(len(restrictions) - 2, -1, -1):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i+1][1] + restrictions[i+1][0] - restrictions[i][0]
            )

        # Find max height between each pair of adjacent restrictions
        max_h = 0
        for i in range(1, len(restrictions)):
            p1, h1 = restrictions[i-1]
            p2, h2 = restrictions[i]
            # Peak between two buildings: average of heights + half the gap
            peak = (h1 + h2 + p2 - p1) // 2
            max_h = max(max_h, peak)

        return max_h
```

**Complexity:**
- Time: O(n log n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Two-pass constraint propagation | O(n log n) | O(n) | ✅ Yes |

---

## Reference

[LeetCode #1840 — Maximum Building Height](https://leetcode.com/problems/maximum-building-height/)
