from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: In-Place Prefix Sum (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

# ─────────────────────────────────────────────────
# APPROACH 2: itertools.accumulate
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution2:
    def runningSum(self, nums: List[int]) -> List[int]:
        import itertools
        return list(itertools.accumulate(nums))
