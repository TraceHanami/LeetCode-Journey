# 217 — Contains Duplicate

## Problem
Given an integer array, return true if any value appears at least twice.

**Difficulty:** Easy | **Topic:** Hash Tables
**[View on LeetCode](https://leetcode.com/problems/contains-duplicate/)**

**Examples:**
```text
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false
```

---

## My Approaches
### Attempt 1 — Set Membership While Scanning
**Why I used it:**
Check membership before adding, so the first repeat is caught immediately without a second pass.

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---
### Attempt 2 — Compare Lengths of List vs Set ✅ Final Accepted Solution
**Why I used it:**
A set automatically discards duplicates — if its length differs from the original list, duplicates exist.

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Converting to a set removes duplicates automatically; comparing lengths tells you in one line whether any duplicates existed. Functionally identical in complexity to scanning with a seen-set, just more concise.

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
```

### Complexity
- Time: O(n)
- Space: O(n)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Compare Lengths of List vs Set) | O(n) | O(n) | ✅ |
| Standard Approach 1 | O(n) | O(n) | ✅ |
| Set Membership While Scanning | O(n) | O(n) | ❌ |


---

## Key Takeaway
Both a scan-with-seen-set and a length-comparison approach are O(n) time and space — the length comparison is just a terser way to express the same idea.

---

## Reference
- LeetCode #217 — Contains Duplicate
