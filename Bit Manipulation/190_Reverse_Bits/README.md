# 190 — Reverse Bits

## Problem

Build the reversed 32-bit integer bit by bit.

**Difficulty:** Easy | **Topic:** Bit Manipulation

**[View on LeetCode](https://leetcode.com/problems/reverse-bits/)**

**Examples:**
```
n = 43261596 -> 964176192
n = 2147483644 -> 1073741822
```
---

## Approach 1 — Bit-by-bit ✅

**Idea:** Extract last bit of n, shift result left and OR in the bit, shift n right. Repeat 32 times.
```python
class Solution1:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
```

**Complexity:**
- Time: O(1)
- Space: O(1)

---

## Approach 2 — Python bin reverse

**Idea:** Convert to 32-bit binary string, reverse it, parse back to int.

```python
class Solution2:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)
```

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
