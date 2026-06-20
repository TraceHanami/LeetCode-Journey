# ─────────────────────────────────────────────────
# APPROACH 1: Two Pointers (Recommended)
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        lo, hi = 0, len(s) - 1
        while lo < hi:
            while lo < hi and not s[lo].isalpha():
                lo += 1
            while lo < hi and not s[hi].isalpha():
                hi -= 1
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1
        return ''.join(s)
