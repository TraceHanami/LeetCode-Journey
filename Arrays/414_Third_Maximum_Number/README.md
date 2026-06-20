# 414 — Third Maximum Number

## Problem

Track top three distinct maximums in a single pass.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/third-maximum-number/)**

---

## Approach 1 — Three variables ✅

**Idea:** Maintain first, second, third max. Skip duplicates. Return third if exists, else first.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Sorted set

**Idea:** Use sorted set, pick third from end if size >= 3.

**Complexity:**
- Time: O(n log n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Three variables | O(n) | O(1) | ✅ Yes |
| 2 — Sorted set | O(n log n) | O(n) | No |

---

## Reference

[LeetCode #414 — Third Maximum Number](https://leetcode.com/problems/third-maximum-number/)
