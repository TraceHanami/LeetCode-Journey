from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Dedupe, Sort, Index
# Why: Sorting a deduplicated set makes picking the third-largest a simple index lookup.
# Time: O(n log n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def thirdMax(self, nums: List[int]) -> int:
        unique = sorted(set(nums))
        if len(unique) >= 3:
            return unique[-3]
        return unique[-1]


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None
        for n in set(nums):
            if first is None or n > first:
                first, second, third = n, first, second
            elif second is None or n > second:
                second, third = n, second
            elif third is None or n > third:
                third = n
        return third if third is not None else first

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
