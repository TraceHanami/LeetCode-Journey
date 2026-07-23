# 1291 — Sequential Digits

## Problem
A number has sequential digits if each digit is one more than the previous digit. Return all numbers with sequential digits in the range [low, high], sorted in increasing order.

**Difficulty:** Medium | **Topic:** Math
**[View on LeetCode](https://leetcode.com/problems/sequential-digits/)**

**Examples:**
```text
Input: low = 100, high = 300
Output: [123,234]
```

---

## My Approaches
### Attempt 1 — Generate from a Fixed Digit Source String ✅ Final Accepted Solution
**Why I used it:**
Every sequential-digit number is a substring of "123456789" — generate all substrings of the right lengths and filter by range.

```python
def sequentialDigits(self, low: int, high: int) -> List[int]:
    sample = "123456789"
    result = []
    low_len = len(str(low))
    high_len = len(str(high))
    for length in range(low_len, high_len + 1):
        for start in range(10 - length):
            num = int(sample[start:start + length])
            if low <= num <= high:
                result.append(num)
    return result
```

**Complexity:**
- Time: O(1) — at most 36 candidates total
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Every sequential-digit number is exactly a contiguous substring of the digit string "123456789". For each possible length between the digit-lengths of low and high, slide a window across that source string, and keep any resulting number that falls within [low, high]. Since results only depend on length, they come out sorted automatically.

```python
def sequentialDigits(self, low: int, high: int) -> List[int]:
    digits = "123456789"
    result = []
    for length in range(len(str(low)), len(str(high)) + 1):
        for start in range(len(digits) - length + 1):
            num = int(digits[start:start + length])
            if low <= num <= high:
                result.append(num)
    return result
```

### Complexity
- Time: O(1)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Generate from a Fixed Digit Source String) | O(1) — at most 36 candidates total | O(1) | ✅ |
| Standard Approach 1 | O(1) | O(1) | ✅ |


---

## Key Takeaway
Recognizing that all valid answers come from substrings of a single fixed string ("123456789") turns a search problem into simple enumeration.

---

## Reference
- LeetCode #1291 — Sequential Digits
