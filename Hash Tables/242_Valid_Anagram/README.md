# 242 — Valid Anagram

## Problem

Two strings are anagrams if they have identical character frequency counts.

**Difficulty:** Easy | **Topic:** Hash Tables

**[View on LeetCode](https://leetcode.com/problems/valid-anagram/)**

---

## Approach 1 — Counter comparison ✅

**Idea:** Count character frequencies with Counter or array of 26. Compare both counts.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Sort and compare

**Idea:** Sort both strings. Equal sorted strings = anagram.

**Complexity:**
- Time: O(n log n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Counter comparison | O(n) | O(1) | ✅ Yes |
| 2 — Sort and compare | O(n log n) | O(n) | No |

---

## Reference

[LeetCode #242 — Valid Anagram](https://leetcode.com/problems/valid-anagram/)
