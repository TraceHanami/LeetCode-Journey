# 1004 — Max Consecutive Ones III

## Problem
Given a binary array and an integer k, return the maximum number of consecutive 1's if you can flip at most k 0's to 1's.

**Difficulty:** Medium | **Topic:** Sliding Window
**[View on LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii/)**

**Examples:**
```text
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
```

---

## My Approaches
### Attempt 1 — Variable-Size Sliding Window Tracking Zero Count ✅ Final Accepted Solution
**Why I used it:**
Expand the window freely, but once the number of 0's inside exceeds k, shrink from the left until it's back within budget.

```python
def longestOnes(self, nums: List[int], k: int) -> int:
    left = zeros = best = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        best = max(right - left + 1, best)
    return best
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Same 'at most K' sliding window pattern as Fruit Into Baskets, but the constraint here is on the count of 0's in the window instead of distinct values. Expand right freely; shrink left whenever zero-count exceeds the flip budget k.

```python
def longestOnes(self, nums: List[int], k: int) -> int:
    left = zero_count = best = 0
    for right, val in enumerate(nums):
        if val == 0:
            zero_count += 1
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Variable-Size Sliding Window Tracking Zero Count) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
Flipping at most k zeros is equivalent to allowing at most k 'bad' elements in the window — the same expand-shrink sliding window template applies directly.

---

## Reference
- LeetCode #1004 — Max Consecutive Ones III
