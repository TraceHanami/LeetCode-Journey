# 268 — Missing Number

## Problem

Expected sum minus actual sum gives the missing number.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/missing-number/)**

---

## Approach 1 — Gauss sum ✅

**Idea:** Missing = n*(n+1)//2 - sum(nums).

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — XOR

**Idea:** XOR all indices and values — duplicates cancel, leaving the missing number.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 3 — Sort

**Idea:** Sort and check if nums[i] == i.

**Complexity:**
- Time: O(n log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Gauss sum | O(n) | O(1) | ✅ Yes |
| 2 — XOR | O(n) | O(1) | No |
| 3 — Sort | O(n log n) | O(1) | No |

---

## Reference

[LeetCode #268 — Missing Number](https://leetcode.com/problems/missing-number/)
