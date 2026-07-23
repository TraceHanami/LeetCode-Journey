# 1480 — Running Sum of 1d Array

## Problem
Given an array nums, return the running sum where runningSum[i] = sum(nums[0..i]).

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/)**

**Examples:**
```text
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
```

---

## My Approaches
### Attempt 1 — Accumulate in a Running Total ✅ Final Accepted Solution
**Why I used it:**
Keep a running total and append it as you scan through the array once.

```python
def runningSum(self, nums: List[int]) -> List[int]:
    result = []
    total = 0
    for n in nums:
        total += n
        result.append(total)
    return result
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
A prefix sum is exactly a running total — accumulate as you go, in one linear pass.

```python
def runningSum(self, nums: List[int]) -> List[int]:
    total = 0
    result = []
    for n in nums:
        total += n
        result.append(total)
    return result
```

### Complexity
- Time: O(n)
- Space: O(n)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Accumulate in a Running Total) | O(n) | O(n) | ✅ |
| Standard Approach 1 | O(n) | O(n) | ✅ |


---

## Key Takeaway
This is the textbook definition of a prefix sum — a single accumulating pass.

---

## Reference
- LeetCode #1480 — Running Sum of 1d Array
