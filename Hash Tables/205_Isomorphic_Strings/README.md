# 205 — Isomorphic Strings

## Problem

Map each character in s to corresponding character in t; check consistency both ways.

**Difficulty:** Easy | **Topic:** Hash Tables

**[View on LeetCode](https://leetcode.com/problems/isomorphic-strings/)**

---

## Approach 1 — Two hash maps ✅

**Idea:** Map s→t and t→s. Reject if any inconsistency found.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Encode pattern

**Idea:** Replace each char with its first-seen index. If encoded s == encoded t, isomorphic.

**Complexity:**
- Time: O(n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Two hash maps | O(n) | O(1) | ✅ Yes |
| 2 — Encode pattern | O(n) | O(n) | No |

---

## Reference

[LeetCode #205 — Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)
