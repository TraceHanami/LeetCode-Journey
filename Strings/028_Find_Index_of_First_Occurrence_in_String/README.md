# 28 — Find Index of First Occurrence in String

## Problem

Find the first index where needle appears in haystack.

**Difficulty:** Easy | **Topic:** Strings

**[View on LeetCode](https://leetcode.com/problems/find-index-of-first-occurrence-in-string/)**

---

## Approach 1 — Sliding window ✅

**Idea:** Check each window of length m in haystack against needle.

**Complexity:**
- Time: O(n*m)
- Space: O(1)

---

## Approach 2 — Built-in find

**Idea:** Use haystack.find(needle) or haystack.index(needle).

**Complexity:**
- Time: O(n*m)
- Space: O(1)

---

## Approach 3 — KMP algorithm

**Idea:** Build failure function for needle, use it to skip redundant comparisons.

**Complexity:**
- Time: O(n+m)
- Space: O(m)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Sliding window | O(n*m) | O(1) | ✅ Yes |
| 2 — Built-in find | O(n*m) | O(1) | No |
| 3 — KMP algorithm | O(n+m) | O(m) | No |

---

## Reference

[LeetCode #28 — Find Index of First Occurrence in String](https://leetcode.com/problems/find-index-of-first-occurrence-in-string/)
