# 067 — Add Binary

## Problem
Given two binary strings a and b, return their sum as a binary string.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/add-binary/)**

**Examples:**
```text
Input: a = "11", b = "1"
Output: "100"
```

---

## My Approaches
### Attempt 1 — Convert to Int, Add, Convert Back to Binary ✅ Final Accepted Solution
**Why I used it:**
Python's built-in int(..., 2) and bin() make this a one-liner.

```python
def addBinary(self, a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
For very large binary strings (bigger than native int handling in other languages) you'd add digit by digit from the right with a carry, exactly like grade-school addition — Python's arbitrary-precision ints make the built-in conversion just as effective here.

```python
def addBinary(self, a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i]); i -= 1
        if j >= 0:
            total += int(b[j]); j -= 1
        result.append(str(total % 2))
        carry = total // 2
    return "".join(reversed(result))
```

### Complexity
- Time: O(max(n, m))
- Space: O(max(n, m))

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Convert to Int, Add, Convert Back to Binary) | O(n) | O(n) | ✅ |
| Standard Approach 1 | O(max(n, m)) | O(max(n, m)) | ✅ |


---

## Key Takeaway
Python's arbitrary-precision integers make binary conversion trivial, but the manual carry-based addition is the language-agnostic technique worth knowing.

---

## Reference
- LeetCode #67 — Add Binary
