# 83 — Remove Duplicates from Sorted List

## Problem

Single pass: skip nodes whose value equals the next node's value.

**Difficulty:** Easy | **Topic:** Linked Lists

**[View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)**

---

## Approach 1 — Single pass ✅

**Idea:** If curr.val == curr.next.val, skip next node. Else advance.

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Single pass | O(n) | O(1) | ✅ Yes |

---

## Reference

[LeetCode #83 — Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
