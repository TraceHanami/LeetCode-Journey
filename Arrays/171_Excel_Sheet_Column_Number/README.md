# 171 — Excel Sheet Column Number

## Problem

Given a spreadsheet column title as it appears in Excel (e.g. "A", "Z", "AA", "AB"), return its corresponding column number.

**Difficulty:** Easy | **Topic:** Math

**[View on LeetCode](https://leetcode.com/problems/excel-sheet-column-number/)**

**Examples:**

```text
Input: columnTitle = "A"
Output: 1

Input: columnTitle = "AB"
Output: 28

Input: columnTitle = "ZY"
Output: 701
```

---

## My Approach ✅

### Why I Used This Method

This is base-26 conversion where the digits are letters 'A'-'Z' instead of 0-9. Treating it like reading a number left to right — multiply the running total by the base and add the next digit's value — falls straight out of that observation.

```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        r=0
        for i in columnTitle:
            r=r*26+(ord(i)-64)
        return r
```

### Complexity

* Time: O(n) where n = length of columnTitle
* Space: O(1)

---

## Alternative Approaches

### Approach 2 — `reduce` One-Liner

#### Idea

Express the same left-to-right accumulation using `functools.reduce` instead of an explicit loop.

```python
from functools import reduce

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return reduce(lambda acc, ch: acc * 26 + (ord(ch) - 64), columnTitle, 0)
```

#### Complexity

* Time: O(n)
* Space: O(1)

---

## Optimal Approach 🚀

### Idea

The submitted left-to-right base-26 accumulation is already the optimal approach for this problem — a single linear pass with constant extra space, with no faster asymptotic solution possible since every character must be read at least once.

```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for ch in columnTitle:
            result = result * 26 + (ord(ch) - ord('A') + 1)
        return result
```

### Complexity

* Time: O(n)
* Space: O(1)

---

## Comparison

| Approach       | Time | Space | Recommended |
| -------------- | ---- | ----- | ----------- |
| My Approach    | O(n) | O(1)  | ✅           |
| `reduce` Style | O(n) | O(1)  | Optional    |
| Optimal        | O(n) | O(1)  | 🚀          |

---

## Key Takeaway

Excel column titles are just base-26 numbers with digits 'A'-'Z' standing in for 1-26 (no zero digit), so the standard "multiply-then-add" base-conversion pattern applies directly.

---

## Reference

* LeetCode #171 — Excel Sheet Column Number
