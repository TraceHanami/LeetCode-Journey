# 1344 — Angle Between Hands of a Clock

## Problem

Calculate exact angles of hour and minute hands, return the smaller angle.

**Difficulty:** Med | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/angle-between-hands-of-a-clock/)**

---

## Approach 1 — Math formula ✅

**Idea:** Minute hand: 6*minutes degrees. Hour hand: 30*hour + 0.5*minutes degrees. Return min(diff, 360-diff).

**Complexity:**
- Time: O(1)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Math formula | O(1) | O(1) | ✅ Yes |

---

## Reference

[LeetCode #1344 — Angle Between Hands of a Clock](https://leetcode.com/problems/angle-between-hands-of-a-clock/)
