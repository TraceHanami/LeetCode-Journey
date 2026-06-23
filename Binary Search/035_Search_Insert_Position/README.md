# 35 — Search Insert Position

## Problem

Binary search — if not found, left pointer is the insert position.

**Difficulty:** Easy | **Topic:** Binary Search

**[View on LeetCode](https://leetcode.com/problems/search-insert-position/)**

**Exampels:**
```
nums = [1,3,5,6], target = 5 -> 2
nums = [1,3,5,6], target = 2 -> 1
nums = [1,3,5,6], target = 7 -> 4
```
---

## Approach 1 — Binary search ✅

**Idea:** Standard binary search. Return lo when target not found — lo is the insert position.

```python
 class Solution1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
```

**Complexity:**
- Time: O(log n)
- Space: O(1)

---

## Approach 2 — Linear scan

**Idea:** Scan left to right, return index of first element >= target.

```python
class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Binary search | O(log n) | O(1) | ✅ Yes |
| 2 — Linear scan | O(n) | O(1) | No |

---

## Reference

[LeetCode #35 — Search Insert Position](https://leetcode.com/problems/search-insert-position/)
