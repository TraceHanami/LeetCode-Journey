# 167 — Two Sum II Input Array Is Sorted

## Problem

Two pointers from both ends — sorted array makes this O(n).

**Difficulty:** Med | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)**

**Examples:**
```
numbers = [2,7,11,15], target = 9 -> [1,2]
numbers = [2,3,4], target = 6 -> [1,3]
numbers = [-1,0], target = -1 -> [1,2]
```
---

## Approach 1 — Two pointers ✅

**Idea:** Left and right pointers. Sum too small → move left right. Sum too big → move right left. Return when equal.

```python
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            s = numbers[lo] + numbers[hi]
            if s == target:
                return [lo + 1, hi + 1]
            elif s < target:
                lo += 1
            else:
                hi -= 1
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Binary search

**Idea:** For each element, binary search for the complement.

```python
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        import bisect
        for i, num in enumerate(numbers):
            comp = target - num
            j = bisect.bisect_left(numbers, comp, i + 1)
            if j < len(numbers) and numbers[j] == comp:
                return [i + 1, j + 1]
```

**Complexity:**
- Time: O(n log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Two pointers | O(n) | O(1) | ✅ Yes |
| 2 — Binary search | O(n log n) | O(1) | No |

---

## Reference

[LeetCode #167 — Two Sum II Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
