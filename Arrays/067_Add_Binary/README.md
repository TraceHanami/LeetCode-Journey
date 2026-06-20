# 67 — Add Binary

## Problem

String simulation using carry logic — similar to how you'd add two numbers by hand.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/add-binary/)**

---

## Approach 1 — Simulation with carry ✅

**Idea:** Iterate from right to left, adding bits with a carry. Append remainder and reverse.

**Complexity:**
- Time: O(max(n,m))
- Space: O(max(n,m))

---

## Approach 2 — Python int conversion

**Idea:** Convert both binary strings to integers, add, convert back to binary.

**Complexity:**
- Time: O(n+m)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Simulation with carry | O(max(n,m)) | O(max(n,m)) | ✅ Yes |
| 2 — Python int conversion | O(n+m) | O(1) | No |

---

## Reference

[LeetCode #67 — Add Binary](https://leetcode.com/problems/add-binary/)
