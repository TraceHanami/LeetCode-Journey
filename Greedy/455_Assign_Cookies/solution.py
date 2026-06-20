from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Greedy Two Pointers (Recommended)
# Time: O(n log n + m log m) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = cookie = 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        return child
