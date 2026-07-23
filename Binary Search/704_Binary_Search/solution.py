from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Classic Binary Search
# Why: Textbook implementation — halve the search space every step.
# Time: O(log n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(log n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
