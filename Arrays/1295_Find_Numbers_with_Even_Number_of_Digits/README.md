# 1295 — Find Numbers with Even Number of Digits

## Problem
Given an array of integers, return how many of them have an even number of digits.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/)**

**Examples:**
```text
Input: nums = [12,345,2,6,7896]
Output: 2
```

---

## My Approaches
### Attempt 1 — len(str(n))
**Why I used it:**
Converting to a string makes counting digits trivial.

```python
def findNumbers(self, nums: List[int]) -> int:
    count = 0
    for n in nums:
        if len(str(n)) % 2 == 0:
            count += 1
    return count
```

**Complexity:**
- Time: O(n * d)
- Space: O(1)

---
### Attempt 2 — Count Digits by Division ✅ Final Accepted Solution
**Why I used it:**
Avoids string conversion — divide by 10 repeatedly to count digits directly.

```python
def findNumbers(self, nums: List[int]) -> int:
    count = 0
    for n in nums:
        digits = 0
        while n > 0:
            n //= 10
            digits += 1
        if digits % 2 == 0:
            count += 1
    return count
```

**Complexity:**
- Time: O(n * d)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Digit counting via string conversion is clean and fast enough given LeetCode's constraints (values fit comfortably under 10^5), so `len(str(n))` is the pragmatic optimal choice in Python.

```python
def findNumbers(self, nums: List[int]) -> int:
    return sum(1 for n in nums if len(str(n)) % 2 == 0)
```

### Complexity
- Time: O(n * d)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Count Digits by Division) | O(n * d) | O(1) | ✅ |
| Standard Approach 1 | O(n * d) | O(1) | ✅ |
| len(str(n)) | O(n * d) | O(1) | ❌ |


---

## Key Takeaway
Both string-length and manual digit-division approaches are O(d) per number — pick whichever reads more clearly for the language you're in.

---

## Reference
- LeetCode #1295 — Find Numbers with Even Number of Digits
