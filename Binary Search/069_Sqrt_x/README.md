# 69 — Sqrt x

## Problem

Binary search on the answer space from 0 to x.

**Difficulty:** Easy | **Topic:** Binary Search

**[View on LeetCode](https://leetcode.com/problems/sqrt-x/)**

---

## Approach 1 — Binary search ✅

**Idea:** Search for largest k where k*k <= x.

**Complexity:**
- Time: O(log x)
- Space: O(1)

---

## Approach 2 — Newton's method

**Idea:** x1 = (x0 + n/x0)/2 converges fast to sqrt.

**Complexity:**
- Time: O(log x)
- Space: O(1)

---

## Approach 3 — Built-in

**Idea:** int(math.sqrt(x)) — not recommended in interviews.

**Complexity:**
- Time: O(1)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Binary search | O(log x) | O(1) | ✅ Yes |
| 2 — Newton's method | O(log x) | O(1) | No |
| 3 — Built-in | O(1) | O(1) | No |

---

## Reference

[LeetCode #69 — Sqrt x](https://leetcode.com/problems/sqrt-x/)
