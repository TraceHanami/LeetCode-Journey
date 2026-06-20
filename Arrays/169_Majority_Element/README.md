# 169 — Majority Element

## Problem

Boyer-Moore Voting: the majority element cancels out all others.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/majority-element/)**

---

## Approach 1 — Boyer-Moore Voting ✅

**Idea:** Maintain candidate and count. Increment if same, decrement if different, reset at 0.

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Hash map count

**Idea:** Count frequencies with Counter, return element with count > n//2.

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 3 — Sort

**Idea:** Sorted array — majority element always occupies index n//2.

**Complexity:**
- Time: O(n log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Boyer-Moore Voting | O(n) | O(1) | ✅ Yes |
| 2 — Hash map count | O(n) | O(n) | No |
| 3 — Sort | O(n log n) | O(1) | No |

---

## Reference

[LeetCode #169 — Majority Element](https://leetcode.com/problems/majority-element/)
