from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Iterative Binary Search (Recommended)
# Time: O(log n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

# ─────────────────────────────────────────────────
# APPROACH 2: Recursive Binary Search
# Time: O(log n) | Space: O(log n)
# ─────────────────────────────────────────────────
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        def helper(lo, hi):
            if lo > hi:
                return -1
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return helper(mid + 1, hi)
            else:
                return helper(lo, mid - 1)
        return helper(0, len(nums) - 1)
