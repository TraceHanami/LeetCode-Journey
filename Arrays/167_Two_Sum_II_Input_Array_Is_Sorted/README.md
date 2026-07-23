# 167 — Two Sum II - Input Array Is Sorted

## Problem
Given a 1-indexed sorted array, find two numbers that add up to target and return their indices.

**Difficulty:** Medium | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)**

**Examples:**
```text
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
```

---

## My Approaches
### Attempt 1 — Two Pointer (Optimal) ✅ Final Accepted Solution
**Why I used it:**
Since the array is sorted, moving pointers inward based on whether the sum is too big or small avoids any extra space.

```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    i, j = 0, len(numbers) - 1
    while i < j:
        s = numbers[i] + numbers[j]
        if s == target:
            return [i + 1, j + 1]
        elif s > target:
            j -= 1
        else:
            i += 1
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Because the array is sorted, a two-pointer sweep from both ends works: if the current sum is too large, the right pointer must move left (numbers only get smaller); if too small, the left pointer moves right.

```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        if total > target:
            right -= 1
        else:
            left += 1
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Two Pointer (Optimal)) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
Sortedness turns this into a classic O(n) two-pointer problem, avoiding the O(n) space a hash map would use for the unsorted version.

---

## Reference
- LeetCode #167 — Two Sum II - Input Array Is Sorted
