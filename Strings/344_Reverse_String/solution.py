from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Two Pointers In-Place (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def reverseString(self, s: List[str]) -> None:
        lo, hi = 0, len(s) - 1
        while lo < hi:
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1

# ─────────────────────────────────────────────────
# APPROACH 2: Built-in Reverse
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
