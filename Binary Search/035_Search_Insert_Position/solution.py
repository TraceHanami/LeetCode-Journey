from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Binary Search (Recommended)
# Time: O(log n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

# ─────────────────────────────────────────────────
# APPROACH 2: Linear Scan
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)
