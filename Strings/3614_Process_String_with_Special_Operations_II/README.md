# 3614 — Process String with Special Operations II

## Problem
Same operations as Process String I ('*' delete last, '#' duplicate, '%' reverse, else append), but instead of returning the whole result, return only the character at index k — without materializing a potentially astronomically large string.

**Difficulty:** Hard | **Topic:** Strings
**[View on LeetCode](https://leetcode.com/problems/process-string-with-special-operations-ii/)**

**Examples:**
```text
Input: s = "a#b%c", k = 2
Output: the character that would land at index k after applying every operation
```

---

## My Approaches
### Attempt 1 — Track Length, Then Replay Backward to Locate Index k ✅ Final Accepted Solution
**Why I used it:**
Since '#' can double the string length repeatedly (making it too large to build), first track the length after each operation, then walk operations backward mapping index k through each transformation to find its origin.

```python
def processStr(self, s: str, k: int) -> str:
    n = []
    c = 0
    for ch in s:
        if ch == "*":
            if c > 0:
                c -= 1
        elif ch == "#":
            c *= 2
        elif ch not in "*#%":
            c += 1
        n.append(c)
    if k >= c:
        return "."
    for i in range(len(s) - 1, -1, -1):
        ch = s[i]
        if ch == "#":
            half = n[i] // 2
            k %= half
        elif ch == "%":
            k = n[i] - 1 - k
        elif ch not in "#%*":
            if k == n[i] - 1:
                return ch
    return "."
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Never build the actual string — it can grow exponentially via '#'. Instead, track the length of the result after every operation in a first forward pass. Then walk the operations in reverse, mapping the target index k backward through each transformation (undoing a duplicate by taking k modulo half-length, undoing a reverse by flipping the index, and undoing a plain append by checking if k points at that exact position) until the origin character is found.

```python
def processStr(self, s: str, k: int) -> str:
    lengths = []
    length = 0
    for ch in s:
        if ch == "*":
            length = max(0, length - 1)
        elif ch == "#":
            length *= 2
        else:
            length += 1
        lengths.append(length)
    if k >= length:
        return "."
    for i in range(len(s) - 1, -1, -1):
        ch = s[i]
        if ch == "#":
            k %= lengths[i] // 2
        elif ch == "%":
            k = lengths[i] - 1 - k
        elif ch != "*":
            if k == lengths[i] - 1:
                return ch
    return "."
```

### Complexity
- Time: O(n)
- Space: O(n)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Track Length, Then Replay Backward to Locate Index k) | O(n) | O(n) | ✅ |
| Standard Approach 1 | O(n) | O(n) | ✅ |


---

## Key Takeaway
When an operation can cause exponential growth, never materialize the full result — track lengths forward and reverse-map the target index backward through each operation instead.

---

## Reference
- LeetCode #3614 — Process String with Special Operations II
