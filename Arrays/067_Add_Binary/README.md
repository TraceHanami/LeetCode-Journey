# 67 — Add Binary

## Problem

String simulation using carry logic — similar to how you'd add two numbers by hand.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/add-binary/)**

**Examples:**
```
a = "11", b = "1" -> "100"
a = "1010", b = "1011" -> "10101"
```

---

## Approach 1 — Simulation with carry ✅

**Idea:** Iterate from right to left, adding bits with a carry. Append remainder and reverse.

```python
class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return ''.join(reversed(result))

```

**Complexity:**
- Time: O(max(n,m))
- Space: O(max(n,m))

---

## Approach 2 — Python int conversion

**Idea:** Convert both binary strings to integers, add, convert back to binary.

```python
class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
```

**Complexity:**
- Time: O(n+m)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Simulation with carry | O(max(n,m)) | O(max(n,m)) | ✅ Yes |
| 2 — Python int conversion | O(n+m) | O(1) | No |

---

## Reference

[LeetCode #67 — Add Binary](https://leetcode.com/problems/add-binary/)
