# 977 — Squares of a Sorted Array

## Problem

Two pointers from both ends — largest squares always at the extremes.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array/)**

**Examples:**
```
nums = [-4,-1,0,3,10] -> [0,1,9,16,100]
nums = [-7,-3,2,3,11] -> [4,9,9,49,121]
```
---

## Approach 1 — Two pointers ✅

**Idea:** Compare abs values at left and right pointers. Place larger square at end of result. Move that pointer inward.

```python
class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        lo, hi, pos = 0, n - 1, n - 1
        while lo <= hi:
            if abs(nums[lo]) >= abs(nums[hi]):
                result[pos] = nums[lo] ** 2
                lo += 1
            else:
                result[pos] = nums[hi] ** 2
                hi -= 1
            pos -= 1
        return result
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 2 — Sort squares

**Idea:** Square all elements, sort. Simple but not optimal.

```python
class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(x ** 2 for x in nums)
```

**Complexity:**
- Time: O(n log n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Two pointers | O(n) | O(n) | ✅ Yes |
| 2 — Sort squares | O(n log n) | O(n) | No |

---

## Reference

[LeetCode #977 — Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)
