from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Linear Scan (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def maximumCount(self, nums: List[int]) -> int:
        neg = sum(1 for x in nums if x < 0)
        pos = sum(1 for x in nums if x > 0)
        return max(neg, pos)

# ─────────────────────────────────────────────────
# APPROACH 2: Binary Search
# Time: O(log n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def maximumCount(self, nums: List[int]) -> int:
        import bisect
        neg = bisect.bisect_left(nums, 0)
        pos = len(nums) - bisect.bisect_right(nums, 0)
        return max(neg, pos)
