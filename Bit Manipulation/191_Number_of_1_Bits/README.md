# 191 — Number of 1 Bits

## Problem

Count set bits in the binary representation of n.

**Difficulty:** Easy | **Topic:** Bit Manipulation

**[View on LeetCode](https://leetcode.com/problems/number-of-1-bits/)**

---

## Approach 1 — Bit mask loop ✅

**Idea:** AND n with 1 to check last bit, right-shift n each iteration.

**Complexity:**
- Time: O(1)
- Space: O(1)

---

## Approach 2 — Brian Kernighan

**Idea:** n & (n-1) clears the lowest set bit. Count how many times until n=0.

**Complexity:**
- Time: O(k)
- Space: O(1)

---

## Approach 3 — Built-in bin()

**Idea:** bin(n).count('1')

**Complexity:**
- Time: O(1)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Bit mask loop | O(1) | O(1) | ✅ Yes |
| 2 — Brian Kernighan | O(k) | O(1) | No |
| 3 — Built-in bin() | O(1) | O(1) | No |

---

## Reference

[LeetCode #191 — Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
