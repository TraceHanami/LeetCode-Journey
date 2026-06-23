# 1344 — Angle Between Hands of a Clock

## Problem

Calculate exact angles of hour and minute hands, return the smaller angle.

**Difficulty:** Med | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/angle-between-hands-of-a-clock/)**

**Examples:**
```
hour = 12, minutes = 30 -> 165
hour = 3, minutes = 30 -> 75
hour = 3, minutes = 15 -> 7.5
```
---

## Approach 1 — Math formula ✅

**Idea:** Minute hand: 6*minutes degrees. Hour hand: 30*hour + 0.5*minutes degrees. Return min(diff, 360-diff).

```python
class Solution1:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = 6 * minutes                   # 360/60 = 6 degrees per minute
        hour_angle = 30 * (hour % 12) + 0.5 * minutes  # 360/12 = 30 per hour + 0.5 per minute
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360 - diff)
```

**Complexity:**
- Time: O(1)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Math formula | O(1) | O(1) | ✅ Yes |

---

## Reference

[LeetCode #1344 — Angle Between Hands of a Clock](https://leetcode.com/problems/angle-between-hands-of-a-clock/)
