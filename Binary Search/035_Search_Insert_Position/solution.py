from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Binary Search
# Why: Sorted array means the insertion point can be found in O(log n) instead of scanning linearly.
# Time: O(log n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(log n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
