from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Three Variables (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        for num in nums:
            if num in (first, second, third):
                continue
            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num
        return third if third != float('-inf') else first

# ─────────────────────────────────────────────────
# APPROACH 2: Sorted Set
# Time: O(n log n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution2:
    def thirdMax(self, nums: List[int]) -> int:
        unique = sorted(set(nums), reverse=True)
        return unique[2] if len(unique) >= 3 else unique[0]
