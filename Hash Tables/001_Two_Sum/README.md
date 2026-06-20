# 1 — Two Sum

## Problem

Store complement in a hash map — O(n) single pass.

**Difficulty:** Easy | **Topic:** Hash Tables

**[View on LeetCode](https://leetcode.com/problems/two-sum/)**

---

## Approach 1 — Hash map one pass ✅

**Idea:** For each num, check if complement (target-num) is in map. If yes return indices. Else store num:index.

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 2 — Brute force

**Idea:** Check all pairs. Too slow for large inputs.

**Complexity:**
- Time: O(n²)
- Space: O(1)

---

## Approach 3 — Sort and two pointers

**Idea:** Sort with original indices. Two pointers from both ends. Note: doesn't work if original indices needed without extra bookkeeping.

**Complexity:**
- Time: O(n log n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Hash map one pass | O(n) | O(n) | ✅ Yes |
| 2 — Brute force | O(n²) | O(1) | No |
| 3 — Sort and two pointers | O(n log n) | O(n) | No |

---

## Reference

[LeetCode #1 — Two Sum](https://leetcode.com/problems/two-sum/)
