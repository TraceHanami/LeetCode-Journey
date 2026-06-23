# 26 — Remove Duplicates from Sorted Array

## Problem

Two pointers on a sorted array — slow pointer marks unique position.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)**

**Examples:**
```
nums = [1,1,2] -> 2
nums = [0,0,1,1,1,2,2,3,3,4] -> 5 
```
---

## Approach 1 — Two pointers ✅

**Idea:** Slow pointer advances only when nums[fast] != nums[slow].

```python
class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Two pointers | O(n) | O(1) | ✅ Yes |

---

## Reference

[LeetCode #26 — Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
