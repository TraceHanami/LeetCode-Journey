# 88 — Merge Sorted Array

## Problem

Fill from the end — compare from back of both arrays to avoid overwriting.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/merge-sorted-array/)**

**Examples:**
```
nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 -> [1,2,2,3,5,6]
nums1 = [1], m = 1, nums2 = [], n = 0 -> [1]
nums1 = [0], m = 0, nums2 = [1], n = 1 -> [1]
```

---

## Approach 1 — Three pointers from end ✅

**Idea:** p1=m-1, p2=n-1, p=m+n-1. Place larger of nums1[p1], nums2[p2] at p. Move pointers.

```python
class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]
```

**Complexity:**
- Time: O(n+m)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Three pointers from end | O(n+m) | O(1) | ✅ Yes |

---

## Reference

[LeetCode #88 — Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
