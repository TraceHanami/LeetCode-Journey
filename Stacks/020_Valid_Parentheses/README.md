# 20 — Valid Parentheses

## Problem

Stack-based matching — push open brackets, pop and verify on close.

**Difficulty:** Easy | **Topic:** Stacks

**[View on LeetCode](https://leetcode.com/problems/valid-parentheses/)**

**Exampples:**
```
s = "()" -> true
s = "()[]{}" ->true
s = "(]" -> false
s = "([])" ->true
s = "([)]" -> fasle
```

---

## Approach 1 — Stack ✅

**Idea:** Push open brackets. On close bracket, check top of stack matches. Stack must be empty at end.

```python
class Solution1:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Stack | O(n) | O(n) | ✅ Yes |

---

## Reference

[LeetCode #20 — Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
