# 026 — Remove Duplicates from Sorted Array

## Problem
Remove duplicates in-place from a sorted array so each unique element appears once, and return the new length.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)**

**Examples:**
```text
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5
```

---

## My Approaches
### Attempt 1 — Build a Deduplicated List, Copy Back ✅ Final Accepted Solution
**Why I used it:**
Easiest to reason about — collect unique values first, then overwrite the original array.

```python
def removeDuplicates(self, nums: List[int]) -> int:
    unique = []
    for n in nums:
        if n not in unique:
            unique.append(n)
    for i in range(len(unique)):
        nums[i] = unique[i]
    return len(unique)
```

**Complexity:**
- Time: O(n^2)
- Space: O(n)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Since the array is already sorted, duplicates are always adjacent. Keep a slow pointer marking the end of the unique section and a fast pointer that scans ahead, only writing a value when it differs from the last kept one.

```python
def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Build a Deduplicated List, Copy Back) | O(n^2) | O(n) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
Sorted input means duplicates are neighbors — a two-pointer in-place pass beats checking membership in a growing list.

---

## Reference
- LeetCode #26 — Remove Duplicates from Sorted Array
