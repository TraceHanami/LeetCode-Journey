# 1768 — Merge Strings Alternately

## Problem
Given two strings word1 and word2, merge them by adding letters in alternating order, starting with word1. Append any leftover letters from the longer string.

**Difficulty:** Easy | **Topic:** Strings
**[View on LeetCode](https://leetcode.com/problems/merge-strings-alternately/)**

**Examples:**
```text
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
```

---

## My Approaches
### Attempt 1 — Two Pointer, Alternate Append ✅ Final Accepted Solution
**Why I used it:**
Walk both strings in lockstep, appending one character from each per step, then tack on whatever's left.

```python
def mergeAlternately(self, word1: str, word2: str) -> str:
    result = ""
    i = j = 0
    while i < len(word1) and j < len(word2):
        result += word1[i]
        result += word2[j]
        i += 1
        j += 1
    result += word1[i:]
    result += word2[j:]
    return result
```

**Complexity:**
- Time: O(n + m)
- Space: O(n + m)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Python's itertools.zip_longest pairs up characters from both strings, filling missing positions with an empty string once the shorter one runs out — a concise way to express the same alternating merge.

```python
def mergeAlternately(self, word1: str, word2: str) -> str:
    from itertools import zip_longest
    return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))
```

### Complexity
- Time: O(n + m)
- Space: O(n + m)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Two Pointer, Alternate Append) | O(n + m) | O(n + m) | ✅ |
| Standard Approach 1 | O(n + m) | O(n + m) | ✅ |


---

## Key Takeaway
zip_longest is a clean built-in way to alternate through two sequences of different lengths without manual index bookkeeping.

---

## Reference
- LeetCode #1768 — Merge Strings Alternately
