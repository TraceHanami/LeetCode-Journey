from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Built-in isqrt
# Why: Python's math.isqrt computes the integer square root directly and efficiently.
# Time: O(log x)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def mySqrt(self, x: int) -> int:
        return isqrt(x)


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(log x)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
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

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
