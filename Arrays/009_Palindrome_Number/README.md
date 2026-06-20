# 9 — Palindrome Number

## Problem

Reverse half the number and compare to the other half — no string conversion.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/palindrome-number/)**

---

## Approach 1 — Reverse half ✅

**Idea:** Reverse digits of second half. Compare with first half. Handle negatives and trailing zeros.

**Complexity:**
- Time: O(log n)
- Space: O(1)

---

## Approach 2 — String conversion

**Idea:** str(x) == str(x)[::-1]. Simple but uses extra space.

**Complexity:**
- Time: O(log n)
- Space: O(log n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Reverse half | O(log n) | O(1) | ✅ Yes |
| 2 — String conversion | O(log n) | O(log n) | No |

---

## Reference

[LeetCode #9 — Palindrome Number](https://leetcode.com/problems/palindrome-number/)
