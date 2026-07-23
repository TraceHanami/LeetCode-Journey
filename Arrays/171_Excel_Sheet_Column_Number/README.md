# 171 — Excel Sheet Column Number

## Problem
Given a column title as it appears in an Excel sheet (e.g. 'A', 'AB', 'ZY'), return its corresponding column number.

**Difficulty:** Easy | **Topic:** Arrays
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

## My Approaches
_No personal attempt logged for this problem yet — see the Standard Approach below._

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
This is base-26 conversion, except the digits run 1–26 instead of 0–25. Walk left to right, multiplying the running total by 26 and adding the value of each letter (A=1 ... Z=26) — exactly like converting a base-26 number to decimal.

```python
def titleToNumber(self, columnTitle: str) -> int:
    result = 0
    for ch in columnTitle:
        result = result * 26 + (ord(ch) - ord('A') + 1)
    return result
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
No personal attempt logged for this one yet — it's effectively base-26 conversion with a 1-indexed digit range instead of the usual 0-indexed one.

---

## Reference
- LeetCode #171 — Excel Sheet Column Number
