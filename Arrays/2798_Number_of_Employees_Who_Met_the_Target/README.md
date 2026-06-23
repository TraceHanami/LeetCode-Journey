# 2798 — Number of Employees Who Met the Target

## Problem

Count employees whose hours meet or exceed the target.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/number-of-employees-who-met-the-target/)**

**Examples:**
```
hours = [0,1,2,3,4], target = 2 -> 3
hours = [5,1,4,2,2], target = 6 -> 0
```
---

## Approach 1 — Linear scan ✅

**Idea:** Sum 1 for each employee where hours[i] >= target.

```python
class Solution1:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(1 for h in hours if h >= target)
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Linear scan | O(n) | O(1) | ✅ Yes |

---

## Reference

[LeetCode #2798 — Number of Employees Who Met the Target](https://leetcode.com/problems/number-of-employees-who-met-the-target/)
