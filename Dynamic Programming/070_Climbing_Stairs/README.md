# 70 — Climbing Stairs

## Problem

At each step you can come from one or two steps back — Fibonacci pattern.

**Difficulty:** Easy | **Topic:** Dynamic Programming

**[View on LeetCode](https://leetcode.com/problems/climbing-stairs/)**

---

## Approach 1 — Iterative DP ✅

**Idea:** dp[i] = dp[i-1] + dp[i-2]. Use two variables instead of array.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Memoization

**Idea:** Recursive with cache.

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 3 — Matrix exponentiation

**Idea:** Optimal for very large n.

**Complexity:**
- Time: O(log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Iterative DP | O(n) | O(1) | ✅ Yes |
| 2 — Memoization | O(n) | O(n) | No |
| 3 — Matrix exponentiation | O(log n) | O(1) | No |

---

## Reference

[LeetCode #70 — Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
