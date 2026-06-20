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
