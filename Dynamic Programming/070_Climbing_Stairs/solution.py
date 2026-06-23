# ─────────────────────────────────────────────────
# APPROACH 1: Iterative DP (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

# ─────────────────────────────────────────────────
# APPROACH 2: Memoization
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
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

# ─────────────────────────────────────────────────
# APPROACH 2: Matrix exponentiation
# Time: O(log n) | Space: O(1)
# ─────────────────────────────────────────────────
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
