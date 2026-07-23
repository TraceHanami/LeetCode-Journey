# 066 — Plus One

## Problem
Given a large integer as an array of digits, increment the integer by one and return the resulting digit array.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/plus-one/)**

**Examples:**
```text
Input: digits = [1,2,3]
Output: [1,2,4]

Input: digits = [9,9]
Output: [1,0,0]
```

---

## My Approaches
### Attempt 1 — Right-to-Left Carry Propagation ✅ Final Accepted Solution
**Why I used it:**
Mirrors how you'd add 1 by hand — carry only propagates while digits are 9.

```python
def plusOne(self, digits: List[int]) -> List[int]:
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
```

**Complexity:**
- Time: O(n)
- Space: O(1) extra (O(n) for the new array on all-9s)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Walk from the last digit backward. If a digit is less than 9, incrementing it stops all carrying immediately. If it's a 9, it becomes 0 and the carry continues left; if the carry runs off the front, prepend a 1.

```python
def plusOne(self, digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
```

### Complexity
- Time: O(n)
- Space: O(1) extra

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Right-to-Left Carry Propagation) | O(n) | O(1) extra (O(n) for the new array on all-9s) | ✅ |
| Standard Approach 1 | O(n) | O(1) extra | ✅ |


---

## Key Takeaway
Carry propagation only ever needs to travel as far as the trailing run of 9s — most of the time it stops after one digit.

---

## Reference
- LeetCode #66 — Plus One
