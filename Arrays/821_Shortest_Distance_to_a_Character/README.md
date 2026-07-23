# 821 — Shortest Distance to a Character

## Problem
Given a string s and a character c that occurs in s, return an array where answer[i] is the distance from index i to the closest occurrence of c.

**Difficulty:** Medium | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/shortest-distance-to-a-character/)**

**Examples:**
```text
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
```

---

## My Approaches
### Attempt 1 — Brute Force — Compare Against Every Occurrence
**Why I used it:**
Collect all positions of c, then for each index find the closest one by scanning the whole list.

```python
def shortestToChar(self, s: str, c: str) -> List[int]:
    positions = [i for i in range(len(s)) if s[i] == c]
    result = []
    for i in range(len(s)):
        result.append(min(abs(i - p) for p in positions))
    return result
```

**Complexity:**
- Time: O(n * k)
- Space: O(k)

---
### Attempt 2 — Two-Pass Sweep (Optimal) ✅ Final Accepted Solution
**Why I used it:**
One left-to-right pass tracks distance since the last occurrence; one right-to-left pass tracks distance to the next occurrence — take the min of both.

```python
def shortestToChar(self, s: str, c: str) -> List[int]:
    n = len(s)
    result = [0] * n
    prev = float('-inf')
    for i in range(n):
        if s[i] == c:
            prev = i
        result[i] = i - prev
    prev = float('inf')
    for i in range(n - 1, -1, -1):
        if s[i] == c:
            prev = i
        result[i] = min(result[i], prev - i)
    return result
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Two linear sweeps: left-to-right tracks the distance since the most recent occurrence of c; right-to-left tracks the distance to the next occurrence. Taking the minimum of both at each index gives the true shortest distance without ever comparing against every occurrence.

```python
def shortestToChar(self, s: str, c: str) -> List[int]:
    n = len(s)
    ans = [0] * n
    last = float('-inf')
    for i in range(n):
        if s[i] == c:
            last = i
        ans[i] = i - last
    last = float('inf')
    for i in range(n - 1, -1, -1):
        if s[i] == c:
            last = i
        ans[i] = min(ans[i], last - i)
    return ans
```

### Complexity
- Time: O(n)
- Space: O(n)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Two-Pass Sweep (Optimal)) | O(n) | O(n) | ✅ |
| Standard Approach 1 | O(n) | O(n) | ✅ |
| Brute Force — Compare Against Every Occurrence | O(n * k) | O(k) | ❌ |


---

## Key Takeaway
Two direction-aware sweeps replace an O(n·k) brute-force comparison with a single pair of O(n) passes.

---

## Reference
- LeetCode #821 — Shortest Distance to a Character
