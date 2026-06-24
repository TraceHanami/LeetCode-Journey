# 28 — Find Index of First Occurrence in String

## Problem

Find the first index where needle appears in haystack.

**Difficulty:** Easy | **Topic:** Strings

**[View on LeetCode](https://leetcode.com/problems/find-index-of-first-occurrence-in-string/)**

---

## Approach 1 — Sliding window ✅

**Idea:** Check each window of length m in haystack against needle.

```python
class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1
```

**Complexity:**
- Time: O(n*m)
- Space: O(1)

---

## Approach 2 — Built-in find

**Idea:** Use haystack.find(needle) or haystack.index(needle).

```python
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
```

**Complexity:**
- Time: O(n*m)
- Space: O(1)

---

## Approach 3 — KMP algorithm

**Idea:** Build failure function for needle, use it to skip redundant comparisons.

```python
class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:
        def build_lps(pattern):
            lps = [0] * len(pattern)
            length, i = 0, 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                elif length:
                    length = lps[length - 1]
                else:
                    i += 1
            return lps

        lps = build_lps(needle)
        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == len(needle):
                return i - j
            elif i < len(haystack) and haystack[i] != needle[j]:
                if j:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1
```

**Complexity:**
- Time: O(n+m)
- Space: O(m)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Sliding window | O(n*m) | O(1) | ✅ Yes |
| 2 — Built-in find | O(n*m) | O(1) | No |
| 3 — KMP algorithm | O(n+m) | O(m) | No |

---

## Reference

[LeetCode #28 — Find Index of First Occurrence in String](https://leetcode.com/problems/find-index-of-first-occurrence-in-string/)
