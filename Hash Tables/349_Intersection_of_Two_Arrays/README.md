# 349 — Intersection of Two Arrays

## Problem

Convert one array to set, filter the other by membership.

**Difficulty:** Easy | **Topic:** Hash Tables

**[View on LeetCode](https://leetcode.com/problems/intersection-of-two-arrays/)**

---

## Approach 1 — Set intersection ✅

**Idea:** set(nums1) & set(nums2) directly gives unique intersection.

**Complexity:**
- Time: O(n+m)
- Space: O(n)

---

## Approach 2 — Sort and two pointers

**Idea:** Sort both. Two pointers advance on mismatch, record match and advance both.

**Complexity:**
- Time: O(n log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Set intersection | O(n+m) | O(n) | ✅ Yes |
| 2 — Sort and two pointers | O(n log n) | O(1) | No |

---

## Reference

[LeetCode #349 — Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)
