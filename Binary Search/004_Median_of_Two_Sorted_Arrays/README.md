# 004 — Median of Two Sorted Arrays

## Problem
Given two sorted integer arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should ideally be `O(log(m + n))`.

**Difficulty:** Hard | **Topic:** Binary Search
**[View on LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/)**

**Examples:**
```text
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: Merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: Merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

---

## My Approaches
### Attempt 1 — Merge and Sort
**Why I used it:**
Combines both sorted lists into a single list using `extend()`, sorts the unified array using Python's built-in `sort()`, and indexes the middle element(s) directly to compute the median.

```python
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
```

**Algorithm Steps:**
1. Extend `nums1` in place with all elements of `nums2`.
2. Sort the combined array `nums1` in non-decreasing order using Python's Timsort.
3. Compute the length `n = len(nums1)`.
4. If `n` is even, return the average of the two middle elements at indices `n // 2 - 1` and `n // 2`.
5. If `n` is odd, return the middle element at index `n // 2`.

**Complexity:**
- Time: O((m + n) log(m + n)) — extending takes O(n) time, and sorting `m + n` elements with Timsort requires O((m + n) log(m + n)) comparisons.
- Space: O(m + n) auxiliary space — resizing `nums1` in place requires reallocating internal list capacity for up to `m + n` elements (O(n) extra items appended), and Python's Timsort uses up to O((m + n) / 2) temporary memory for merge runs.

---

---

## Standard Approach
### Standard Approach 1 — Binary Search Partition ✅ Recommended
### Idea
Instead of merging and sorting, partition both sorted arrays into left and right halves such that the total number of elements in the combined left half equals `(m + n + 1) // 2`. Binary search is conducted on the partition point `i` of the smaller array (say `nums1` of length `m <= n`). For partition index `i` in `nums1`, the corresponding partition index in `nums2` is fixed at `j = (m + n + 1) // 2 - i`. A partition is correct when `maxLeft1 <= minRight2` and `maxLeft2 <= minRight1`. Once the correct partition is found:
- If `m + n` is odd, the median is `max(maxLeft1, maxLeft2)`.
- If `m + n` is even, the median is the average of `max(maxLeft1, maxLeft2)` and `min(minRight1, minRight2)`.

```python
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
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
```

### Complexity
- Time: O(log(min(m, n))) — binary search operates on the smaller array of size `min(m, n)`.
- Space: O(1) auxiliary space — only scalar pointers and boundary values are stored.

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Approach (Merge and Sort) | O((m + n) log(m + n)) | O(m + n) | ❌ |
| Standard Approach (Binary Search Partition) | O(log(min(m, n))) | O(1) | ✅ |

---

## Key Takeaway
Merging and sorting is simple to implement but discards the fact that both input arrays are already sorted. By binary searching the partition boundary between the two arrays, we achieve the optimal O(log(min(m, n))) time complexity and O(1) auxiliary space.

---

## Reference
- LeetCode #4 — Median of Two Sorted Arrays
