# 821 — Shortest Distance to a Character

## Problem

Two-pass: scan left for nearest c, scan right for nearest c, take min.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/shortest-distance-to-a-character/)**

---

## Approach 1 — Two-pass scan ✅

**Idea:** Left pass fills distances from last seen c. Right pass updates with next c. Min of both.

**Complexity:**
- Time: O(n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Two-pass scan | O(n) | O(n) | ✅ Yes |

---

## Reference

[LeetCode #821 — Shortest Distance to a Character](https://leetcode.com/problems/shortest-distance-to-a-character/)
