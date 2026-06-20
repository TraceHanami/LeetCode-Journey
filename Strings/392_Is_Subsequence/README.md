# 392 — Is Subsequence

## Problem

Greedy two-pointer: advance s pointer whenever characters match.

**Difficulty:** Easy | **Topic:** Strings

**[View on LeetCode](https://leetcode.com/problems/is-subsequence/)**

---

## Approach 1 — Two pointers greedy ✅

**Idea:** Pointer on s advances when s[i]==t[j]. If s pointer reaches end, s is a subsequence.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Recursive

**Idea:** Base case: s empty → True. Match first char and recurse on remainder.

**Complexity:**
- Time: O(n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Two pointers greedy | O(n) | O(1) | ✅ Yes |
| 2 — Recursive | O(n) | O(n) | No |

---

## Reference

[LeetCode #392 — Is Subsequence](https://leetcode.com/problems/is-subsequence/)
