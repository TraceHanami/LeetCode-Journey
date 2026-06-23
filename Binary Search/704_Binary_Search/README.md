# 704 — Binary Search

## Problem

Classic binary search — halve the search space each iteration.

**Difficulty:** Easy | **Topic:** Binary Search

**[View on LeetCode](https://leetcode.com/problems/binary-search/)**

**Examples:**
```
nums = [-1,0,3,5,9,12], target = 9 -> 4
nums = [-1,0,3,5,9,12], target = 2 -> -1
```
---

## Approach 1 — Iterative binary search ✅

**Idea:** lo=0, hi=n-1. mid=(lo+hi)//2. Adjust lo or hi based on comparison.

```python
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
```

**Complexity:**
- Time: O(log n)
- Space: O(1)

---

## Approach 2 — Recursive binary search

**Idea:** Same logic with recursive calls. Stack space is the trade-off.

```python
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        def helper(lo, hi):
            if lo > hi:
                return -1
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return helper(mid + 1, hi)
            else:
                return helper(lo, mid - 1)
        return helper(0, len(nums) - 1)
```

**Complexity:**
- Time: O(log n)
- Space: O(log n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Iterative binary search | O(log n) | O(1) | ✅ Yes |
| 2 — Recursive binary search | O(log n) | O(log n) | No |

---

## Reference

[LeetCode #704 — Binary Search](https://leetcode.com/problems/binary-search/)
