# 2529 — Maximum Count of Positive Integer and Negative Integer

## Problem

Count negatives and positives separately (zeros excluded); return the larger count.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/)**

**Examples:**
```
nums = [-2,-1,-1,1,2,3] -> 3
nums = [-3,-2,-1,0,0,1,2] -> 3
nums = [5,20,66,1314] -> 4
```

---

## Approach 1 — Linear scan ✅

**Idea:** Count neg (< 0) and pos (> 0). Return max of both.

```python
class Solution1:
    def maximumCount(self, nums: List[int]) -> int:
        neg = sum(1 for x in nums if x < 0)
        pos = sum(1 for x in nums if x > 0)
        return max(neg, pos)
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Binary search

**Idea:** Use bisect to find boundary of negatives and positives.

```python
class Solution2:
    def maximumCount(self, nums: List[int]) -> int:
        import bisect
        neg = bisect.bisect_left(nums, 0)
        pos = len(nums) - bisect.bisect_right(nums, 0)
        return max(neg, pos)
```

**Complexity:**
- Time: O(log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Linear scan | O(n) | O(1) | ✅ Yes |
| 2 — Binary search | O(log n) | O(1) | No |

---

## Reference

[LeetCode #2529 — Maximum Count of Positive Integer and Negative Integer](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/)
