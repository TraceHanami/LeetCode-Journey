# 2108 — Find First Palindromic String in the Array

## Problem
Given an array of strings, return the first string that is a palindrome. Return an empty string if none exists.

**Difficulty:** Easy | **Topic:** Strings
**[View on LeetCode](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/)**

**Examples:**
```text
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
```

---

## My Approaches
### Attempt 1 — Linear Scan, Check Reversal ✅ Final Accepted Solution
**Why I used it:**
Walk the list in order and return the first word that equals its own reverse.

```python
def firstPalindrome(self, words: List[str]) -> str:
    for w in words:
        if w == w[::-1]:
            return w
    return ""
```

**Complexity:**
- Time: O(n * k)
- Space: O(k) per check

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Check words in order and return as soon as a palindrome is found — there's no way to avoid checking each word up to its own length in the worst case, so this is already optimal.

```python
def firstPalindrome(self, words: List[str]) -> str:
    for word in words:
        if word == word[::-1]:
            return word
    return ""
```

### Complexity
- Time: O(n * k)
- Space: O(k) per check

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Linear Scan, Check Reversal) | O(n * k) | O(k) per check | ✅ |
| Standard Approach 1 | O(n * k) | O(k) per check | ✅ |


---

## Key Takeaway
A simple ordered linear scan with early return is already optimal here — there's no shortcut around checking each candidate.

---

## Reference
- LeetCode #2108 — Find First Palindromic String in the Array
