# 21 — Merge Two Sorted Lists

## Problem

Compare heads of both lists, attach the smaller, advance that pointer.

**Difficulty:** Easy | **Topic:** Linked Lists

**[View on LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)**

---

## Approach 1 — Iterative with dummy head ✅

**Idea:** Use a dummy node to simplify edge cases. Attach remaining list at end.

**Complexity:**
- Time: O(n+m)
- Space: O(1)

---

## Approach 2 — Recursive

**Idea:** Base case: one list empty. Attach smaller head and recurse.

**Complexity:**
- Time: O(n+m)
- Space: O(n+m)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Iterative with dummy head | O(n+m) | O(1) | ✅ Yes |
| 2 — Recursive | O(n+m) | O(n+m) | No |

---

## Reference

[LeetCode #21 — Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
