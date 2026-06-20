# 704 — Binary Search

## Problem

Classic binary search — halve the search space each iteration.

**Difficulty:** Easy | **Topic:** Binary Search

**[View on LeetCode](https://leetcode.com/problems/binary-search/)**

---

## Approach 1 — Iterative binary search ✅

**Idea:** lo=0, hi=n-1. mid=(lo+hi)//2. Adjust lo or hi based on comparison.

**Complexity:**
- Time: O(log n)
- Space: O(1)

---

## Approach 2 — Recursive binary search

**Idea:** Same logic with recursive calls. Stack space is the trade-off.

**Complexity:**
- Time: O(log n)
- Space: O(log n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Iterative binary search | O(log n) | O(1) | ✅ Yes |
| 2 — Recursive binary search | O(log n) | O(log n) | No |

---

## Reference

[LeetCode #704 — Binary Search](https://leetcode.com/problems/binary-search/)
