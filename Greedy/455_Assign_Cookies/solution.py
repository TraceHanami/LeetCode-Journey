from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Sort Both, Two Pointer
# Why: Sorting both lists lets the smallest sufficient cookie always go to the least greedy unsatisfied child first.
# Time: O(n log n + m log m)
# Space: O(1) extra
# ─────────────────────────────────────────────────
class Solution1:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n log n + m log m)
# Space: O(1) extra
# ─────────────────────────────────────────────────
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        for cookie in s:
            if child < len(g) and cookie >= g[child]:
                child += 1
        return child

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
