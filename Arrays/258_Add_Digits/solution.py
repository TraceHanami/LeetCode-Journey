from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Digital Root Formula
# Why: Recognized this as the digital root, which has a closed-form formula based on mod 9.
# Time: O(1)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 9 if num % 9 == 0 else num % 9


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(1)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
