# ─────────────────────────────────────────────────
# APPROACH 1: Binary Search (Recommended)
# Time: O(log x) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi

# ─────────────────────────────────────────────────
# APPROACH 2: Newton's Method
# Time: O(log x) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r
