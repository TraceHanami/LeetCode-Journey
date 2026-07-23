# 345 — Reverse Vowels of a String

## Problem
Given a string, reverse only the vowels in it and return the result.

**Difficulty:** Easy | **Topic:** Strings
**[View on LeetCode](https://leetcode.com/problems/reverse-vowels-of-a-string/)**

**Examples:**
```text
Input: s = "hello"
Output: "holle"
```

---

## My Approaches
### Attempt 1 — Two Pointer, Skip Consonants ✅ Final Accepted Solution
**Why I used it:**
Only vowels need to be swapped, so advance each pointer past non-vowels before swapping the vowels found.

```python
def reverseVowels(self, s: str) -> str:
    s = list(s)
    i, j = 0, len(s) - 1
    vowels = "aeiouAEIOU"
    while i < j:
        if s[i] in vowels and s[j] in vowels:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        elif s[i] not in vowels:
            i += 1
        else:
            j -= 1
    return "".join(s)
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Two pointers from both ends, each skipping forward/backward over consonants, and swapping whenever both land on a vowel — a variant of the standard two-pointer reversal restricted to a subset of characters.

```python
def reverseVowels(self, s: str) -> str:
    vowels = set("aeiouAEIOU")
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        if chars[left] not in vowels:
            left += 1
        elif chars[right] not in vowels:
            right -= 1
        else:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    return "".join(chars)
```

### Complexity
- Time: O(n)
- Space: O(n)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Two Pointer, Skip Consonants) | O(n) | O(n) | ✅ |
| Standard Approach 1 | O(n) | O(n) | ✅ |


---

## Key Takeaway
The classic two-pointer swap pattern still applies when only a subset of positions (vowels) are eligible to be swapped — just skip ineligible positions before swapping.

---

## Reference
- LeetCode #345 — Reverse Vowels of a String
