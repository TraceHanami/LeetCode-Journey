# 075 — Sort Colors

## Problem
Given an array with n objects colored red, white, or blue (represented as 0, 1, 2), sort them in-place so objects of the same color are adjacent, in the order red, white, blue.

**Difficulty:** Medium | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/sort-colors/)**

**Examples:**
```text
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

---

## My Approaches
### Attempt 1 — Built-in Sort ✅ Final Accepted Solution
**Why I used it:**
Only three distinct values, so a general sort trivially produces the right order.

```python
def sortColors(self, nums: List[int]) -> None:
    nums.sort()
```

**Complexity:**
- Time: O(n log n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
The Dutch National Flag algorithm uses three pointers — low, mid, high — to partition the array into 0s, 1s, and 2s in a single pass, swapping elements into place as mid scans through.

```python
def sortColors(self, nums: List[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1; mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Built-in Sort) | O(n log n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
Because there are only 3 distinct values, a full comparison sort is overkill — the Dutch National Flag one-pass partition is the intended optimal solution.

---

## Reference
- LeetCode #75 — Sort Colors
