# 75 — Sort Colors

## Problem

Dutch National Flag algorithm — three-way partition in a single pass.

**Difficulty:** Med | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/sort-colors/)**

**Examples:**
```
nums = [2,0,2,1,1,0] -> [0,0,1,1,2,2]
nums = [2,0,1] -> [0,1,2]
---

## Approach 1 — Dutch National Flag ✅

**Idea:** Three pointers: lo, mid, hi. Swap 0s to front, 2s to back, 1s stay in middle.

```python
class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        lo, mid, hi = 0, 0, len(nums) - 1
        while mid <= hi:
            if nums[mid] == 0:
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Count and fill

**Idea:** Count 0s, 1s, 2s. Overwrite array with correct counts.

```python
class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        c0, c1, c2 = nums.count(0), nums.count(1), nums.count(2)
        nums[:c0] = [0] * c0
        nums[c0:c0+c1] = [1] * c1
        nums[c0+c1:] = [2] * c2
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Dutch National Flag | O(n) | O(1) | ✅ Yes |
| 2 — Count and fill | O(n) | O(1) | No |

---

## Reference

[LeetCode #75 — Sort Colors](https://leetcode.com/problems/sort-colors/)
