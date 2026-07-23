# 1840 — Maximum Building Height

## Problem
You want to build n buildings, each with a non-negative integer height, where building 1 must have height 0 and adjacent buildings differ by at most 1. Given a list of (building, maxHeight) restrictions, maximize the height of the tallest building.

**Difficulty:** Hard | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/maximum-building-height/)**

**Examples:**
```text
Input: n = 5, restrictions = [[2,1],[4,1]]
Output: 2
```

---

## My Approaches
### Attempt 1 — Propagate Restrictions Left-to-Right and Right-to-Left, Then Sweep ✅ Final Accepted Solution
**Why I used it:**
Turn the restrictions into a sorted list of (position, cap) pairs including the fixed endpoints, then tighten every cap based on its neighbors in both directions before computing the achievable peak between each adjacent pair.

```python
def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
    r = restrictions[:]
    r.append([1, 0])
    r.sort()
    if r[-1][0] != n:
        r.append([n, n - 1])
    m = len(r)
    for i in range(1, m):
        d = r[i][0] - r[i - 1][0]
        r[i][1] = min(r[i][1], r[i - 1][1] + d)
    for i in range(m - 2, -1, -1):
        d = r[i + 1][0] - r[i][0]
        r[i][1] = min(r[i][1], r[i + 1][1] + d)
    best = 0
    for i in range(1, m):
        x, h = r[i - 1]
        y, k = r[i]
        d = y - x
        best = max(best, (h + k + d) // 2)
    return best
```

**Complexity:**
- Time: O(n log n)
- Space: O(n)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Add the implicit restrictions (building 1 has height 0, building n has no explicit cap so its max is n-1), sort all restricted points by position. Sweep left-to-right so every cap is at most the previous cap plus the distance traveled (heights change by at most 1 per building), then sweep right-to-left to apply the same tightening from the other direction. Once every pair of adjacent restricted points has consistent caps, the highest achievable point between any two capped points is a simple 'triangle peak' formula: (capA + capB + distance) // 2.

```python
def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
    points = sorted(restrictions + [[1, 0]])
    if points[-1][0] != n:
        points.append([n, n - 1])
    for i in range(1, len(points)):
        dist = points[i][0] - points[i - 1][0]
        points[i][1] = min(points[i][1], points[i - 1][1] + dist)
    for i in range(len(points) - 2, -1, -1):
        dist = points[i + 1][0] - points[i][0]
        points[i][1] = min(points[i][1], points[i + 1][1] + dist)
    best = 0
    for (x1, h1), (x2, h2) in zip(points, points[1:]):
        dist = x2 - x1
        best = max(best, (h1 + h2 + dist) // 2)
    return best
```

### Complexity
- Time: O(n log n)
- Space: O(n)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Propagate Restrictions Left-to-Right and Right-to-Left, Then Sweep) | O(n log n) | O(n) | ✅ |
| Standard Approach 1 | O(n log n) | O(n) | ✅ |


---

## Key Takeaway
With a 'changes by at most 1 per step' constraint, propagating caps forward and backward between fixed points, then using the triangle-peak formula (h1+h2+dist)//2 between each pair, avoids ever simulating every building's height individually.

---

## Reference
- LeetCode #1840 — Maximum Building Height
