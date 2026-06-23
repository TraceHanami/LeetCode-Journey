# 83 — Remove Duplicates from Sorted List

## Problem

Single pass: skip nodes whose value equals the next node's value.

**Difficulty:** Easy | **Topic:** Linked Lists

**[View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)**

**Examples:**
```
head = [1,1,2] -> [1,2]
head = [1,1,2,3,3] -> [1,2,3]
```
---

## Approach 1 — Single pass ✅

**Idea:** If curr.val == curr.next.val, skip next node. Else advance.

```python
class Solution1:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
```

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
