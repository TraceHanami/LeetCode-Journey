# 258 — Add Digits

## Problem

Digital root formula: result is 0 if n=0, 9 if n%9==0, else n%9.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/add-digits/)**

---

## Approach 1 — Digital root formula ✅

**Idea:** return 0 if n==0 else 9 if n%9==0 else n%9.

**Complexity:**
- Time: O(1)
- Space: O(1)

---

## Approach 2 — Simulation

**Idea:** Repeatedly sum digits until single digit.

**Complexity:**
- Time: O(log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Digital root formula | O(1) | O(1) | ✅ Yes |
| 2 — Simulation | O(log n) | O(1) | No |

---

## Reference

[LeetCode #258 — Add Digits](https://leetcode.com/problems/add-digits/)
