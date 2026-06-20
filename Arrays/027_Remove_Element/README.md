# 27 — Remove Element

## Problem

Two-pointer: overwrite elements equal to val with valid elements.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/remove-element/)**

---

## Approach 1 — Two pointers ✅

**Idea:** Keep a write pointer; copy elements != val to front.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Swap with end

**Idea:** Swap val elements with end of array and shrink size.

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Two pointers | O(n) | O(1) | ✅ Yes |
| 2 — Swap with end | O(n) | O(1) | No |

---

## Reference

[LeetCode #27 — Remove Element](https://leetcode.com/problems/remove-element/)
