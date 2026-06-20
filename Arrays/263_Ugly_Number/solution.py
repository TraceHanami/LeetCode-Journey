# ─────────────────────────────────────────────────
# APPROACH 1: Repeated Division (Recommended)
# Time: O(log n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        return n == 1
