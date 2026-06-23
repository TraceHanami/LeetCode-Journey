# 1732 — Find the Highest Altitude

## Problem

Running prefix sum of altitude gains; track maximum.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/find-the-highest-altitude/)**

**Examples:**
```
gain = [-5,1,5,0,-7] -> 1
gain = [-4,-3,-2,-1,4,3,2] -> 2
```

---

## Approach 1 — Prefix sum ✅

**Idea:** Maintain running altitude sum, update max at each step.

```python
class Solution1:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = curr = 0
        for g in gain:
            curr += g
            max_alt = max(max_alt, curr)
        return max_alt
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Prefix sum | O(n) | O(1) | ✅ Yes |

---

## Reference

[LeetCode #1732 — Find the Highest Altitude](https://leetcode.com/problems/find-the-highest-altitude/)
