# 58 — Length of Last Word

## Problem

Strip trailing spaces, find the last word, return its length.

**Difficulty:** Easy | **Topic:** Strings

**[View on LeetCode](https://leetcode.com/problems/length-of-last-word/)**

---

## Approach 1 — Strip and split ✅

**Idea:** Strip the string, split by space, return length of last element.

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 2 — Reverse scan

**Idea:** Scan from end, skip spaces, count letters until next space.

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Strip and split | O(n) | O(n) | ✅ Yes |
| 2 — Reverse scan | O(n) | O(1) | No |

---

## Reference

[LeetCode #58 — Length of Last Word](https://leetcode.com/problems/length-of-last-word/)
