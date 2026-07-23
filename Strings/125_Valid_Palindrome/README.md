# 125 — Valid Palindrome

## Problem
Given a string, return true if it's a palindrome after converting to lowercase and removing all non-alphanumeric characters.

**Difficulty:** Easy | **Topic:** Strings
**[View on LeetCode](https://leetcode.com/problems/valid-palindrome/)**

**Examples:**
```text
Input: s = "A man, a plan, a canal: Panama"
Output: true
```

---

## My Approaches
### Attempt 1 — Filter and Compare Reversed ✅ Final Accepted Solution
**Why I used it:**
Build a cleaned lowercase-alphanumeric version of the string, then compare it to its reverse.

```python
def isPalindrome(self, s: str) -> bool:
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Filtering into a clean string and reversing it is simple and O(n). A more space-efficient version uses two pointers converging from both ends, skipping non-alphanumeric characters in place without building a new string.

```python
def isPalindrome(self, s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
```

### Complexity
- Time: O(n)
- Space: O(1) extra

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Filter and Compare Reversed) | O(n) | O(n) | ✅ |
| Standard Approach 1 | O(n) | O(1) extra | ✅ |


---

## Key Takeaway
Building a cleaned copy is the readable approach; the two-pointer in-place scan gets the same O(n) time down to O(1) extra space.

---

## Reference
- LeetCode #125 — Valid Palindrome
