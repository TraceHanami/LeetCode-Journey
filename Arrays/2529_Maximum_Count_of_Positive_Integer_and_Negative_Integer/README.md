# 2529 — Maximum Count of Positive Integer and Negative Integer

## Problem

Count negatives and positives separately (zeros excluded); return the larger count.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/)**

---

## Approach 1 — Linear scan ✅

**Idea:** Count neg (< 0) and pos (> 0). Return max of both.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Binary search

**Idea:** Use bisect to find boundary of negatives and positives.

**Complexity:**
- Time: O(log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Linear scan | O(n) | O(1) | ✅ Yes |
| 2 — Binary search | O(log n) | O(1) | No |

---

## Reference

[LeetCode #2529 — Maximum Count of Positive Integer and Negative Integer](https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/)
