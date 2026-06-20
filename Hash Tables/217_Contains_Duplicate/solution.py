from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Hash Set (Recommended)
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)

# ─────────────────────────────────────────────────
# APPROACH 2: Sort and Check Adjacent
# Time: O(n log n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
