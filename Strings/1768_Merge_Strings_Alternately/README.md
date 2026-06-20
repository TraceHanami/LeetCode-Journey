# 1768 — Merge Strings Alternately

## Problem

Interleave characters from both strings; append remainder.

**Difficulty:** Easy | **Topic:** Strings

**[View on LeetCode](https://leetcode.com/problems/merge-strings-alternately/)**

---

## Approach 1 — Zip and append ✅

**Idea:** zip() pairs characters. Append leftover from the longer string.

**Complexity:**
- Time: O(n+m)
- Space: O(n+m)

---

## Approach 2 — Single pointer

**Idea:** Loop to max length, append s1[i] if valid, then s2[i] if valid.

**Complexity:**
- Time: O(n+m)
- Space: O(n+m)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Zip and append | O(n+m) | O(n+m) | ✅ Yes |
| 2 — Single pointer | O(n+m) | O(n+m) | No |

---

## Reference

[LeetCode #1768 — Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/)
