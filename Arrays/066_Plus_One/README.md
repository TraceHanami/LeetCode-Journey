# 66 — Plus One

## Problem

Increment the last digit; propagate carry if digit becomes 10.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/plus-one/)**

---

## Approach 1 — Reverse carry propagation ✅

**Idea:** Traverse from end; increment digit, return if no carry. If all 9s, prepend 1.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Convert to int

**Idea:** Join digits to int, add 1, convert back to list.

**Complexity:**
- Time: O(n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Reverse carry propagation | O(n) | O(1) | ✅ Yes |
| 2 — Convert to int | O(n) | O(n) | No |

---

## Reference

[LeetCode #66 — Plus One](https://leetcode.com/problems/plus-one/)
