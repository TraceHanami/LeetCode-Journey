# 21 — Merge Two Sorted Lists

## Problem

Compare heads of both lists, attach the smaller, advance that pointer.

**Difficulty:** Easy | **Topic:** Linked Lists

**[View on LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)**

**Examples:**
```
list1 = [1,2,4], list2 = [1,3,4] -> [1,1,2,3,4,4]
list1 = [], list2 = [] -> []
list1 = [], list2 = [0] -> [0]
```
---

## Approach 1 — Iterative with dummy head ✅

**Idea:** Use a dummy node to simplify edge cases. Attach remaining list at end.

```python
class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return dummy.next
```

**Complexity:**
- Time: O(n+m)
- Space: O(1)

---

## Approach 2 — Recursive

**Idea:** Base case: one list empty. Attach smaller head and recurse.

```python
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
```

**Complexity:**
- Time: O(n+m)
- Space: O(n+m)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Iterative with dummy head | O(n+m) | O(1) | ✅ Yes |
| 2 — Recursive | O(n+m) | O(n+m) | No |

---

## Reference

[LeetCode #21 — Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
