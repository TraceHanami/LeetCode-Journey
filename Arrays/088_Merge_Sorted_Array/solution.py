from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Overwrite Tail, Then Sort
# Why: Simple to write — drop nums2 into the empty slots and let sort() handle ordering.
# Time: O((m+n) log(m+n))
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(m + n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]; i -= 1
            else:
                nums1[k] = nums2[j]; j -= 1
            k -= 1

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
