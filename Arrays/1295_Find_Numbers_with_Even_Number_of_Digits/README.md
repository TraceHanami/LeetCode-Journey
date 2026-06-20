# 1295 — Find Numbers with Even Number of Digits

## Problem

Count digits in each number; count those with even digit length.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/)**

---

## Approach 1 — String length check ✅

**Idea:** len(str(num)) % 2 == 0 for each number.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Math log10

**Idea:** floor(log10(num)) + 1 gives digit count.

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — String length check | O(n) | O(1) | ✅ Yes |
| 2 — Math log10 | O(n) | O(1) | No |

---

## Reference

[LeetCode #1295 — Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/)
