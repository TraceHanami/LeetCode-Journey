# 509 — Fibonacci Number

## Problem
Given n, calculate F(n), the n-th Fibonacci number.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/fibonacci-number/)**

**Examples:**
```text
Input: n = 4
Output: 3

Input: n = 2
Output: 1
```

---

## My Approaches
### Attempt 1 — Iterative Bottom-Up ✅ Final Accepted Solution
**Why I used it:**
Avoids recursion overhead and exponential blowup by building up from F(0) and F(1).

```python
def fib(self, n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Iteratively build the sequence from the base cases, keeping only the last two values at each step — no need for recursion or memoization tables.

```python
def fib(self, n: int) -> int:
    prev, curr = 0, 1
    for _ in range(n):
        prev, curr = curr, prev + curr
    return prev
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Iterative Bottom-Up) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
The naive recursive Fibonacci is exponential; an iterative two-variable rolling sum is the standard O(n) fix.

---

## Reference
- LeetCode #509 — Fibonacci Number
