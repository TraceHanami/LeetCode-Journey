# 66 — Plus One

## Problem

Increment the last digit; propagate carry if digit becomes 10.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/plus-one/)**

**Examples:**
```
digits = [1,2,3] -> [1,2,4]
digits= [4,3,2,1] -> [4,3,2,2]
digits = [9] -> [1,0]
```
---

## Approach 1 — Reverse carry propagation ✅

**Idea:** Traverse from end; increment digit, return if no carry. If all 9s, prepend 1.

```python
class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Convert to int

**Idea:** Join digits to int, add 1, convert back to list.

```python
class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, str(int(''.join(map(str, digits))) + 1)))
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Reverse carry propagation | O(n) | O(1) | ✅ Yes |
| 2 — Convert to int | O(n) | O(n) | No |

---

## Reference

[LeetCode #66 — Plus One](https://leetcode.com/problems/plus-one/)
