# 509 — Fibonacci Number

## Problem

Bottom-up DP with two variables — no array needed.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/fibonacci-number/)**

**Examples:**
```
n = 2 -> 1
n = 3 -> 2
n = 4 -> 3
```

---

## Approach 1 — Iterative DP ✅

**Idea:** Track prev two values, iterate to n.

```python
class Solution1:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Recursive with memoization

**Idea:** Cache results to avoid recomputation.

```python
class Solution2:
    def fib(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i):
            if i <= 1:
                return i
            return dp(i - 1) + dp(i - 2)

        return dp(n)
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 3 — Matrix exponentiation

**Idea:** Fast method for very large n.

```python
class Solution3:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        def multiply(A, B):
            return [
                [
                    A[0][0] * B[0][0] + A[0][1] * B[1][0],
                    A[0][0] * B[0][1] + A[0][1] * B[1][1]
                ],
                [
                    A[1][0] * B[0][0] + A[1][1] * B[1][0],
                    A[1][0] * B[0][1] + A[1][1] * B[1][1]
                ]
            ]

        def power(matrix, exp):
            result = [[1, 0], [0, 1]]  # Identity matrix

            while exp:
                if exp % 2:
                    result = multiply(result, matrix)

                matrix = multiply(matrix, matrix)
                exp //= 2

            return result

        base = [[1, 1], [1, 0]]
        ans = power(base, n - 1)

        return ans[0][0]
```

**Complexity:**
- Time: O(log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Iterative DP | O(n) | O(1) | ✅ Yes |
| 2 — Recursive with memoization | O(n) | O(n) | No |
| 3 — Matrix exponentiation | O(log n) | O(1) | No |

---

## Reference

[LeetCode #509 — Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
