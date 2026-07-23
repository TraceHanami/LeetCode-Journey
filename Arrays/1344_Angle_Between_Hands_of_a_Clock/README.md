# 1344 — Angle Between Hands of a Clock

## Problem
Given the current time as a pair of hour and minute values, return the smaller angle (in degrees) formed between the hour and minute hands.

**Difficulty:** Medium | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/angle-between-hands-of-a-clock/)**

**Examples:**
```text
Input: hour = 12, minutes = 30
Output: 165
```

---

## My Approaches
### Attempt 1 — Compute Both Hand Angles Directly ✅ Final Accepted Solution
**Why I used it:**
Each hand moves at a constant rate per minute — compute both angles from 12 o'clock and take the difference.

```python
def angleClock(self, hour: int, minutes: int) -> float:
    minute_angle = minutes * 6
    hour_angle = (hour % 12) * 30 + minutes * 0.5
    diff = abs(hour_angle - minute_angle)
    return min(diff, 360 - diff)
```

**Complexity:**
- Time: O(1)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
The minute hand moves 6°/minute (360°/60). The hour hand moves 30°/hour plus an extra 0.5°/minute (30°/60) since it creeps forward between hours. Compute both absolute angles from 12, take the difference, then return the smaller of that angle and its complement to 360°.

```python
def angleClock(self, hour: int, minutes: int) -> float:
    minute_angle = minutes * 6
    hour_angle = (hour % 12) * 30 + minutes * 0.5
    diff = abs(hour_angle - minute_angle)
    return min(diff, 360 - diff)
```

### Complexity
- Time: O(1)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Compute Both Hand Angles Directly) | O(1) | O(1) | ✅ |
| Standard Approach 1 | O(1) | O(1) | ✅ |


---

## Key Takeaway
Modeling each hand's angular speed directly (6°/min and 0.5°/min) turns a geometry problem into simple arithmetic.

---

## Reference
- LeetCode #1344 — Angle Between Hands of a Clock
