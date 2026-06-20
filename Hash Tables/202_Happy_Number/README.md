# 202 — Happy Number

## Problem

Repeatedly sum digit squares; detect cycle using a set or fast/slow pointers.

**Difficulty:** Easy | **Topic:** Hash Tables

**[View on LeetCode](https://leetcode.com/problems/happy-number/)**

---

## Approach 1 — Hash set cycle detection ✅

**Idea:** Store seen sums in a set. Return True if reach 1, False if sum repeats.

**Complexity:**
- Time: O(log n)
- Space: O(log n)

---

## Approach 2 — Floyd's cycle detection

**Idea:** Slow moves one step, fast moves two. Cycle detected when they meet; happy if fast reaches 1.

**Complexity:**
- Time: O(log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Hash set cycle detection | O(log n) | O(log n) | ✅ Yes |
| 2 — Floyd's cycle detection | O(log n) | O(1) | No |

---

## Reference

[LeetCode #202 — Happy Number](https://leetcode.com/problems/happy-number/)
