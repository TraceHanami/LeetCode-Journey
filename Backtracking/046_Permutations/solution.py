from typing import *

# ==================================================
# MY APPROACH (Original Submission)
# ==================================================
# Why:
# Classic "choose, explore, un-choose" backtracking; a linear
# membership check against the current path avoids reusing a number.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for num in nums:
                if num not in path:
                    path.append(num)
                    backtrack(path)
                    path.pop()

        backtrack([])
        return ans
# Time: O(n^2 * n!)
# Space: O(n) recursion + O(n * n!) output

# ==================================================
# ALTERNATIVE APPROACHES
# ==================================================

# Approach 2 - Used-Flags Array Instead of `in` Check
class SolutionUsedFlags:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False] * len(nums)
        path = []

        def backtrack():
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(num)
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return ans
# Time: O(n * n!)
# Space: O(n) recursion + O(n) used array + O(n * n!) output

# Approach 3 - Swap-Based In-Place Backtracking
class SolutionSwap:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(start):
            if start == len(nums):
                ans.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return ans
# Time: O(n * n!)
# Space: O(n) recursion + O(n * n!) output

# ==================================================
# OPTIMAL APPROACH
# ==================================================
# Same swap-based in-place partitioning as Approach 3 - the most
# efficient in practice since it avoids both the `in` scan and an
# extra used array.

class SolutionOptimal:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def backtrack(start):
            if start == n:
                ans.append(nums[:])
                return
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return ans
# Time: O(n * n!)
# Space: O(n) recursion + O(n * n!) output
