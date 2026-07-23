from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Right-to-Left Carry Propagation
# Why: Mirrors how you'd add 1 by hand — carry only propagates while digits are 9.
# Time: O(n)
# Space: O(1) extra (O(n) for the new array on all-9s)
# ─────────────────────────────────────────────────
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1) extra
# ─────────────────────────────────────────────────
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
