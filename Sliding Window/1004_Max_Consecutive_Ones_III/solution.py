from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Variable-Size Sliding Window Tracking Zero Count
# Why: Expand the window freely, but once the number of 0's inside exceeds k, shrink from the left until it's back within budget.
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = zeros = best = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            best = max(right - left + 1, best)
        return best


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = zero_count = best = 0
        for right, val in enumerate(nums):
            if val == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            best = max(best, right - left + 1)
        return best

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
