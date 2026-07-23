# 020 — Valid Parentheses

## Problem
Given a string of brackets '()[]{}', determine if the input string is valid (every open bracket is closed by the same type in the correct order).

**Difficulty:** Easy | **Topic:** Stacks
**[View on LeetCode](https://leetcode.com/problems/valid-parentheses/)**

**Examples:**
```text
Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
```

---

## My Approaches
### Attempt 1 — Stack of Expected Closers ✅ Final Accepted Solution
**Why I used it:**
Push the expected closing bracket whenever an opener is seen; any mismatch or leftover bracket at the end means invalid.

```python
def isValid(self, s: str) -> bool:
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    for ch in s:
        if ch in pairs:
            stack.append(pairs[ch])
        else:
            if not stack or stack.pop() != ch:
                return False
    return not stack
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
A stack naturally models the nesting structure of brackets. Push the matching closer for every opening bracket seen; when a closing bracket appears, it must equal the top of the stack, otherwise the string is invalid. At the end, the stack must be empty.

```python
def isValid(self, s: str) -> bool:
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    for ch in s:
        if ch in pairs:
            stack.append(pairs[ch])
        elif not stack or stack.pop() != ch:
            return False
    return not stack
```

### Complexity
- Time: O(n)
- Space: O(n)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Stack of Expected Closers) | O(n) | O(n) | ✅ |
| Standard Approach 1 | O(n) | O(n) | ✅ |


---

## Key Takeaway
Whenever a problem involves nested/matched structure, a stack is almost always the right data structure — pushing the *expected closer* rather than the opener simplifies the matching check.

---

## Reference
- LeetCode #20 — Valid Parentheses
