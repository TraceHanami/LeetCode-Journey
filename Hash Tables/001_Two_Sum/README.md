# 1 — Two Sum

## Problem

Store complement in a hash map — O(n) single pass.

**Difficulty:** Easy | **Topic:** Hash Tables

**[View on LeetCode](https://leetcode.com/problems/two-sum/)**

**Examples:**
```
nums = [2,7,11,15], target = 9 -> [0,1]
nums = [3,2,4], target = 6 -> [1,2]
nums = [3,3], target = 6 -> [0,1]
```
---

## Approach 1 — Hash map one pass ✅

**Idea:** For each num, check if complement (target-num) is in map. If yes return indices. Else store num:index.

```python
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 2 — Brute force

**Idea:** Check all pairs. Too slow for large inputs.

```python
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

**Complexity:**
- Time: O(n²)
- Space: O(1)

---

## Approach 3 — Sort and two pointers

**Idea:** Sort with original indices. Two pointers from both ends. Note: doesn't work if original indices needed without extra bookkeeping.

```python
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = sorted(enumerate(nums), key=lambda x: x[1])
        lo, hi = 0, len(indexed) - 1
        while lo < hi:
            s = indexed[lo][1] + indexed[hi][1]
            if s == target:
                return [indexed[lo][0], indexed[hi][0]]
            elif s < target:
                lo += 1
            else:
                hi -= 1
```

**Complexity:**
- Time: O(n log n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Hash map one pass | O(n) | O(n) | ✅ Yes |
| 2 — Brute force | O(n²) | O(1) | No |
| 3 — Sort and two pointers | O(n log n) | O(n) | No |

---

## Reference

[LeetCode #1 — Two Sum](https://leetcode.com/problems/two-sum/)
