# 242 — Valid Anagram

## Problem
Given two strings s and t, return true if t is an anagram of s.

**Difficulty:** Easy | **Topic:** Hash Tables
**[View on LeetCode](https://leetcode.com/problems/valid-anagram/)**

**Examples:**
```text
Input: s = "anagram", t = "nagaram"
Output: true
```

---

## My Approaches
### Attempt 1 — Sort and Compare ✅ Final Accepted Solution
**Why I used it:**
Two strings are anagrams exactly when their sorted characters are identical.

```python
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```

**Complexity:**
- Time: O(n log n)
- Space: O(n)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Sorting both strings and comparing is simple and correct, but a character-frequency count avoids the log factor: build a count of letters in s, subtract counts for letters in t, and check everything cancels to zero.

```python
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    from collections import Counter
    return Counter(s) == Counter(t)
```

### Complexity
- Time: O(n)
- Space: O(1) (bounded alphabet)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Sort and Compare) | O(n log n) | O(n) | ✅ |
| Standard Approach 1 | O(n) | O(1) (bounded alphabet) | ✅ |


---

## Key Takeaway
Sorting is a simple O(n log n) way to check anagrams, but counting character frequencies gets it down to O(n).

---

## Reference
- LeetCode #242 — Valid Anagram
