# 455 — Assign Cookies

## Problem

Greedily assign the smallest sufficient cookie to each child.

**Difficulty:** Easy | **Topic:** Greedy

**[View on LeetCode](https://leetcode.com/problems/assign-cookies/)**

---

## Approach 1 — Greedy two pointers ✅

**Idea:** Sort both arrays. Use two pointers — assign cookie to child if size >= greed. Move both pointers; otherwise only cookie pointer.

**Complexity:**
- Time: O(n log n + m log m)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Greedy two pointers | O(n log n + m log m) | O(1) | ✅ Yes |

---

## Reference

[LeetCode #455 — Assign Cookies](https://leetcode.com/problems/assign-cookies/)
