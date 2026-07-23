# 414 — Third Maximum Number

## Problem
Given an integer array, return the third distinct maximum number. If it doesn't exist, return the maximum.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/third-maximum-number/)**

**Examples:**
```text
Input: nums = [3,2,1]
Output: 1

Input: nums = [1,2]
Output: 2
```

---

## My Approaches
### Attempt 1 — Dedupe, Sort, Index ✅ Final Accepted Solution
**Why I used it:**
Sorting a deduplicated set makes picking the third-largest a simple index lookup.

```python
def thirdMax(self, nums: List[int]) -> int:
    unique = sorted(set(nums))
    if len(unique) >= 3:
        return unique[-3]
    return unique[-1]
```

**Complexity:**
- Time: O(n log n)
- Space: O(n)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Track the top three distinct values seen so far using three variables updated in a single pass — avoids the O(n log n) sort in exchange for more careful bookkeeping.

```python
def thirdMax(self, nums: List[int]) -> int:
    first = second = third = None
    for n in set(nums):
        if first is None or n > first:
            first, second, third = n, first, second
        elif second is None or n > second:
            second, third = n, second
        elif third is None or n > third:
            third = n
    return third if third is not None else first
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Dedupe, Sort, Index) | O(n log n) | O(n) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
Sorting a deduplicated set is the simplest correct approach; tracking the top three with running variables gets it down to linear time.

---

## Reference
- LeetCode #414 — Third Maximum Number
