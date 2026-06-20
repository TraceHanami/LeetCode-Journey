# 509 — Fibonacci Number

## Problem

Bottom-up DP with two variables — no array needed.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/fibonacci-number/)**

---

## Approach 1 — Iterative DP ✅

**Idea:** Track prev two values, iterate to n.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Recursive with memoization

**Idea:** Cache results to avoid recomputation.

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 3 — Matrix exponentiation

**Idea:** Fast method for very large n.

**Complexity:**
- Time: O(log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Iterative DP | O(n) | O(1) | ✅ Yes |
| 2 — Recursive with memoization | O(n) | O(n) | No |
| 3 — Matrix exponentiation | O(log n) | O(1) | No |

---

## Reference

[LeetCode #509 — Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
