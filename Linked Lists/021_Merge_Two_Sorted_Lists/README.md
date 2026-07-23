# 021 — Merge Two Sorted Lists

## Problem
Merge two sorted linked lists into one sorted list by splicing together their nodes.

**Difficulty:** Easy | **Topic:** Linked Lists
**[View on LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)**

**Examples:**
```text
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4]
```

---

## My Approaches
### Attempt 1 — Dummy Head, Splice Smaller Node Each Step ✅ Final Accepted Solution
**Why I used it:**
A dummy head node avoids special-casing the first node, and comparing heads at each step naturally builds the merged list in order.

```python
def mergeTwoLists(self, list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    tail.next = list1 if list1 else list2
    return dummy.next
```

**Complexity:**
- Time: O(n + m)
- Space: O(1) extra

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Use a dummy head to simplify edge cases, then repeatedly attach whichever list's current node is smaller. Once one list is exhausted, splice the remainder of the other list on directly (no need to walk it node by node).

```python
def mergeTwoLists(self, list1, list2):
    dummy = tail = ListNode()
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next, list1 = list1, list1.next
        else:
            tail.next, list2 = list2, list2.next
        tail = tail.next
    tail.next = list1 or list2
    return dummy.next
```

### Complexity
- Time: O(n + m)
- Space: O(1) extra

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Dummy Head, Splice Smaller Node Each Step) | O(n + m) | O(1) extra | ✅ |
| Standard Approach 1 | O(n + m) | O(1) extra | ✅ |


---

## Key Takeaway
A dummy head node is the standard trick for building a linked list result without special-casing the first insertion.

---

## Reference
- LeetCode #21 — Merge Two Sorted Lists
