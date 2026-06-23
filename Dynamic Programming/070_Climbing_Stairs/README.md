# 70 — Climbing Stairs

## Problem

At each step you can come from one or two steps back — Fibonacci pattern.

**Difficulty:** Easy | **Topic:** Dynamic Programming

**[View on LeetCode](https://leetcode.com/problems/climbing-stairs/)**

**Examples:**
```
n = 2 -> 2
n = 3 -> 3
```
---

## Approach 1 — Iterative DP ✅

**Idea:** dp[i] = dp[i-1] + dp[i-2]. Use two variables instead of array.

```python
class Solution1:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Memoization

**Idea:** Recursive with cache.

```python
class Solution2:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(i):
            if i <= 2:
                return i
            if i not in memo:
                memo[i] = dp(i - 1) + dp(i - 2)
            return memo[i]
        return dp(n)
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 3 — Matrix exponentiation

**Idea:** Optimal for very large n.

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
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
                if exp & 1:
                    result = multiply(result, matrix)
                matrix = multiply(matrix, matrix)
                exp >>= 1
            return result
        base = [[1, 1], [1, 0]]
        res = power(base, n)
        return res[0][1]
```

**Complexity:**
- Time: O(log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Iterative DP | O(n) | O(1) | ✅ Yes |
| 2 — Memoization | O(n) | O(n) | No |
| 3 — Matrix exponentiation | O(log n) | O(1) | No |

---

## Reference

[LeetCode #70 — Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
