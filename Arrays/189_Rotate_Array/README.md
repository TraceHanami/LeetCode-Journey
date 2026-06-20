# 189 — Rotate Array

## Problem

Reverse the whole array, then reverse each part separately.

**Difficulty:** Med | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/rotate-array/)**

---

## Approach 1 — Three reverses ✅

**Idea:** Reverse all, reverse first k, reverse remaining n-k.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Extra array

**Idea:** Place each element at (i+k)%n in a new array.

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 3 — Cyclic replacement

**Idea:** Follow cycles — place each element at its final position.

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Three reverses | O(n) | O(1) | ✅ Yes |
| 2 — Extra array | O(n) | O(n) | No |
| 3 — Cyclic replacement | O(n) | O(1) | No |

---

## Reference

[LeetCode #189 — Rotate Array](https://leetcode.com/problems/rotate-array/)
