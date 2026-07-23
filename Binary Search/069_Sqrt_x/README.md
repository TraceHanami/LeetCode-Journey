# 069 — Sqrt(x)

## Problem
Given a non-negative integer x, return the integer square root of x (round down).

**Difficulty:** Easy | **Topic:** Binary Search
**[View on LeetCode](https://leetcode.com/problems/sqrtx/)**

**Examples:**
```text
Input: x = 8
Output: 2
```

---

## My Approaches
### Attempt 1 — Built-in isqrt ✅ Final Accepted Solution
**Why I used it:**
Python's math.isqrt computes the integer square root directly and efficiently.

```python
def mySqrt(self, x: int) -> int:
    return isqrt(x)
```

**Complexity:**
- Time: O(log x)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Binary search over the candidate answer range [0, x]: for each midpoint, check if mid*mid <= x. The largest mid satisfying that is the floor square root — this is what math.isqrt effectively does under the hood.

```python
def mySqrt(self, x: int) -> int:
    if x < 2:
        return x
    left, right = 1, x // 2
    ans = 1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans
```

### Complexity
- Time: O(log x)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Built-in isqrt) | O(log x) | O(1) | ✅ |
| Standard Approach 1 | O(log x) | O(1) | ✅ |


---

## Key Takeaway
Integer square root is a monotonic-predicate binary search problem — 'is mid*mid <= x' is exactly the kind of predicate binary search is built for.

---

## Reference
- LeetCode #69 — Sqrt(x)
