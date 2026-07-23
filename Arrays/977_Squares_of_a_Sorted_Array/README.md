# 977 — Squares of a Sorted Array

## Problem
Given a sorted array (possibly with negatives), return an array of the squares of each number, sorted in non-decreasing order.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array/)**

**Examples:**
```text
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
```

---

## My Approaches
### Attempt 1 — Square Then Sort ✅ Final Accepted Solution
**Why I used it:**
Simplest correct approach — square every value and let sort() handle ordering.

```python
def sortedSquares(self, nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return sorted(nums)
```

**Complexity:**
- Time: O(n log n)
- Space: O(n)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
The largest squares always come from the two ends of the sorted input (most negative or most positive). Use two pointers starting at each end and fill the result array from the back, always placing the larger square first.

```python
def sortedSquares(self, nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    for i in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
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
| My Final Solution (Square Then Sort) | O(n log n) | O(n) | ✅ |
| Standard Approach 1 | O(n) | O(n) | ✅ |


---

## Key Takeaway
Because the input is already sorted, the largest squared values always come from one of the two ends — a two-pointer merge-from-the-back beats sorting.

---

## Reference
- LeetCode #977 — Squares of a Sorted Array
