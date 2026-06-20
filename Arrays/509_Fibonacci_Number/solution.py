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
