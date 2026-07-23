# 2461 — Maximum Sum of Distinct Subarrays With Length K

## Problem
Given an array and an integer k, find the maximum sum of any subarray of length k whose elements are all distinct.

**Difficulty:** Medium | **Topic:** Sliding Window
**[View on LeetCode](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/)**

**Examples:**
```text
Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15
```

---

## My Approaches
### Attempt 1 — Fixed-Size Window with Sum + Frequency Map ✅ Final Accepted Solution
**Why I used it:**
Track both a running sum and a frequency count for the window of size k, only counting it as a candidate answer when the frequency map shows exactly k distinct values.

```python
def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    freq = {}
    curr = 0
    for i in range(k):
        freq[nums[i]] = freq.get(nums[i], 0) + 1
        curr += nums[i]
    best = curr if len(freq) == k else 0
    for i in range(k, len(nums)):
        left, right = nums[i - k], nums[i]
        curr += right - left
        freq[left] -= 1
        if freq[left] == 0:
            del freq[left]
        freq[right] = freq.get(right, 0) + 1
        if len(freq) == k:
            best = max(best, curr)
    return best
```

**Complexity:**
- Time: O(n)
- Space: O(k)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Slide a fixed-size window of length k, maintaining both a running sum (add entering element, subtract leaving element) and a frequency map. The window's elements are all distinct exactly when the frequency map has k unique keys — only then is the window's sum a valid candidate for the answer.

```python
def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    from collections import Counter
    freq = Counter(nums[:k])
    curr = sum(nums[:k])
    best = curr if len(freq) == k else 0
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        freq[nums[i]] += 1
        freq[nums[i - k]] -= 1
        if freq[nums[i - k]] == 0:
            del freq[nums[i - k]]
        if len(freq) == k:
            best = max(best, curr)
    return best
```

### Complexity
- Time: O(n)
- Space: O(k)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Fixed-Size Window with Sum + Frequency Map) | O(n) | O(k) | ✅ |
| Standard Approach 1 | O(n) | O(k) | ✅ |


---

## Key Takeaway
Combining a running sum with a running frequency map lets you validate the 'all distinct' constraint in O(1) per slide instead of re-checking the whole window each time.

---

## Reference
- LeetCode #2461 — Maximum Sum of Distinct Subarrays With Length K
