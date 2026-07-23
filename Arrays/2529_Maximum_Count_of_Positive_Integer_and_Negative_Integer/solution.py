from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Linear Count
# Why: Scan once, tallying positives and negatives separately, then compare.
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def maximumCount(self, nums: List[int]) -> int:
        pos, neg = 0, 0
        for n in nums:
            if n > 0:
                pos += 1
            elif n < 0:
                neg += 1
        return max(pos, neg)


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = sum(1 for n in nums if n > 0)
        neg = sum(1 for n in nums if n < 0)
        return max(pos, neg)

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
