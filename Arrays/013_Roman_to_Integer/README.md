# 013 — Roman to Integer

## Problem
Convert a Roman numeral string to an integer.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/roman-to-integer/)**

**Examples:**
```text
Input: s = "III"
Output: 3

Input: s = "LVIII"
Output: 58
```

---

## My Approaches
### Attempt 1 — Compare Adjacent Symbol Values ✅ Final Accepted Solution
**Why I used it:**
A smaller value before a larger one means subtraction, otherwise addition — matches the Roman numeral subtraction rule directly.

```python
def romanToInt(self, s: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
    return total
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Map each symbol to its value and walk the string once. Whenever a symbol is smaller than the one that follows it, it must be subtracted (e.g. IV = 4); otherwise it's added.

```python
def romanToInt(self, s: str) -> int:
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i, ch in enumerate(s):
        if i + 1 < len(s) and values[ch] < values[s[i + 1]]:
            total -= values[ch]
        else:
            total += values[ch]
    return total
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Compare Adjacent Symbol Values) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
A single left-to-right pass works as long as you peek one symbol ahead to detect the subtractive pairs (IV, IX, XL, XC, CD, CM).

---

## Reference
- LeetCode #13 — Roman to Integer
