# 14 — Longest Common Prefix

## Problem

Compare characters column by column across all strings.

**Difficulty:** Easy | **Topic:** Strings

**[View on LeetCode](https://leetcode.com/problems/longest-common-prefix/)**

---

## Approach 1 — Vertical scanning ✅

**Idea:** Fix first string as reference. For each character position, check all strings match.

**Complexity:**
- Time: O(n*m)
- Space: O(1)

---

## Approach 2 — Sort and compare ends

**Idea:** Sort array. LCP of sorted array = LCP of first and last strings only.

**Complexity:**
- Time: O(n log n)
- Space: O(1)

---

## Approach 3 — Divide and conquer

**Idea:** Split array in half, find LCP of each half, merge.

**Complexity:**
- Time: O(n*m)
- Space: O(m log n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Vertical scanning | O(n*m) | O(1) | ✅ Yes |
| 2 — Sort and compare ends | O(n log n) | O(1) | No |
| 3 — Divide and conquer | O(n*m) | O(m log n) | No |

---

## Reference

[LeetCode #14 — Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
