# 088 — Merge Sorted Array

## Problem
Merge nums2 into nums1 as one sorted array, given nums1 has extra trailing space to hold nums2's elements.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/merge-sorted-array/)**

**Examples:**
```text
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
```

---

## My Approaches
### Attempt 1 — Overwrite Tail, Then Sort ✅ Final Accepted Solution
**Why I used it:**
Simple to write — drop nums2 into the empty slots and let sort() handle ordering.

```python
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    nums1[m:] = nums2
    nums1.sort()
```

**Complexity:**
- Time: O((m+n) log(m+n))
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Merge from the back instead of the front — compare the largest remaining elements of each array and place the bigger one at the end of nums1. This avoids overwriting values in nums1 that haven't been read yet.

```python
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]; i -= 1
        else:
            nums1[k] = nums2[j]; j -= 1
        k -= 1
```

### Complexity
- Time: O(m + n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Overwrite Tail, Then Sort) | O((m+n) log(m+n)) | O(1) | ✅ |
| Standard Approach 1 | O(m + n) | O(1) | ✅ |


---

## Key Takeaway
Merging from the back avoids the need for extra space or sorting — it's the classic two-pointer trick when one array has trailing empty slots.

---

## Reference
- LeetCode #88 — Merge Sorted Array
