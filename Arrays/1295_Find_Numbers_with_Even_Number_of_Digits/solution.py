from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: String Length Check (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if len(str(num)) % 2 == 0)

# ─────────────────────────────────────────────────
# APPROACH 2: Math log10
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def findNumbers(self, nums: List[int]) -> int:
        import math
        return sum(1 for num in nums if (math.floor(math.log10(num)) + 1) % 2 == 0)
