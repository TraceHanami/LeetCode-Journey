from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Swap Every Non-Zero Forward
# Why: First pass — always swap, even when i == l, which does redundant self-swaps but is still correct.
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1

# ─────────────────────────────────────────────────
# MY APPROACH 2: Swap Only When Needed
# Why: Skip the swap when i == l to avoid pointless self-swaps — a small but meaningful cleanup.
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != l:
                    nums[l], nums[i] = nums[i], nums[l]
                l += 1


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
