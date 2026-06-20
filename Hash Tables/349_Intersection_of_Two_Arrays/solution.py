from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Set Intersection (Recommended)
# Time: O(n+m) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

# ─────────────────────────────────────────────────
# APPROACH 2: Sort and Two Pointers
# Time: O(n log n + m log m) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result
