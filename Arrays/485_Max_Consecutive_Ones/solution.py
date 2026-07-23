from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Running Streak Counter
# Why: Track the current streak of 1s, resetting to 0 on any 0, and keep the max streak seen.
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        streak = 0
        for n in nums:
            if n == 1:
                streak += 1
                best = max(best, streak)
            else:
                streak = 0
        return best


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = streak = 0
        for n in nums:
            streak = streak + 1 if n == 1 else 0
            best = max(best, streak)
        return best

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
