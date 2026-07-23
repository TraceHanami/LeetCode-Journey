from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Divide Out 2, 3, 5
# Why: Repeatedly strip each allowed prime factor; if only 1 remains, every factor was one of 2, 3, or 5.
# Time: O(log n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for f in [2, 3, 5]:
            while n % f == 0:
                n //= f
        return n == 1


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(log n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for factor in (2, 3, 5):
            while n % factor == 0:
                n //= factor
        return n == 1

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
