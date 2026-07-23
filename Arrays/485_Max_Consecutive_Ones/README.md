# 485 — Max Consecutive Ones

## Problem
Given a binary array, return the maximum number of consecutive 1's.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/max-consecutive-ones/)**

**Examples:**
```text
Input: nums = [1,1,0,1,1,1]
Output: 3
```

---

## My Approaches
### Attempt 1 — Running Streak Counter ✅ Final Accepted Solution
**Why I used it:**
Track the current streak of 1s, resetting to 0 on any 0, and keep the max streak seen.

```python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    best = 0
    streak = 0
    for n in nums:
        if n == 1:
            streak += 1
            best = max(best, streak)
        else:
            streak = 0
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
A single pass with a running counter that resets on every 0 — the maximum value the counter reaches is the answer.

```python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    best = streak = 0
    for n in nums:
        streak = streak + 1 if n == 1 else 0
        best = max(best, streak)
    return best
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Running Streak Counter) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
A running streak counter that resets on the 'break' condition is the go-to pattern for consecutive-run problems.

---

## Reference
- LeetCode #485 — Max Consecutive Ones
