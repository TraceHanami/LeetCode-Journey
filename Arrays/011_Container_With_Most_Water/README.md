# 11 — Container With Most Water

## Problem

Greedy two-pointer: always move the shorter line inward to maximize area.

**Difficulty:** Med | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/container-with-most-water/)**

---

## Approach 1 — Two pointers ✅

**Idea:** Start with widest container. Move pointer at shorter height inward. Track max area.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Brute force

**Idea:** Check all pairs. Too slow for large input.

**Complexity:**
- Time: O(n²)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Two pointers | O(n) | O(1) | ✅ Yes |
| 2 — Brute force | O(n²) | O(1) | No |

---

## Reference

[LeetCode #11 — Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
