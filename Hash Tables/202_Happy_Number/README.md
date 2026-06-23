# 202 — Happy Number

## Problem

Repeatedly sum digit squares; detect cycle using a set or fast/slow pointers.

**Difficulty:** Easy | **Topic:** Hash Tables

**[View on LeetCode](https://leetcode.com/problems/happy-number/)**

**Examples**
```
n = 19 -> true
n = 2 -> false
```
---

## Approach 1 — Hash set cycle detection ✅

**Idea:** Store seen sums in a set. Return True if reach 1, False if sum repeats.

```python
class Solution1:
    def isHappy(self, n: int) -> bool:
        def digit_square_sum(num):
            return sum(int(d) ** 2 for d in str(num))

        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = digit_square_sum(n)
        return True
```

**Complexity:**
- Time: O(log n)
- Space: O(log n)

---

## Approach 2 — Floyd's cycle detection

**Idea:** Slow moves one step, fast moves two. Cycle detected when they meet; happy if fast reaches 1.

```python
class Solution2:
    def isHappy(self, n: int) -> bool:
        def digit_square_sum(num):
            return sum(int(d) ** 2 for d in str(num))

        slow, fast = n, digit_square_sum(n)
        while fast != 1 and slow != fast:
            slow = digit_square_sum(slow)
            fast = digit_square_sum(digit_square_sum(fast))
        return fast == 1
```

**Complexity:**
- Time: O(log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Hash set cycle detection | O(log n) | O(log n) | ✅ Yes |
| 2 — Floyd's cycle detection | O(log n) | O(1) | No |

---

## Reference

[LeetCode #202 — Happy Number](https://leetcode.com/problems/happy-number/)
