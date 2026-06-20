# 977 — Squares of a Sorted Array

## Problem

Two pointers from both ends — largest squares always at the extremes.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array/)**

---

## Approach 1 — Two pointers ✅

**Idea:** Compare abs values at left and right pointers. Place larger square at end of result. Move that pointer inward.

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 2 — Sort squares

**Idea:** Square all elements, sort. Simple but not optimal.

**Complexity:**
- Time: O(n log n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Two pointers | O(n) | O(n) | ✅ Yes |
| 2 — Sort squares | O(n log n) | O(n) | No |

---

## Reference

[LeetCode #977 — Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)
