# 3612 — Process String with Special Operations I

## Problem
Process a string left to right where '*' removes the last character, '#' duplicates the current result, '%' reverses the current result, and any other character is appended normally.

**Difficulty:** Medium | **Topic:** Strings
**[View on LeetCode](https://leetcode.com/problems/process-string-with-special-operations-i/)**

**Examples:**
```text
Input: s = "a#b%c"
Output: builds up via append/duplicate/reverse operations character by character
```

---

## My Approaches
### Attempt 1 — Direct String Simulation ✅ Final Accepted Solution
**Why I used it:**
Simulate each operation directly against a growing string result, following the rules exactly as specified.

```python
def processStr(self, s: str) -> str:
    r = ""
    for ch in s:
        if ch == '*':
            if r:
                r = r[:-1]
        elif ch == '#':
            r = r + r
        elif ch == '%':
            r = r[::-1]
        else:
            r += ch
    return r
```

**Complexity:**
- Time: O(n * L) where L grows with duplication
- Space: O(L)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Simulating directly against a plain string works and is easy to reason about, since each operation (delete-last, duplicate, reverse, append) maps to one line of string manipulation. For very large inputs where '#' causes exponential growth, a more careful approach tracks length/parity instead of materializing the full string (see Process String II).

```python
def processStr(self, s: str) -> str:
    result = ""
    for ch in s:
        if ch == '*':
            result = result[:-1] if result else result
        elif ch == '#':
            result += result
        elif ch == '%':
            result = result[::-1]
        else:
            result += ch
    return result
```

### Complexity
- Time: O(n * L)
- Space: O(L)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Direct String Simulation) | O(n * L) where L grows with duplication | O(L) | ✅ |
| Standard Approach 1 | O(n * L) | O(L) | ✅ |


---

## Key Takeaway
Simulating each special operation directly on a string is the clearest correct approach when the final string is small enough to materialize in full.

---

## Reference
- LeetCode #3612 — Process String with Special Operations I
