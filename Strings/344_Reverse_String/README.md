# 344 — Reverse String

## Problem

Two pointers from both ends — swap in place.

**Difficulty:** Easy | **Topic:** Strings

**[View on LeetCode](https://leetcode.com/problems/reverse-string/)**

---

## Approach 1 — Two pointers in-place ✅

**Idea:** Swap s[left] and s[right], move pointers inward.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Built-in reverse

**Idea:** s.reverse() modifies list in place.

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Two pointers in-place | O(n) | O(1) | ✅ Yes |
| 2 — Built-in reverse | O(n) | O(1) | No |

---

## Reference

[LeetCode #344 — Reverse String](https://leetcode.com/problems/reverse-string/)
