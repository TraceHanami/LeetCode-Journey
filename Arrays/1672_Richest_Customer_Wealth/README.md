# 1672 — Richest Customer Wealth

## Problem
Given a grid where accounts[i][j] is the money customer i has in bank j, return the wealth of the richest customer.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/richest-customer-wealth/)**

**Examples:**
```text
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
```

---

## My Approaches
### Attempt 1 — Running List of Prefix Sums
**Why I used it:**
Accumulated sums per row into a flat list, then took the max — works but does more bookkeeping than necessary.

```python
def maximumWealth(self, accounts: List[List[int]]) -> int:
    sums = []
    for row in accounts:
        s = 0
        for v in row:
            s += v
            sums.append(s)
    return max(sums)
```

**Complexity:**
- Time: O(n * m)
- Space: O(n * m)

---
### Attempt 2 — Sum Each Row, Take the Max ✅ Final Accepted Solution
**Why I used it:**
Only the final row total matters, so no need to store every partial sum.

```python
def maximumWealth(self, accounts: List[List[int]]) -> int:
    return max(sum(row) for row in accounts)
```

**Complexity:**
- Time: O(n * m)
- Space: O(1) extra

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Sum each customer's row and keep the maximum — a direct generator expression over `sum()` and `max()` is both the clearest and most efficient way to express it.

```python
def maximumWealth(self, accounts: List[List[int]]) -> int:
    return max(sum(row) for row in accounts)
```

### Complexity
- Time: O(n * m)
- Space: O(1) extra

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Sum Each Row, Take the Max) | O(n * m) | O(1) extra | ✅ |
| Standard Approach 1 | O(n * m) | O(1) extra | ✅ |
| Running List of Prefix Sums | O(n * m) | O(n * m) | ❌ |


---

## Key Takeaway
You only need each row's final total, not every partial sum along the way.

---

## Reference
- LeetCode #1672 — Richest Customer Wealth
