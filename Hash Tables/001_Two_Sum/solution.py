from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Brute Force (Nested Loops)
# Why: Simplest way to check every pair without thinking about extra space.
# Time: O(n^2)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# ─────────────────────────────────────────────────
# MY APPROACH 2: Hash Map (One Pass)
# Why: Trade space for time — store what's been seen and look up the complement instead of re-scanning.
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, n in enumerate(nums):
            c = target - n
            if c in s:
                return [s[c], i]
            s[n] = i


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                return [seen[complement], i]
            seen[n] = i

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
