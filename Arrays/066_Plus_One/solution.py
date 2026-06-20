from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Reverse Carry Propagation (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

# ─────────────────────────────────────────────────
# APPROACH 2: Convert to Int
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, str(int(''.join(map(str, digits))) + 1)))
