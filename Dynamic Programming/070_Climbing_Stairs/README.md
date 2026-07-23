# 070 — Climbing Stairs

## Problem
You can climb 1 or 2 steps at a time. Given n steps, return the number of distinct ways to reach the top.

**Difficulty:** Easy | **Topic:** Dynamic Programming
**[View on LeetCode](https://leetcode.com/problems/climbing-stairs/)**

**Examples:**
```text
Input: n = 3
Output: 3  (1+1+1, 1+2, 2+1)
```

---

## My Approaches
### Attempt 1 — Iterative Fibonacci-Style DP ✅ Final Accepted Solution
**Why I used it:**
Recognized ways(n) = ways(n-1) + ways(n-2), so just build it up bottom-up with two rolling variables.

```python
def climbStairs(self, n: int) -> int:
    if n <= 2:
        return n
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
This is Fibonacci in disguise: to reach step n, your last move was either a 1-step from n-1 or a 2-step from n-2, so ways(n) = ways(n-1) + ways(n-2). Track only the last two values instead of a full DP array.

```python
def climbStairs(self, n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Iterative Fibonacci-Style DP) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
Recognizing the recurrence as Fibonacci immediately suggests the O(1)-space rolling-variable optimization instead of a full DP table.

---

## Reference
- LeetCode #70 — Climbing Stairs
