# 75 — Sort Colors

## Problem

Dutch National Flag algorithm — three-way partition in a single pass.

**Difficulty:** Med | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/sort-colors/)**

---

## Approach 1 — Dutch National Flag ✅

**Idea:** Three pointers: lo, mid, hi. Swap 0s to front, 2s to back, 1s stay in middle.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Count and fill

**Idea:** Count 0s, 1s, 2s. Overwrite array with correct counts.

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Dutch National Flag | O(n) | O(1) | ✅ Yes |
| 2 — Count and fill | O(n) | O(1) | No |

---

## Reference

[LeetCode #75 — Sort Colors](https://leetcode.com/problems/sort-colors/)
