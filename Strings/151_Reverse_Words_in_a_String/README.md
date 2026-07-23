# 151 — Reverse Words in a String

## Problem
Given an input string s, reverse the order of the words (words separated by whitespace, ignoring leading/trailing/multiple spaces).

**Difficulty:** Medium | **Topic:** Strings
**[View on LeetCode](https://leetcode.com/problems/reverse-words-in-a-string/)**

**Examples:**
```text
Input: s = "the sky is blue"
Output: "blue is sky the"
```

---

## My Approaches
### Attempt 1 — split() + reversed join ✅ Final Accepted Solution
**Why I used it:**
Python's split() already collapses multiple spaces and strips leading/trailing whitespace, so reversing the resulting list is enough.

```python
def reverseWords(self, s: str) -> str:
    return " ".join(s.split()[::-1])
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Split on whitespace (which naturally handles multiple spaces and trims the ends), reverse the list of words, and rejoin with single spaces.

```python
def reverseWords(self, s: str) -> str:
    words = s.split()
    return " ".join(reversed(words))
```

### Complexity
- Time: O(n)
- Space: O(n)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (split() + reversed join) | O(n) | O(n) | ✅ |
| Standard Approach 1 | O(n) | O(n) | ✅ |


---

## Key Takeaway
split() handles all the whitespace edge cases (leading, trailing, multiple spaces) automatically, making the reversal itself trivial.

---

## Reference
- LeetCode #151 — Reverse Words in a String
