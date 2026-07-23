from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Square Then Sort
# Why: Simplest correct approach — square every value and let sort() handle ordering.
# Time: O(n log n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        return sorted(nums)


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        return result

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
