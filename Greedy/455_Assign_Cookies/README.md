# 455 — Assign Cookies

## Problem

Greedily assign the smallest sufficient cookie to each child.

**Difficulty:** Easy | **Topic:** Greedy

**[View on LeetCode](https://leetcode.com/problems/assign-cookies/)**

**Examples:**
```
g = [1,2,3], s = [1,1] -> 1
g = [1,2], s = [1,2,3] -> 2
```

---

## Approach 1 — Greedy two pointers ✅

**Idea:** Sort both arrays. Use two pointers — assign cookie to child if size >= greed. Move both pointers; otherwise only cookie pointer.

```python
class Solution1:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = cookie = 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        return child
```

**Complexity:**
- Time: O(n log n + m log m)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Greedy two pointers | O(n log n + m log m) | O(1) | ✅ Yes |

---

## Reference

[LeetCode #455 — Assign Cookies](https://leetcode.com/problems/assign-cookies/)
