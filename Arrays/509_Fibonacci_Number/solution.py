# ─────────────────────────────────────────────────
# APPROACH 1: Iterative DP (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# ─────────────────────────────────────────────────
# APPROACH 2: Memoization
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution2:
    def fib(self, n: int) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i):
            if i <= 1:
                return i
            return dp(i - 1) + dp(i - 2)

        return dp(n)
        
# ─────────────────────────────────────────────────
# APPROACH 3: Matrix Exponentiation
# Time: O(log n) | Space: O(1)
# ─────────────────────────────────────────────────
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
            result = [[1, 0], [0, 1]] 
            while exp:
                if exp % 2:
                    result = multiply(result, matrix)
                matrix = multiply(matrix, matrix)
                exp //= 2
            return result
        base = [[1, 1], [1, 0]]
        ans = power(base, n - 1)
        return ans[0][0]
