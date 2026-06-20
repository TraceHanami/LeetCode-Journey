# 167 — Two Sum II Input Array Is Sorted

## Problem

Two pointers from both ends — sorted array makes this O(n).

**Difficulty:** Med | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)**

---

## Approach 1 — Two pointers ✅

**Idea:** Left and right pointers. Sum too small → move left right. Sum too big → move right left. Return when equal.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Binary search

**Idea:** For each element, binary search for the complement.

**Complexity:**
- Time: O(n log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Two pointers | O(n) | O(1) | ✅ Yes |
| 2 — Binary search | O(n log n) | O(1) | No |

---

## Reference

[LeetCode #167 — Two Sum II Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
