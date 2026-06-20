from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Gauss Sum (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

# ─────────────────────────────────────────────────
# APPROACH 2: XOR
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i, num in enumerate(nums):
            result ^= i ^ num
        return result

# ─────────────────────────────────────────────────
# APPROACH 3: Sort
# Time: O(n log n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if i != num:
                return i
        return len(nums)
