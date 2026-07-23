from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Set Intersection
# Why: Python's built-in set operations directly express the intersection semantics needed here.
# Time: O(n + m)
# Space: O(n + m)
# ─────────────────────────────────────────────────
class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n + m)
# Space: O(n + m)
# ─────────────────────────────────────────────────
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
