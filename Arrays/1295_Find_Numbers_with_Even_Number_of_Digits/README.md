# 1295 — Find Numbers with Even Number of Digits

## Problem

Count digits in each number; count those with even digit length.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/)**

**Examples:**
```
nums = [12,345,2,6,7896] -> 2
nums = [555,901,482,1771] -> 1
```
---

## Approach 1 — String length check ✅

**Idea:** len(str(num)) % 2 == 0 for each number.

```python
class Solution1:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if len(str(num)) % 2 == 0)
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Math log10

**Idea:** floor(log10(num)) + 1 gives digit count.

```python
class Solution2:
    def findNumbers(self, nums: List[int]) -> int:
        import math
        return sum(1 for num in nums if (math.floor(math.log10(num)) + 1) % 2 == 0)
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — String length check | O(n) | O(1) | ✅ Yes |
| 2 — Math log10 | O(n) | O(1) | No |

---

## Reference

[LeetCode #1295 — Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/)
