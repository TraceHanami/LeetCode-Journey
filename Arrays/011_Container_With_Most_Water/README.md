# 011 — Container With Most Water

## Problem
Given n non-negative integers representing heights of vertical lines, find two lines that together with the x-axis form a container holding the most water.

**Difficulty:** Medium | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/container-with-most-water/)**

**Examples:**
```text
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

---

## My Approaches
### Attempt 1 — Two Pointer (Optimal) ✅ Final Accepted Solution
**Why I used it:**
The widest container is a good starting point; moving the shorter wall inward is the only move that can possibly increase area.

```python
def maxArea(self, height: List[int]) -> int:
    i = 0
    j = len(height) - 1
    m = 0
    while i < j:
        w = j - i
        a = w * min(height[i], height[j])
        m = max(m, a)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return m
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Start with the widest possible container (both ends). At each step, area is limited by the shorter wall, so moving the taller wall inward can only shrink or keep the width down without any chance of a taller wall — always move the shorter side.

```python
def maxArea(self, height: List[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        best = max(best, width * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best
```

### Complexity
- Time: O(n)
- Space: O(1)

---
### Standard Approach 2 — Alternative
### Idea
Brute force checks every pair of lines directly — useful as a baseline to see why the two-pointer trick is worth learning.

```python
def maxArea(self, height: List[int]) -> int:
    best = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            best = max(best, (j - i) * min(height[i], height[j]))
    return best
```

### Complexity
- Time: O(n^2)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Two Pointer (Optimal)) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |
| Standard Approach 2 | O(n^2) | O(1) | Optional |


---

## Key Takeaway
Greedily moving the shorter wall inward is provably safe — it's the only move that could ever increase the area.

---

## Reference
- LeetCode #11 — Container With Most Water
