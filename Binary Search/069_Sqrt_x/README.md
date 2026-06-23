# 69 — Sqrt x

## Problem

Binary search on the answer space from 0 to x.

**Difficulty:** Easy | **Topic:** Binary Search

**[View on LeetCode](https://leetcode.com/problems/sqrt-x/)**

**Examples:**
```
x = 4 ->2
x = 8 -> 2
```

---

## Approach 1 — Binary search ✅

**Idea:** Search for largest k where k*k <= x.

```python
class Solution1:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
```

**Complexity:**
- Time: O(log x)
- Space: O(1)

---

## Approach 2 — Newton's method

**Idea:** x1 = (x0 + n/x0)/2 converges fast to sqrt.

```python
class Solution2:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r
```

**Complexity:**
- Time: O(log x)
- Space: O(1)

---

## Approach 3 — Built-in

**Idea:** int(math.sqrt(x)) — not recommended in interviews.

```python
import math

class Solution3:
    def mySqrt(self, x: int) -> int:
        return math.isqrt(x)
```

**Complexity:**
- Time: O(1)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Binary search | O(log x) | O(1) | ✅ Yes |
| 2 — Newton's method | O(log x) | O(1) | No |
| 3 — Built-in | O(1) | O(1) | No |

---

## Reference

[LeetCode #69 — Sqrt x](https://leetcode.com/problems/sqrt-x/)
