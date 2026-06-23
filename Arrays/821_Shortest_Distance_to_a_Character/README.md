# 821 — Shortest Distance to a Character

## Problem

Given a string `s` and a character `c`, return an array where each element represents the shortest distance from that index to any occurrence of `c`.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/shortest-distance-to-a-character/)**

**Examples:**
```text
s = "loveleetcode", c = "e" -> [3,2,1,0,1,0,0,1,2,2,1,0]
s = "aaab", c = "b" -> [3,2,1,0]
```

---

## Approach 1 — Store Character Positions

**Idea:**  
First collect all indices where `c` appears. Then, for each position in the string, compute the minimum distance to any stored index.

```python
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        a = []
        r = []
        for i in range(len(s)):
            if s[i] == c:
                a.append(i)
        for i in range(len(s)):
            z = min(abs(i - x) for x in a)
            r.append(z)
        return r
```

### Complexity

- Time: O(n × k)
- Worst Case: O(n²)
- Space: O(n)

---

## Approach 2 — Two-Pass Scan ✅

**Idea:**  
Scan from left to right to find the nearest occurrence on the left. Then scan from right to left to find the nearest occurrence on the right. Take the minimum of both distances.

```python
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [n] * n

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

### Complexity

- Time: O(n)
- Space: O(n)

---

## Comparison

| Approach | Time | Space | Recommended |
|----------|------|--------|-------------|
| Store Character Positions | O(n²) worst case | O(n) | For understanding |
| Two-Pass Scan | O(n) | O(n) | ✅ Yes |

---

## Reference

[LeetCode #821 — Shortest Distance to a Character](https://leetcode.com/problems/shortest-distance-to-a-character/)
