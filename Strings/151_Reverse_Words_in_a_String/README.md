# 151 — Reverse Words in a String

## Problem

Split on whitespace, reverse the word list, rejoin with single space.

**Difficulty:** Med | **Topic:** Strings

**[View on LeetCode](https://leetcode.com/problems/reverse-words-in-a-string/)**

---

## Approach 1 — Split and reverse ✅

**Idea:** s.split() handles multiple spaces. Reverse list and join with ' '.

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 2 — Two pointers in-place

**Idea:** Reverse entire string, then reverse each word individually.

**Complexity:**
- Time: O(n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Split and reverse | O(n) | O(n) | ✅ Yes |
| 2 — Two pointers in-place | O(n) | O(n) | No |

---

## Reference

[LeetCode #151 — Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)
