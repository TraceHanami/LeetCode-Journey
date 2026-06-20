from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Hash Map One Pass (Recommended)
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

# ─────────────────────────────────────────────────
# APPROACH 2: Brute Force
# Time: O(n²) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# ─────────────────────────────────────────────────
# APPROACH 3: Sort + Two Pointers
# Time: O(n log n) | Space: O(n)
# Note: requires tracking original indices
# ─────────────────────────────────────────────────
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = sorted(enumerate(nums), key=lambda x: x[1])
        lo, hi = 0, len(indexed) - 1
        while lo < hi:
            s = indexed[lo][1] + indexed[hi][1]
            if s == target:
                return [indexed[lo][0], indexed[hi][0]]
            elif s < target:
                lo += 1
            else:
                hi -= 1
