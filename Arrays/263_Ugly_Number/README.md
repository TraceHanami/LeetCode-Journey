# 263 — Ugly Number

## Problem
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5. Given an integer n, return true if it is an ugly number.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/ugly-number/)**

**Examples:**
```text
Input: n = 6
Output: true

Input: n = 14
Output: false
```

---

## My Approaches
### Attempt 1 — Divide Out 2, 3, 5 ✅ Final Accepted Solution
**Why I used it:**
Repeatedly strip each allowed prime factor; if only 1 remains, every factor was one of 2, 3, or 5.

```python
def isUgly(self, n: int) -> bool:
    if n <= 0:
        return False
    for f in [2, 3, 5]:
        while n % f == 0:
            n //= f
    return n == 1
```

**Complexity:**
- Time: O(log n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Divide n by 2, 3, and 5 as many times as each divides evenly. If what's left is 1, every prime factor was one of those three; anything else means a different prime factor exists (or n was <= 0).

```python
def isUgly(self, n: int) -> bool:
    if n <= 0:
        return False
    for factor in (2, 3, 5):
        while n % factor == 0:
            n //= factor
    return n == 1
```

### Complexity
- Time: O(log n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Divide Out 2, 3, 5) | O(log n) | O(1) | ✅ |
| Standard Approach 1 | O(log n) | O(1) | ✅ |


---

## Key Takeaway
Stripping out each allowed prime factor and checking what's left is a direct translation of the problem's definition.

---

## Reference
- LeetCode #263 — Ugly Number
