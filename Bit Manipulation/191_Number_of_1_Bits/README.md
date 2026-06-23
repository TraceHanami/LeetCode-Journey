# 191 — Number of 1 Bits

## Problem

Count set bits in the binary representation of n.

**Difficulty:** Easy | **Topic:** Bit Manipulation

**[View on LeetCode](https://leetcode.com/problems/number-of-1-bits/)**

**Examples:**
```
n = 11 -> 3
n = 128 -> 1
n = 2147483645 -> 30
```
---

## Approach 1 — Bit mask loop ✅

**Idea:** AND n with 1 to check last bit, right-shift n each iteration.

```python
class Solution1:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
```

**Complexity:**
- Time: O(1)
- Space: O(1)

---

## Approach 2 — Brian Kernighan

**Idea:** n & (n-1) clears the lowest set bit. Count how many times until n=0.

```python
class Solution2:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1  # clears lowest set bit
            count += 1
        return count
```

**Complexity:**
- Time: O(k)
- Space: O(1)

---

## Approach 3 — Built-in bin()

**Idea:** bin(n).count('1')

```python
class Solution3:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
```

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
