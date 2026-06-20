from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Dutch National Flag (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        lo, mid, hi = 0, 0, len(nums) - 1
        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1

# ─────────────────────────────────────────────────
# APPROACH 2: Count and Fill
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        c0, c1, c2 = nums.count(0), nums.count(1), nums.count(2)
        nums[:c0] = [0] * c0
        nums[c0:c0+c1] = [1] * c1
        nums[c0+c1:] = [2] * c2
