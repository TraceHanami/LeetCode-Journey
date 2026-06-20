from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Two Pointers (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for num in nums:
            if num != val:
                nums[write] = num
                write += 1
        return write

# ─────────────────────────────────────────────────
# APPROACH 2: Swap with End
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n
