from typing import List

# ─────────────────────────────────────────────────
# MY APPROACH: Merge and Sort
# Why: Combines both lists with extend(), sorts in-place, and
#      retrieves the middle element(s) to compute the median.
# Time: O((m + n) log(m + n))
# Space: O(m + n) auxiliary space (list resizing buffer + Timsort scratch space)
# ─────────────────────────────────────────────────
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()

        n = len(nums1)

        if n % 2 == 0:
            s = (nums1[n // 2 - 1] + nums1[n // 2]) / 2
        else:
            s = nums1[n // 2]

        return s


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH: Binary Search Partition
# Why: Binary search the partition of the smaller array to divide
#      both arrays into equal left/right halves in logarithmic time.
# Time: O(log(min(m, n)))
# Space: O(1) auxiliary space
# ─────────────────────────────────────────────────
class SolutionBinarySearch:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i

            maxLeft1 = float('-inf') if i == 0 else nums1[i - 1]
            minRight1 = float('inf') if i == m else nums1[i]

            maxLeft2 = float('-inf') if j == 0 else nums2[j - 1]
            minRight2 = float('inf') if j == n else nums2[j]

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            elif maxLeft1 > minRight2:
                high = i - 1
            else:
                low = i + 1

        return 0.0


# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    sol_opt = SolutionBinarySearch()

    # Test 1: Odd total length
    res1 = sol.findMedianSortedArrays([1, 3], [2])
    res1_opt = sol_opt.findMedianSortedArrays([1, 3], [2])
    print(f"Test 1: {res1} (optimal: {res1_opt})")
    assert res1 == 2.0 and res1_opt == 2.0

    # Test 2: Even total length
    res2 = sol.findMedianSortedArrays([1, 2], [3, 4])
    res2_opt = sol_opt.findMedianSortedArrays([1, 2], [3, 4])
    print(f"Test 2: {res2} (optimal: {res2_opt})")
    assert res2 == 2.5 and res2_opt == 2.5

    print("All tests passed!")
