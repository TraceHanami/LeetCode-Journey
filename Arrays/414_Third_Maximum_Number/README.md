# 414 — Third Maximum Number

## Problem

Track top three distinct maximums in a single pass.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/third-maximum-number/)**

**Examples:**
```
nums = [3,2,1] -> 1
nums = [1,2] -> 2
```

---

## Approach 1 — Three variables ✅

**Idea:** Maintain first, second, third max. Skip duplicates. Return third if exists, else first.

```python
class Solution1:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        for num in nums:
            if num in (first, second, third):
                continue
            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num
        return third if third != float('-inf') else first
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Sorted set

**Idea:** Use sorted set, pick third from end if size >= 3.

```python
class Solution2:
    def thirdMax(self, nums: List[int]) -> int:
        unique = sorted(set(nums), reverse=True)
        return unique[2] if len(unique) >= 3 else unique[0]
```

**Complexity:**
- Time: O(n log n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Three variables | O(n) | O(1) | ✅ Yes |
| 2 — Sorted set | O(n log n) | O(n) | No |

---

## Reference

[LeetCode #414 — Third Maximum Number](https://leetcode.com/problems/third-maximum-number/)
