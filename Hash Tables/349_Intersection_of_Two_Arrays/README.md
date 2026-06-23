# 349 — Intersection of Two Arrays

## Problem

Convert one array to set, filter the other by membership.

**Difficulty:** Easy | **Topic:** Hash Tables

**[View on LeetCode](https://leetcode.com/problems/intersection-of-two-arrays/)**

**Examples:**
```
nums1 = [1,2,2,1], nums2 = [2,2] -> [2]
nums1 = [4,9,5], nums2 = [9,4,9,8,4] ->[9,4]
```
---

## Approach 1 — Set intersection ✅

**Idea:** set(nums1) & set(nums2) directly gives unique intersection.

```python
class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
```

**Complexity:**
- Time: O(n+m)
- Space: O(n)

---

## Approach 2 — Sort and two pointers

**Idea:** Sort both. Two pointers advance on mismatch, record match and advance both.

```python
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
```

**Complexity:**
- Time: O(n log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Set intersection | O(n+m) | O(n) | ✅ Yes |
| 2 — Sort and two pointers | O(n log n) | O(1) | No |

---

## Reference

[LeetCode #349 — Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)
