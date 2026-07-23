from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Build a Deduplicated List, Copy Back
# Why: Easiest to reason about — collect unique values first, then overwrite the original array.
# Time: O(n^2)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = []
        for n in nums:
            if n not in unique:
                unique.append(n)
        for i in range(len(unique)):
            nums[i] = unique[i]
        return len(unique)


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
