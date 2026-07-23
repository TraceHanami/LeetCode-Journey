# 202 — Happy Number

## Problem
A happy number eventually reaches 1 by repeatedly replacing it with the sum of the squares of its digits. Return true if n is happy.

**Difficulty:** Easy | **Topic:** Hash Tables
**[View on LeetCode](https://leetcode.com/problems/happy-number/)**

**Examples:**
```text
Input: n = 19
Output: true  (1^2+9^2=82, 8^2+2^2=68, ... -> 1)
```

---

## My Approaches
### Attempt 1 — Cycle Detection with a Seen Set ✅ Final Accepted Solution
**Why I used it:**
If a number repeats, the sequence is stuck in an infinite loop that will never reach 1 — track seen values to detect that.

```python
def isHappy(self, n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        total = 0
        while n > 0:
            d = n % 10
            total += d ** 2
            n //= 10
        n = total
    return n == 1
```

**Complexity:**
- Time: O(log n) per step, bounded overall
- Space: O(k) for the seen set

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Repeatedly compute the sum of squared digits. Numbers that aren't happy always fall into a cycle rather than growing forever, so tracking seen values (or using Floyd's cycle detection with a slow/fast pointer) reliably detects non-happy numbers.

```python
def isHappy(self, n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1
```

### Complexity
- Time: O(log n) per step
- Space: O(k)

---
### Standard Approach 2 — Alternative
### Idea
Floyd's cycle detection (tortoise and hare) avoids the O(k) set entirely: advance a slow pointer one step and a fast pointer two steps through the digit-square-sum sequence; if they ever meet on a value other than 1, it's a cycle (not happy).

```python
def isHappy(self, n: int) -> bool:
    def next_val(x):
        return sum(int(d) ** 2 for d in str(x))
    slow, fast = n, next_val(n)
    while fast != 1 and slow != fast:
        slow = next_val(slow)
        fast = next_val(next_val(fast))
    return fast == 1
```

### Complexity
- Time: O(log n) per step
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Cycle Detection with a Seen Set) | O(log n) per step, bounded overall | O(k) for the seen set | ✅ |
| Standard Approach 1 | O(log n) per step | O(k) | ✅ |
| Standard Approach 2 | O(log n) per step | O(1) | Optional |


---

## Key Takeaway
Non-happy numbers always enter a cycle rather than diverging, so cycle detection (via a seen set or Floyd's algorithm) reliably identifies them.

---

## Reference
- LeetCode #202 — Happy Number
