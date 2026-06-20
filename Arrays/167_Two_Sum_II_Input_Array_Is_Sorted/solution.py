from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Two Pointers (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            s = numbers[lo] + numbers[hi]
            if s == target:
                return [lo + 1, hi + 1]
            elif s < target:
                lo += 1
            else:
                hi -= 1

# ─────────────────────────────────────────────────
# APPROACH 2: Binary Search
# Time: O(n log n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        import bisect
        for i, num in enumerate(numbers):
            comp = target - num
            j = bisect.bisect_left(numbers, comp, i + 1)
            if j < len(numbers) and numbers[j] == comp:
                return [i + 1, j + 1]
