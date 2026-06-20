from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Two Pointers (Recommended)
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        lo, hi, pos = 0, n - 1, n - 1
        while lo <= hi:
            if abs(nums[lo]) >= abs(nums[hi]):
                result[pos] = nums[lo] ** 2
                lo += 1
            else:
                result[pos] = nums[hi] ** 2
                hi -= 1
            pos -= 1
        return result

# ─────────────────────────────────────────────────
# APPROACH 2: Sort Squares
# Time: O(n log n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x ** 2 for x in nums)
