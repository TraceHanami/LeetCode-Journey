# 058 — Length of Last Word

## Problem
Given a string of words separated by spaces, return the length of the last word.

**Difficulty:** Easy | **Topic:** Strings
**[View on LeetCode](https://leetcode.com/problems/length-of-last-word/)**

**Examples:**
```text
Input: s = "Hello World"
Output: 5
```

---

## My Approaches
### Attempt 1 — Strip Trailing Spaces, Scan Backward ✅ Final Accepted Solution
**Why I used it:**
Trim trailing whitespace, then count characters from the end until hitting a space.

```python
def lengthOfLastWord(self, s: str) -> int:
    length = 0
    s = s.rstrip()
    for ch in reversed(s):
        if ch == ' ':
            break
        length += 1
    return length
```

**Complexity:**
- Time: O(n)
- Space: O(1) extra

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Splitting on whitespace and taking the length of the last token is the most direct expression, letting Python's split() handle multiple/trailing spaces automatically.

```python
def lengthOfLastWord(self, s: str) -> int:
    return len(s.split()[-1])
```

### Complexity
- Time: O(n)
- Space: O(n)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Strip Trailing Spaces, Scan Backward) | O(n) | O(1) extra | ✅ |
| Standard Approach 1 | O(n) | O(n) | ✅ |


---

## Key Takeaway
Scanning backward avoids allocating a full list of words, but split()[-1] is simpler to read when the extra O(n) space isn't a concern.

---

## Reference
- LeetCode #58 — Length of Last Word
