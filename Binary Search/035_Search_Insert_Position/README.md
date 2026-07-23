# 035 — Search Insert Position

## Problem
Given a sorted array of distinct integers and a target, return the index if found, or the index where it would be inserted in order.

**Difficulty:** Easy | **Topic:** Binary Search
**[View on LeetCode](https://leetcode.com/problems/search-insert-position/)**

**Examples:**
```text
Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1
```

---

## My Approaches
### Attempt 1 — Binary Search ✅ Final Accepted Solution
**Why I used it:**
Sorted array means the insertion point can be found in O(log n) instead of scanning linearly.

```python
def searchInsert(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
```

**Complexity:**
- Time: O(log n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Classic binary search. When the target isn't found, `left` naturally ends up exactly at the index where the target should be inserted to keep the array sorted.

```python
def searchInsert(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
```

### Complexity
- Time: O(log n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Binary Search) | O(log n) | O(1) | ✅ |
| Standard Approach 1 | O(log n) | O(1) | ✅ |


---

## Key Takeaway
When binary search 'fails' to find the target, the left pointer lands exactly on the correct insertion index — no extra logic needed.

---

## Reference
- LeetCode #35 — Search Insert Position
