# 35 — Search Insert Position

## Problem

Binary search — if not found, left pointer is the insert position.

**Difficulty:** Easy | **Topic:** Binary Search

**[View on LeetCode](https://leetcode.com/problems/search-insert-position/)**

---

## Approach 1 — Binary search ✅

**Idea:** Standard binary search. Return lo when target not found — lo is the insert position.

**Complexity:**
- Time: O(log n)
- Space: O(1)

---

## Approach 2 — Linear scan

**Idea:** Scan left to right, return index of first element >= target.

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Binary search | O(log n) | O(1) | ✅ Yes |
| 2 — Linear scan | O(n) | O(1) | No |

---

## Reference

[LeetCode #35 — Search Insert Position](https://leetcode.com/problems/search-insert-position/)
