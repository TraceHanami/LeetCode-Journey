from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: XOR of Indices and Values
# Why: XORing every index and every value cancels out all present pairs, leaving only the missing number.
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, n in enumerate(nums):
            missing ^= i ^ n
        return missing


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, n in enumerate(nums):
            missing ^= i ^ n
        return missing

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
