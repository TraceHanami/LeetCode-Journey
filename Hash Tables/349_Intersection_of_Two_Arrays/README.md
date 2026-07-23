# 349 — Intersection of Two Arrays

## Problem
Given two integer arrays, return an array of their unique intersection (each element appears once).

**Difficulty:** Easy | **Topic:** Hash Tables
**[View on LeetCode](https://leetcode.com/problems/intersection-of-two-arrays/)**

**Examples:**
```text
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

---

## My Approaches
### Attempt 1 — Set Intersection ✅ Final Accepted Solution
**Why I used it:**
Python's built-in set operations directly express the intersection semantics needed here.

```python
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))
```

**Complexity:**
- Time: O(n + m)
- Space: O(n + m)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Converting both arrays to sets and intersecting them directly matches the problem's requirement of unique, order-independent output — no need for manual loops.

```python
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))
```

### Complexity
- Time: O(n + m)
- Space: O(n + m)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Set Intersection) | O(n + m) | O(n + m) | ✅ |
| Standard Approach 1 | O(n + m) | O(n + m) | ✅ |


---

## Key Takeaway
When a problem explicitly wants a unique, unordered intersection, built-in set operations are both the simplest and most efficient tool.

---

## Reference
- LeetCode #349 — Intersection of Two Arrays
