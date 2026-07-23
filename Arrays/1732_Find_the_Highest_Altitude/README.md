# 1732 — Find the Highest Altitude

## Problem
Given the net altitude gains between consecutive points on a biking trip, return the highest altitude reached, starting from altitude 0.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/find-the-highest-altitude/)**

**Examples:**
```text
Input: gain = [-5,1,5,0,-7]
Output: 1
```

---

## My Approaches
### Attempt 1 — Running Total, Track the Max ✅ Final Accepted Solution
**Why I used it:**
The altitude at each point is a prefix sum of the gains — track the running total and remember its peak.

```python
def largestAltitude(self, gain: List[int]) -> int:
    best = 0
    total = 0
    for g in gain:
        total += g
        best = max(best, total)
    return best
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Altitude at each point is simply the cumulative sum of gains so far, starting at 0 — track the running sum and keep the highest value seen.

```python
def largestAltitude(self, gain: List[int]) -> int:
    altitude = highest = 0
    for g in gain:
        altitude += g
        highest = max(highest, altitude)
    return highest
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Running Total, Track the Max) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
Another prefix-sum-in-disguise problem — the answer is just the max of the running total.

---

## Reference
- LeetCode #1732 — Find the Highest Altitude
