# 704 — Binary Search

## Problem
Given a sorted array of unique integers and a target, return its index, or -1 if not present.

**Difficulty:** Easy | **Topic:** Binary Search
**[View on LeetCode](https://leetcode.com/problems/binary-search/)**

**Examples:**
```text
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
```

---

## My Approaches
### Attempt 1 — Classic Binary Search ✅ Final Accepted Solution
**Why I used it:**
Textbook implementation — halve the search space every step.

```python
def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
```

**Complexity:**
- Time: O(log n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Repeatedly compare the target to the middle element and discard the half of the array that can't contain it. Using `left + (right - left) // 2` instead of `(left + right) // 2` avoids integer overflow in languages with fixed-width ints.

```python
def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Complexity
- Time: O(log n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Classic Binary Search) | O(log n) | O(1) | ✅ |
| Standard Approach 1 | O(log n) | O(1) | ✅ |


---

## Key Takeaway
This is the canonical binary search template — every other binary-search problem is a variation of this loop.

---

## Reference
- LeetCode #704 — Binary Search
