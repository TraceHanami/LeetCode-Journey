from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Two Pointers (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        max_water = 0
        while lo < hi:
            water = min(height[lo], height[hi]) * (hi - lo)
            max_water = max(max_water, water)
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return max_water

# ─────────────────────────────────────────────────
# APPROACH 2: Brute Force
# Time: O(n²) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                max_water = max(max_water, min(height[i], height[j]) * (j - i))
        return max_water
