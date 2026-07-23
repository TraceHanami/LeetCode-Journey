# 009 — Palindrome Number

## Problem
Given an integer x, return true if x is a palindrome, and false otherwise, without converting it to a string (bonus challenge).

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/palindrome-number/)**

**Examples:**
```text
Input: x = 121
Output: true

Input: x = -121
Output: false
```

---

## My Approaches
### Attempt 1 — Convert to String
**Why I used it:**
Simplest check — reverse the string form and compare.

```python
def isPalindrome(self, x: int) -> bool:
    s = str(x)
    return s == s[::-1]
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---
### Attempt 2 — Reverse Half the Number ✅ Final Accepted Solution
**Why I used it:**
Avoids string conversion and stops halfway once the reversed part meets or passes the remaining part.

```python
def isPalindrome(self, x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return x == rev or x == rev // 10
```

**Complexity:**
- Time: O(log10 n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Negative numbers and numbers ending in 0 (except 0 itself) can never be palindromes. Reverse only the second half of the digits and compare it against the first half — this avoids ever building a number larger than the input and sidesteps overflow concerns entirely.

```python
def isPalindrome(self, x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return x == rev or x == rev // 10
```

### Complexity
- Time: O(log10 n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Reverse Half the Number) | O(log10 n) | O(1) | ✅ |
| Standard Approach 1 | O(log10 n) | O(1) | ✅ |
| Convert to String | O(n) | O(n) | ❌ |


---

## Key Takeaway
Reversing only half the digits avoids doing extra work and never risks building a number bigger than necessary.

---

## Reference
- LeetCode #9 — Palindrome Number
