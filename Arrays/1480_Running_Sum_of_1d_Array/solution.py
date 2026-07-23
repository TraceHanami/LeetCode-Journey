from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Accumulate in a Running Total
# Why: Keep a running total and append it as you scan through the array once.
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        total = 0
        for n in nums:
            total += n
            result.append(total)
        return result


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        result = []
        for n in nums:
            total += n
            result.append(total)
        return result

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
