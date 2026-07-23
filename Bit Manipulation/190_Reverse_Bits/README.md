# 190 — Reverse Bits

## Problem
Reverse the bits of a given 32-bit unsigned integer.

**Difficulty:** Easy | **Topic:** Bit Manipulation
**[View on LeetCode](https://leetcode.com/problems/reverse-bits/)**

**Examples:**
```text
Input: n = 00000010100101000001111010011100
Output: 964176192 (00111001011110000010100101000000)
```

---

## My Approaches
### Attempt 1 — String Reversal via bin() ✅ Final Accepted Solution
**Why I used it:**
Convert to a zero-padded 32-bit binary string, reverse it, and parse it back to an int.

```python
def reverseBits(self, n: int) -> int:
    bits = bin(n)[2:].zfill(32)
    return int(bits[::-1], 2)
```

**Complexity:**
- Time: O(32) = O(1)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Build the result bit by bit: shift the accumulated result left, pull off the lowest bit of n with `& 1`, OR it in, then shift n right. Repeating 32 times reverses the bit order.

```python
def reverseBits(self, n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
```

### Complexity
- Time: O(32) = O(1)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (String Reversal via bin()) | O(32) = O(1) | O(1) | ✅ |
| Standard Approach 1 | O(32) = O(1) | O(1) | ✅ |


---

## Key Takeaway
String reversal is a clean shortcut in Python, but the bit-shifting version is the language-agnostic technique and avoids any string allocation.

---

## Reference
- LeetCode #190 — Reverse Bits
