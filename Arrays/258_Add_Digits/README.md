# 258 — Add Digits

## Problem

Digital root formula: result is 0 if n=0, 9 if n%9==0, else n%9.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/add-digits/)**

**Examples:**
```
num = 38 -> 2
num = 0 -> 0
```

---

## Approach 1 — Digital root formula ✅

**Idea:** return 0 if n==0 else 9 if n%9==0 else n%9.

```python
class Solution1:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 9 if num % 9 == 0 else num % 9
```

**Complexity:**
- Time: O(1)
- Space: O(1)

---

## Approach 2 — Simulation

**Idea:** Repeatedly sum digits until single digit.

```python
class Solution2:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum(int(d) for d in str(num))
        return num
```

**Complexity:**
- Time: O(log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Digital root formula | O(1) | O(1) | ✅ Yes |
| 2 — Simulation | O(log n) | O(1) | No |

---

## Reference

[LeetCode #258 — Add Digits](https://leetcode.com/problems/add-digits/)
