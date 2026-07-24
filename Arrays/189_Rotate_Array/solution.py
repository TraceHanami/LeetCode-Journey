from typing import *

# ==================================================
# MY APPROACH (Original Submission)
# ==================================================
# Why:
# Slice the last k elements off and put them in front of the rest -
# the most direct expression of "rotate right by k" in Python.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        nums[:]=nums[-k:]+nums[:-k]
# Time: O(n)
# Space: O(n)

# ==================================================
# ALTERNATIVE APPROACHES
# ==================================================

# Approach 2 - Extra Array with Index Mapping (also my original submission)
class SolutionExtraArray:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        d=[0]*len(nums)
        for i in range(len(nums)):
            n=(i+k)%len(nums)
            d[n]=nums[i]
        for i in range(len(nums)):
            nums[i]=d[i]
# Time: O(n)
# Space: O(n)

# ==================================================
# OPTIMAL APPROACH
# ==================================================

class SolutionOptimal:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
# Time: O(n)
# Space: O(1)
