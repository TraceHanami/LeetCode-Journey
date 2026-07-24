# 50 — Pow(x, n)

## Problem

Implement `pow(x, n)`, computing `x` raised to the power `n` (`n` can be negative or zero).

**Difficulty:** Medium | **Topic:** Math / Divide and Conquer

**[View on LeetCode](https://leetcode.com/problems/powx-n/)**

**Examples:**

```text
Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.10000, n = 3
Output: 9.26100

Input: x = 2.00000, n = -2
Output: 0.25000
```

---

## My Approach ✅

### Why I Used This Method

Python's built-in `**` operator already handles integer exponentiation correctly, including negative exponents (returning a fraction) and zero (returning 1), so it directly solves the problem without any extra code.

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
```

### Complexity

* Time: O(log n) in practice — CPython's built-in power operator uses exponentiation by squaring internally
* Space: O(1)

---

## Alternative Approaches

### Approach 2 — Naive Repeated Multiplication

#### Idea

Multiply `x` by itself `|n|` times in a loop, then take the reciprocal if `n` is negative. This is what "manually implementing" the operator without any optimization looks like — correct, but far slower for large exponents.

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        result = 1.0
        for _ in range(n):
            result *= x
        return result
```

#### Complexity

* Time: O(n)
* Space: O(1)

---

## Optimal Approach 🚀

### Idea

Exponentiation by squaring: to compute `x^n`, recursively compute `x^(n/2)` and square it, handling the odd-exponent case by multiplying in one extra factor of `x`. This halves the exponent at every step instead of subtracting one, taking the time down from linear to logarithmic — this is the same technique CPython's built-in `**` already uses under the hood, made explicit here.

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(base: float, exp: int) -> float:
            if exp == 0:
                return 1.0
            half = fast_pow(base, exp // 2)
            if exp % 2 == 0:
                return half * half
            return half * half * base

        if n < 0:
            x = 1 / x
            n = -n
        return fast_pow(x, n)
```

### Complexity

* Time: O(log n)
* Space: O(log n) recursion depth (or O(1) if written iteratively)

---

## Comparison

| Approach                  | Time      | Space     | Recommended |
| -------------------------- | --------- | --------- | ----------- |
| My Approach (built-in `**`)| O(log n)* | O(1)      | ✅           |
| Naive Repeated Multiply     | O(n)      | O(1)      | Optional    |
| Optimal (explicit squaring) | O(log n)  | O(log n)  | 🚀          |

\* Relies on the interpreter's internal implementation rather than code written for this solution.

---

## Key Takeaway

Halving the exponent at each recursive step (instead of decrementing it by one) is the core trick behind fast exponentiation — the same divide-and-conquer idea that makes `x^n` computable in logarithmic rather than linear time.

---

## Reference

* LeetCode #50 — Pow(x, n)
