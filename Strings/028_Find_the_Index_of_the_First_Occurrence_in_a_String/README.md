# 028 — Find the Index of the First Occurrence in a String

## Problem
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if it does not occur.

**Difficulty:** Easy | **Topic:** Strings
**[View on LeetCode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)**

**Examples:**
```text
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
```

---

## My Approaches
### Attempt 1 — Built-in str.find() ✅ Final Accepted Solution
**Why I used it:**
Python's find() implements substring search directly and efficiently.

```python
def strStr(self, haystack: str, needle: str) -> int:
    return haystack.find(needle)
```

**Complexity:**
- Time: O(n * m) worst case
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
For interview purposes the naive sliding-window comparison (check needle against every starting index) is the baseline; production string search uses KMP or Boyer-Moore for guaranteed O(n + m), but Python's built-in find() already uses a fast underlying implementation.

```python
def strStr(self, haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)
    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i
    return -1
```

### Complexity
- Time: O(n * m) worst case
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Built-in str.find()) | O(n * m) worst case | O(1) | ✅ |
| Standard Approach 1 | O(n * m) worst case | O(1) | ✅ |


---

## Key Takeaway
For real-world/interview follow-ups, KMP is the standard O(n + m) algorithm for substring search, avoiding the re-comparison work of the naive sliding window.

---

## Reference
- LeetCode #28 — Find the Index of the First Occurrence in a String
