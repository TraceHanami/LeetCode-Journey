# 263 — Ugly Number

## Problem

Divide out factors of 2, 3, 5 repeatedly; ugly numbers reduce to 1.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/ugly-number/)**

**Examples:**
```
n = 6 -> true
n = 1 -> true
n = 14 -> false
```
---

## Approach 1 — Repeated division ✅

**Idea:** While n divisible by 2, 3, or 5 — divide. Return n==1.

```python
class Solution1:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        return n == 1
```

**Complexity:**
- Time: O(log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Repeated division | O(log n) | O(1) | ✅ Yes |

---

## Reference

[LeetCode #263 — Ugly Number](https://leetcode.com/problems/ugly-number/)
