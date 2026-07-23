# 2529 — Maximum Count of Positive Integer and Negative Integer

## Problem
Given a sorted array of integers, return the larger of the count of positive numbers and the count of negative numbers.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/)**

**Examples:**
```text
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
```

---

## My Approaches
### Attempt 1 — Linear Count ✅ Final Accepted Solution
**Why I used it:**
Scan once, tallying positives and negatives separately, then compare.

```python
def maximumCount(self, nums: List[int]) -> int:
    pos, neg = 0, 0
    for n in nums:
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1
    return max(pos, neg)
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Since the array is sorted, binary search (bisect) can locate the boundaries between negatives, zeros, and positives in O(log n), but a simple linear scan is just as fine given the constraints and much simpler to write.

```python
def maximumCount(self, nums: List[int]) -> int:
    pos = sum(1 for n in nums if n > 0)
    neg = sum(1 for n in nums if n < 0)
    return max(pos, neg)
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
Sortedness would allow an O(log n) binary-search solution via bisect, but for this problem's size a plain linear scan is simpler and fast enough.

---

## Reference
- LeetCode #2529 — Maximum Count of Positive Integer and Negative Integer
