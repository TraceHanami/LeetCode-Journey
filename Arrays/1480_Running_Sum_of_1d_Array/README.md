# 1480 — Running Sum of 1d Array

## Problem

Each element becomes the sum of all elements up to and including itself.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/)**

**Examples:**
```
nums = [1,2,3,4] -> [1,3,6,10] 
nums = [1,1,1,1,1] -> [1,2,3,4,5]
---

## Approach 1 — In-place prefix sum ✅

**Idea:** nums[i] += nums[i-1] for i in range(1, n).

```python
class Solution1:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — itertools.accumulate

**Idea:** list(itertools.accumulate(nums)).

```python
class Solution2:
    def runningSum(self, nums: List[int]) -> List[int]:
        import itertools
        return list(itertools.accumulate(nums))
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — In-place prefix sum | O(n) | O(1) | ✅ Yes |
| 2 — itertools.accumulate | O(n) | O(n) | No |

---

## Reference

[LeetCode #1480 — Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/)
