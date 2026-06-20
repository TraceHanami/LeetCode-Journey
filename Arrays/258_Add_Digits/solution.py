# ─────────────────────────────────────────────────
# APPROACH 1: Digital Root Formula (Recommended)
# Time: O(1) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 9 if num % 9 == 0 else num % 9

# ─────────────────────────────────────────────────
# APPROACH 2: Simulation
# Time: O(log n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum(int(d) for d in str(num))
        return num
