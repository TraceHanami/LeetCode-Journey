from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Two Pointer (Optimal)
# Why: The widest container is a good starting point; moving the shorter wall inward is the only move that can possibly increase area.
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        m = 0
        while i < j:
            w = j - i
            a = w * min(height[i], height[j])
            m = max(m, a)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return m


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            width = right - left
            best = max(best, width * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
