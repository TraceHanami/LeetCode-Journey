# 88 — Merge Sorted Array

## Problem

Fill from the end — compare from back of both arrays to avoid overwriting.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/merge-sorted-array/)**

---

## Approach 1 — Three pointers from end ✅

**Idea:** p1=m-1, p2=n-1, p=m+n-1. Place larger of nums1[p1], nums2[p2] at p. Move pointers.

**Complexity:**
- Time: O(n+m)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Three pointers from end | O(n+m) | O(1) | ✅ Yes |

---

## Reference

[LeetCode #88 — Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
