# 3754 — Concatenate Non-Zero Digits and Multiply by Sum I

## Problem
Given an integer n, build a number by concatenating its non-zero digits (in order), sum all its non-zero digits separately, then multiply the concatenated number by that digit sum.

**Difficulty:** Easy | **Topic:** Math
**[View on LeetCode](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/)**

**Examples:**
```text
Input: n = 10203
Output: concatenated non-zero digits form 123, digit sum is 1+2+3=6, result is 123*6 = 738
```

---

## My Approaches
### Attempt 1 — Single Pass Building Both Values Digit-by-Digit ✅ Final Accepted Solution
**Why I used it:**
Process digits from the least significant end, skipping zeros, building the concatenated result with a positional multiplier while simultaneously accumulating the digit sum.

```python
def sumAndMultiply(self, n: int) -> int:
    concat = digit_sum = 0
    place = 1
    while n > 0:
        d = n % 10
        if d != 0:
            digit_sum += d
            concat += d * place
            place *= 10
        n //= 10
    return concat * digit_sum
```

**Complexity:**
- Time: O(log n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Peel digits off from the right with modulo/division. Skip zeros entirely — they contribute nothing to either the sum or the concatenation. For the non-zero digits, accumulate a running sum, and build the concatenated number by placing each new digit into the next open decimal position using a growing place-value multiplier.

```python
def sumAndMultiply(self, n: int) -> int:
    concat, digit_sum, place = 0, 0, 1
    while n > 0:
        digit = n % 10
        n //= 10
        if digit == 0:
            continue
        digit_sum += digit
        concat += digit * place
        place *= 10
    return concat * digit_sum
```

### Complexity
- Time: O(log n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Single Pass Building Both Values Digit-by-Digit) | O(log n) | O(1) | ✅ |
| Standard Approach 1 | O(log n) | O(1) | ✅ |


---

## Key Takeaway
Building a number digit-by-digit from the least significant end with a growing place-value multiplier avoids ever converting to a string.

---

## Reference
- LeetCode #3754 — Concatenate Non-Zero Digits and Multiply by Sum I
