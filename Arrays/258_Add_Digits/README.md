# 258 — Add Digits

## Problem
Given an integer, repeatedly add all its digits until the result has only one digit, and return it.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/add-digits/)**

**Examples:**
```text
Input: num = 38
Output: 2  (3+8=11, 1+1=2)
```

---

## My Approaches
### Attempt 1 — Digital Root Formula ✅ Final Accepted Solution
**Why I used it:**
Recognized this as the digital root, which has a closed-form formula based on mod 9.

```python
def addDigits(self, num: int) -> int:
    if num == 0:
        return 0
    return 9 if num % 9 == 0 else num % 9
```

**Complexity:**
- Time: O(1)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
This is the 'digital root' of a number, which has a well-known closed form: it equals 1 + (num - 1) % 9 for num > 0, or 0 for num = 0. No need to actually loop and re-sum digits.

```python
def addDigits(self, num: int) -> int:
    if num == 0:
        return 0
    return 1 + (num - 1) % 9
```

### Complexity
- Time: O(1)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Digital Root Formula) | O(1) | O(1) | ✅ |
| Standard Approach 1 | O(1) | O(1) | ✅ |


---

## Key Takeaway
Repeated digit-summing always converges to the 'digital root', which has a constant-time formula based on modulo 9.

---

## Reference
- LeetCode #258 — Add Digits
