from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Two Pointers (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for num in nums:
            if num != 0:
                nums[write] = num
                write += 1
        while write < len(nums):
            nums[write] = 0
            write += 1

# ─────────────────────────────────────────────────
# APPROACH 2: Swap Partition
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write], nums[i] = nums[i], nums[write]
                write += 1
