from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Dummy Head, Splice Smaller Node Each Step
# Why: A dummy head node avoids special-casing the first node, and comparing heads at each step naturally builds the merged list in order.
# Time: O(n + m)
# Space: O(1) extra
# ─────────────────────────────────────────────────
class Solution1:
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


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n + m)
# Space: O(1) extra
# ─────────────────────────────────────────────────
class Solution:
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

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
