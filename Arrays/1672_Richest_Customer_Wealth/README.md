# 1672 — Richest Customer Wealth

## Problem

Sum each customer's accounts; return the maximum sum.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/richest-customer-wealth/)**

**Examples:**
```
accounts = [[1,2,3],[3,2,1]] -> 6
accounts = [[1,5],[7,3],[3,5]] -> 10
```
---

## Approach 1 — Row sum max ✅

**Idea:** max(sum(row) for row in accounts).

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
- Time: O(n*m)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Row sum max | O(n*m) | O(1) | ✅ Yes |

---

## Reference

[LeetCode #1672 — Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/)
