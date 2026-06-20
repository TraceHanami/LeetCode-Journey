# 2108 — Find First Palindromic String in Array

## Problem

Check each word if it equals its reverse; return first match.

**Difficulty:** Easy | **Topic:** Strings

**[View on LeetCode](https://leetcode.com/problems/find-first-palindromic-string-in-array/)**

---

## Approach 1 — Reverse check ✅

**Idea:** For each word, check word == word[::-1]. Return first match.

**Complexity:**
- Time: O(n*m)
- Space: O(1)

---

## Approach 2 — Two pointers

**Idea:** For each word, use two pointers from both ends to verify palindrome.

**Complexity:**
- Time: O(n*m)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Reverse check | O(n*m) | O(1) | ✅ Yes |
| 2 — Two pointers | O(n*m) | O(1) | No |

---

## Reference

[LeetCode #2108 — Find First Palindromic String in Array](https://leetcode.com/problems/find-first-palindromic-string-in-array/)
