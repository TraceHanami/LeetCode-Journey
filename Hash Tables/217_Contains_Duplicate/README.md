# 217 — Contains Duplicate

## Problem

A set cannot have duplicates — if set size < array size, duplicates exist.

**Difficulty:** Easy | **Topic:** Hash Tables

**[View on LeetCode](https://leetcode.com/problems/contains-duplicate/)**

---

## Approach 1 — Hash set ✅

**Idea:** return len(set(nums)) < len(nums).

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 2 — Sort

**Idea:** Sort and check adjacent elements.

**Complexity:**
- Time: O(n log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Hash set | O(n) | O(n) | ✅ Yes |
| 2 — Sort | O(n log n) | O(1) | No |

---

## Reference

[LeetCode #217 — Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
