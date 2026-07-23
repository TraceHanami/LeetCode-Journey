from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Iterative Bottom-Up
# Why: Avoids recursion overhead and exponential blowup by building up from F(0) and F(1).
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def fib(self, n: int) -> int:
        prev, curr = 0, 1
        for _ in range(n):
            prev, curr = curr, prev + curr
        return prev

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
