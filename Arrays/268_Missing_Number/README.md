# 268 — Missing Number

## Problem
Given an array containing n distinct numbers from 0 to n, find the one number missing from the range.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/missing-number/)**

**Examples:**
```text
Input: nums = [3,0,1]
Output: 2
```

---

## My Approaches
### Attempt 1 — XOR of Indices and Values ✅ Final Accepted Solution
**Why I used it:**
XORing every index and every value cancels out all present pairs, leaving only the missing number.

```python
def missingNumber(self, nums: List[int]) -> int:
    missing = len(nums)
    for i, n in enumerate(nums):
        missing ^= i ^ n
    return missing
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
XOR every index 0..n and every value in nums together. Since XOR is its own inverse, each number that appears in both the index range and the array cancels itself out, leaving only the number that never got paired.

```python
def missingNumber(self, nums: List[int]) -> int:
    missing = len(nums)
    for i, n in enumerate(nums):
        missing ^= i ^ n
    return missing
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (XOR of Indices and Values) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
XOR cancellation avoids any risk of integer overflow that a sum-based Gauss's formula approach could have in other languages.

---

## Reference
- LeetCode #268 — Missing Number
