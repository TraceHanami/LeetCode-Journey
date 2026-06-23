# 485 — Max Consecutive Ones

## Problem

Single pass: increment counter on 1, reset on 0, track max.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/max-consecutive-ones/)**

**Examples:**
```
nums = [1,1,0,1,1,1] -> 3
nums = [1,0,1,1,0,1] ->2
---

## Approach 1 — Single pass ✅

**Idea:** curr count resets to 0 on 0. max_count updated each step.

```python
class Solution1:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = curr = 0
        for num in nums:
            if num == 1:
                curr += 1
                max_count = max(max_count, curr)
            else:
                curr = 0
        return max_count
```
**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Single pass | O(n) | O(1) | ✅ Yes |

---

## Reference

[LeetCode #485 — Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/)
