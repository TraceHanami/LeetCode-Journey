# 2798 — Number of Employees Who Met the Target

## Problem
Given the hours worked by each employee and a target number of hours, count how many employees worked at least the target.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/number-of-employees-who-met-the-target/)**

**Examples:**
```text
Input: hours = [0,1,2,3,4], target = 2
Output: 3
```

---

## My Approaches
### Attempt 1 — Linear Count ✅ Final Accepted Solution
**Why I used it:**
Straightforward single pass comparing each employee's hours to the target.

```python
def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
    count = 0
    for h in hours:
        if h >= target:
            count += 1
    return count
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
A single pass counting how many values meet the threshold — nothing more sophisticated is needed for this constraint size.

```python
def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
    return sum(1 for h in hours if h >= target)
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Linear Count) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
A plain linear scan is already optimal here — there's no ordering or structure in the input to exploit.

---

## Reference
- LeetCode #2798 — Number of Employees Who Met the Target
