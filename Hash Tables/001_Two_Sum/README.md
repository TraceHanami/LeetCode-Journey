# 001 — Two Sum

## Problem
Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target. Each input has exactly one solution, and you may not use the same element twice.

**Difficulty:** Easy | **Topic:** Hash Tables
**[View on LeetCode](https://leetcode.com/problems/two-sum/)**

**Examples:**
```text
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]
```

---

## My Approaches
### Attempt 1 — Brute Force (Nested Loops)
**Why I used it:**
Simplest way to check every pair without thinking about extra space.

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

**Complexity:**
- Time: O(n^2)
- Space: O(1)

---
### Attempt 2 — Hash Map (One Pass) ✅ Final Accepted Solution
**Why I used it:**
Trade space for time — store what's been seen and look up the complement instead of re-scanning.

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    s = {}
    for i, n in enumerate(nums):
        c = target - n
        if c in s:
            return [s[c], i]
        s[n] = i
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Single pass with a hash map: for each number, check if its complement (target - num) has already been seen. If so, return both indices immediately — no need for a second pass.

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
```

### Complexity
- Time: O(n)
- Space: O(n)

---
### Standard Approach 2 — Alternative
### Idea
Build the hash map fully first, then scan again looking up complements. Slightly less elegant than the one-pass version but sometimes taught first since it's more intuitive.

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {n: i for i, n in enumerate(nums)}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen and seen[complement] != i:
            return [i, seen[complement]]
```

### Complexity
- Time: O(n)
- Space: O(n)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Hash Map (One Pass)) | O(n) | O(n) | ✅ |
| Standard Approach 1 | O(n) | O(n) | ✅ |
| Standard Approach 2 | O(n) | O(n) | Optional |
| Brute Force (Nested Loops) | O(n^2) | O(1) | ❌ |


---

## Key Takeaway
Trading space for time with a hash map turns an O(n^2) pairwise search into a single O(n) pass by checking for a number's complement as you go, instead of re-scanning the array.

---

## Reference
- LeetCode #1 — Two Sum
