# 217 — Contains Duplicate

## Problem

A set cannot have duplicates — if set size < array size, duplicates exist.

**Difficulty:** Easy | **Topic:** Hash Tables

**[View on LeetCode](https://leetcode.com/problems/contains-duplicate/)**

**Examples**
```
nums = [1,2,3,1] -> true
nums = [1,2,3,4] -> false
nums = [1,1,1,3,3,4,3,2,4,2-> true
```
---

## Approach 1 — Hash set ✅

**Idea:** return len(set(nums)) < len(nums).

```python
class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 2 — Sort

**Idea:** Sort and check adjacent elements.

```python
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
```

**Complexity:**
- Time: O(n log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Hash set | O(n) | O(n) | ✅ Yes |
| 2 — Sort | O(n log n) | O(1) | No |

---

## Reference

[LeetCode #217 — Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
