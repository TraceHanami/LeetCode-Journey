# 191 — Number of 1 Bits

## Problem
Given a positive integer, return the number of set bits (Hamming weight) in its binary representation.

**Difficulty:** Easy | **Topic:** Bit Manipulation
**[View on LeetCode](https://leetcode.com/problems/number-of-1-bits/)**

**Examples:**
```text
Input: n = 11 (1011)
Output: 3
```

---

## My Approaches
### Attempt 1 — Count '1's in Binary String ✅ Final Accepted Solution
**Why I used it:**
Convert to binary text and count the characters that equal '1'.

```python
def hammingWeight(self, n: int) -> int:
    bits = bin(n)[2:]
    return sum(1 for b in bits if b == '1')
```

**Complexity:**
- Time: O(32) = O(1)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Brian Kernighan's trick: `n & (n - 1)` clears the lowest set bit. Repeating this until n becomes 0 counts exactly as many times as there were set bits — faster on average than checking every bit position.

```python
def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
```

### Complexity
- Time: O(k) where k = number of set bits
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Count '1's in Binary String) | O(32) = O(1) | O(1) | ✅ |
| Standard Approach 1 | O(k) where k = number of set bits | O(1) | ✅ |


---

## Key Takeaway
Brian Kernighan's `n & (n - 1)` trick clears one set bit per iteration, making the loop run proportional to the number of 1s rather than 32 fixed iterations.

---

## Reference
- LeetCode #191 — Number of 1 Bits
