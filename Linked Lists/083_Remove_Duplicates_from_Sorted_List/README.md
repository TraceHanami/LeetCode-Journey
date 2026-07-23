# 083 — Remove Duplicates from Sorted List

## Problem
Given the head of a sorted linked list, delete all duplicates so each element appears only once.

**Difficulty:** Easy | **Topic:** Linked Lists
**[View on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)**

**Examples:**
```text
Input: head = [1,1,2,3,3]
Output: [1,2,3]
```

---

## My Approaches
### Attempt 1 — Skip Forward When Values Match ✅ Final Accepted Solution
**Why I used it:**
Since the list is sorted, duplicates are always adjacent — just relink past them without deleting the current pointer.

```python
def deleteDuplicates(self, head):
    original_head = head
    while head and head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return original_head
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Walk the list with a single pointer. Whenever the current node's value equals the next node's value, skip over the next node by relinking. Otherwise advance normally — sortedness guarantees all duplicates are adjacent, so one pass suffices.

```python
def deleteDuplicates(self, head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Skip Forward When Values Match) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
Sortedness guarantees duplicates are adjacent, so a single pointer relinking past matches is enough — no extra data structure needed.

---

## Reference
- LeetCode #83 — Remove Duplicates from Sorted List
