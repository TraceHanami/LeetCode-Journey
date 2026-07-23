# 1967 — Number of Strings That Appear as Substrings in Word

## Problem
Given an array of strings patterns and a string word, return the number of strings in patterns that are a substring of word.

**Difficulty:** Easy | **Topic:** Strings
**[View on LeetCode](https://leetcode.com/problems/number-of-strings-that-are-substrings-of-word/)**

**Examples:**
```text
Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
```

---

## My Approaches
### Attempt 1 — Manual Substring Scan ✅ Final Accepted Solution
**Why I used it:**
For each pattern, manually slide a window across word checking for an exact match, rather than relying on the 'in' operator.

```python
def numOfStrings(self, patterns: List[str], word: str) -> int:
    count = 0
    n = len(word)
    for p in patterns:
        m = len(p)
        if m > n:
            continue
        for i in range(n - m + 1):
            if word[i:i + m] == p:
                count += 1
                break
    return count
```

**Complexity:**
- Time: O(k * n * m)
- Space: O(1) extra

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Python's `in` operator already performs efficient substring search, so checking each pattern against word directly is both simpler and at least as fast as a hand-rolled sliding window.

```python
def numOfStrings(self, patterns: List[str], word: str) -> int:
    return sum(1 for p in patterns if p in word)
```

### Complexity
- Time: O(k * n) average
- Space: O(1) extra

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Manual Substring Scan) | O(k * n * m) | O(1) extra | ✅ |
| Standard Approach 1 | O(k * n) average | O(1) extra | ✅ |


---

## Key Takeaway
Prefer built-in substring search (`in`) over hand-rolled sliding windows unless the problem specifically calls for implementing the search algorithm yourself.

---

## Reference
- LeetCode #1967 — Number of Strings That Appear as Substrings in Word
