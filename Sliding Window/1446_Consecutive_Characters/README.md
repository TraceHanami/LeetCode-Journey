# 1446 — Consecutive Characters

## Problem
The power of a string is the length of its longest run of consecutive identical characters. Given a string, return its power.

**Difficulty:** Easy | **Topic:** Sliding Window
**[View on LeetCode](https://leetcode.com/problems/consecutive-characters/)**

**Examples:**
```text
Input: s = "leetcode"
Output: 2  (the "ee")
```

---

## My Approaches
### Attempt 1 — Running Streak Counter ✅ Final Accepted Solution
**Why I used it:**
Track the current run length, resetting whenever the character changes, and keep the max.

```python
def maxPower(self, s: str) -> int:
    best = streak = 1
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            streak += 1
        else:
            streak = 1
        best = max(best, streak)
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
A single pass comparing each character to the previous one, extending a running streak on a match and resetting to 1 otherwise — the same running-streak pattern used in Max Consecutive Ones.

```python
def maxPower(self, s: str) -> int:
    best = streak = 1
    for i in range(1, len(s)):
        streak = streak + 1 if s[i] == s[i - 1] else 1
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
This is the same running-streak-with-reset pattern as Max Consecutive Ones — a minimal single-variable sliding window.

---

## Reference
- LeetCode #1446 — Consecutive Characters
