# 190 — Reverse Bits

## Problem

Build the reversed 32-bit integer bit by bit.

**Difficulty:** Easy | **Topic:** Bit Manipulation

**[View on LeetCode](https://leetcode.com/problems/reverse-bits/)**

---

## Approach 1 — Bit-by-bit ✅

**Idea:** Extract last bit of n, shift result left and OR in the bit, shift n right. Repeat 32 times.

**Complexity:**
- Time: O(1)
- Space: O(1)

---

## Approach 2 — Python bin reverse

**Idea:** Convert to 32-bit binary string, reverse it, parse back to int.

**Complexity:**
- Time: O(1)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Bit-by-bit | O(1) | O(1) | ✅ Yes |
| 2 — Python bin reverse | O(1) | O(1) | No |

---

## Reference

[LeetCode #190 — Reverse Bits](https://leetcode.com/problems/reverse-bits/)
