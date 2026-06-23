# 268 — Missing Number

## Problem

Expected sum minus actual sum gives the missing number.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/missing-number/)**

**Examples:**
```
nums = [3,0,1] -> 2
nums = [0,1] -> 2
nums = [9,6,4,2,3,5,7,0,1] -> 8
```
---

## Approach 1 — Gauss sum ✅

**Idea:** Missing = n*(n+1)//2 - sum(nums).

```python
class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — XOR

**Idea:** XOR all indices and values — duplicates cancel, leaving the missing number.

```python
class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for i, num in enumerate(nums):
            result ^= i ^ num
        return result
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 3 — Sort

**Idea:** Sort and check if nums[i] == i.

```python
class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if i != num:
                return i
        return len(nums)
```

**Complexity:**
- Time: O(n log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Gauss sum | O(n) | O(1) | ✅ Yes |
| 2 — XOR | O(n) | O(1) | No |
| 3 — Sort | O(n log n) | O(1) | No |

---

## Reference

[LeetCode #268 — Missing Number](https://leetcode.com/problems/missing-number/)
