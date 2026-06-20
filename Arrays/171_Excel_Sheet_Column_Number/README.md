# 171 — Excel Sheet Column Number

## Problem

Treat column title as a base-26 number using letters A=1..Z=26.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/excel-sheet-column-number/)**

---

## Approach 1 — Base-26 conversion ✅

**Idea:** result = result * 26 + (ord(c) - ord('A') + 1) for each character.

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Base-26 conversion | O(n) | O(1) | ✅ Yes |

---

## Reference

[LeetCode #171 — Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)
