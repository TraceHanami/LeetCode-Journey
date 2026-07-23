# 169 — Majority Element

## Problem
Given an array of size n, return the element that appears more than n/2 times.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/majority-element/)**

**Examples:**
```text
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

---

## My Approaches
### Attempt 1 — Frequency Map
**Why I used it:**
Count occurrences of every value, then check which one crosses the n/2 threshold.

```python
def majorityElement(self, nums: List[int]) -> int:
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    for k, v in freq.items():
        if v > len(nums) // 2:
            return k
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---
### Attempt 2 — Boyer-Moore Voting ✅ Final Accepted Solution
**Why I used it:**
Since a true majority element is guaranteed to exist, votes for/against a candidate cancel out and the majority always survives.

```python
def majorityElement(self, nums: List[int]) -> int:
    count = 0
    candidate = None
    for n in nums:
        if count == 0:
            candidate = n
        count += 1 if n == candidate else -1
    return candidate
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Boyer-Moore Voting: maintain a candidate and a counter. Increment the counter when seeing the candidate, decrement otherwise. When the counter hits zero, switch candidates. Because the majority element appears more than n/2 times, it's guaranteed to outlast every other value's cancellations.

```python
def majorityElement(self, nums: List[int]) -> int:
    count = 0
    candidate = None
    for n in nums:
        if count == 0:
            candidate = n
        count += 1 if n == candidate else -1
    return candidate
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Boyer-Moore Voting) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |
| Frequency Map | O(n) | O(n) | ❌ |


---

## Key Takeaway
Boyer-Moore Voting solves this in O(1) space by treating it as a cancellation game — the guaranteed majority element can never be fully cancelled out.

---

## Reference
- LeetCode #169 — Majority Element
