# 283 — Move Zeroes

## Problem

Two pointers: keep a write pointer for non-zero elements, fill rest with zeros.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/move-zeroes/)**

---

## Approach 1 — Two pointers ✅

**Idea:** Write pointer advances only on non-zero. After loop, fill rest with 0.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Partition

**Idea:** Swap non-zero with write pointer position.

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Two pointers | O(n) | O(1) | ✅ Yes |
| 2 — Partition | O(n) | O(1) | No |

---

## Reference

[LeetCode #283 — Move Zeroes](https://leetcode.com/problems/move-zeroes/)
