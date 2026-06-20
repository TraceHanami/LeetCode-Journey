# 1840 — Maximum Building Height

## Problem

Spread height constraints left and right, then find max between adjacent constraints.

**Difficulty:** Hard | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/maximum-building-height/)**

---

## Approach 1 — Two-pass constraint propagation ✅

**Idea:** Sort restrictions by position. Propagate constraints left-to-right then right-to-left. Find max height between each pair.

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
