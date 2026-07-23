# 643 — Maximum Average Subarray I

## Problem
Given an array and an integer k, find the contiguous subarray of length k with the maximum average value.

**Difficulty:** Easy | **Topic:** Sliding Window
**[View on LeetCode](https://leetcode.com/problems/maximum-average-subarray-i/)**

**Examples:**
```text
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
```

---

## My Approaches
### Attempt 1 — Fixed-Size Sliding Window Sum ✅ Final Accepted Solution
**Why I used it:**
Maintain a running sum for the current window of size k, adding the new element and subtracting the one that leaves, instead of resumming from scratch each time.

```python
def findMaxAverage(self, nums: List[int], k: int) -> float:
    window_sum = sum(nums[:k])
    best = window_sum / k
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        best = max(best, window_sum / k)
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
Compute the sum of the first window of size k, then slide it one step at a time by adding the entering element and removing the leaving one — this avoids recomputing the full sum at every position.

```python
def findMaxAverage(self, nums: List[int], k: int) -> float:
    curr = sum(nums[:k])
    best = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        best = max(best, curr)
    return best / k
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Fixed-Size Sliding Window Sum) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
The 'add new, remove old' sliding window sum update is the canonical way to avoid an O(n*k) brute-force recomputation for fixed-size windows.

---

## Reference
- LeetCode #643 — Maximum Average Subarray I
