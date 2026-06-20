from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Single Pass (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = curr = 0
        for num in nums:
            if num == 1:
                curr += 1
                max_count = max(max_count, curr)
            else:
                curr = 0
        return max_count
