# 455 — Assign Cookies

## Problem
Each child has a greed factor and each cookie has a size. A child is content if given a cookie of size >= their greed factor. Maximize the number of content children.

**Difficulty:** Easy | **Topic:** Greedy
**[View on LeetCode](https://leetcode.com/problems/assign-cookies/)**

**Examples:**
```text
Input: g = [1,2,3], s = [1,1]
Output: 1
```

---

## My Approaches
### Attempt 1 — Sort Both, Two Pointer ✅ Final Accepted Solution
**Why I used it:**
Sorting both lists lets the smallest sufficient cookie always go to the least greedy unsatisfied child first.

```python
def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    i = j = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
        j += 1
    return i
```

**Complexity:**
- Time: O(n log n + m log m)
- Space: O(1) extra

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Sort both children (by greed) and cookies (by size). Walk through cookies in order; whenever a cookie is big enough for the current least-greedy unsatisfied child, assign it and move to the next child. This greedily reserves larger cookies for greedier children.

```python
def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    child = 0
    for cookie in s:
        if child < len(g) and cookie >= g[child]:
            child += 1
    return child
```

### Complexity
- Time: O(n log n + m log m)
- Space: O(1) extra

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Sort Both, Two Pointer) | O(n log n + m log m) | O(1) extra | ✅ |
| Standard Approach 1 | O(n log n + m log m) | O(1) extra | ✅ |


---

## Key Takeaway
Sorting both sides and matching the smallest sufficient cookie to the least greedy child first is the classic two-pointer greedy pattern.

---

## Reference
- LeetCode #455 — Assign Cookies
