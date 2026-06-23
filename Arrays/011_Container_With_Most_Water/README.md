# 11 — Container With Most Water

## Problem

Greedy two-pointer: always move the shorter line inward to maximize area.

**Difficulty:** Med | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/container-with-most-water/)**

**Examples:**
```
height = [1,8,6,2,5,4,8,3,7] -> 49
height = [1,1] -> 1
```
---

## Approach 1 — Two pointers ✅

**Idea:** Start with widest container. Move pointer at shorter height inward. Track max area.

```python
class Solution1:
    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        max_water = 0
        while lo < hi:
            water = min(height[lo], height[hi]) * (hi - lo)
            max_water = max(max_water, water)
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return max_water
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Brute force

**Idea:** Check all pairs. Too slow for large input.

```python
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                max_water = max(max_water, min(height[i], height[j]) * (j - i))
        return max_water
```

**Complexity:**
- Time: O(n²)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Two pointers | O(n) | O(1) | ✅ Yes |
| 2 — Brute force | O(n²) | O(1) | No |

---

## Reference

[LeetCode #11 — Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
