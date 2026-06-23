# 9 — Palindrome Number

## Problem

Reverse half the number and compare to the other half — no string conversion.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/palindrome-number/)**

**Examples:**
```
x=121 -> true
x=-121 ->false
x=789 ->false
```

---

## Approach 1 — Reverse half ✅

**Idea:** Reverse digits of second half. Compare with first half. Handle negatives and trailing zeros.

```python
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return x == reversed_half or x == reversed_half // 10
```

**Complexity:**
- Time: O(log n)
- Space: O(1)

---

## Approach 2 — String conversion

**Idea:** str(x) == str(x)[::-1]. Simple but uses extra space.

```python
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
```

**Complexity:**
- Time: O(log n)
- Space: O(log n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Reverse half | O(log n) | O(1) | ✅ Yes |
| 2 — String conversion | O(log n) | O(log n) | No |

---

## Reference

[LeetCode #9 — Palindrome Number](https://leetcode.com/problems/palindrome-number/)
