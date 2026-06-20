# 125 — Valid Palindrome

## Problem

Keep only alphanumeric characters, compare to its reverse.

**Difficulty:** Easy | **Topic:** Strings

**[View on LeetCode](https://leetcode.com/problems/valid-palindrome/)**

---

## Approach 1 — Filter and reverse ✅

**Idea:** Filter non-alphanumeric, lowercase, compare to [::-1].

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 2 — Two pointers

**Idea:** Left/right skip non-alphanumeric, compare chars, move inward.

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Filter and reverse | O(n) | O(n) | ✅ Yes |
| 2 — Two pointers | O(n) | O(1) | No |

---

## Reference

[LeetCode #125 — Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
