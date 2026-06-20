# ─────────────────────────────────────────────────
# APPROACH 1: Filter and Reverse (Recommended)
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        return filtered == filtered[::-1]

# ─────────────────────────────────────────────────
# APPROACH 2: Two Pointers
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s) - 1
        while lo < hi:
            while lo < hi and not s[lo].isalnum():
                lo += 1
            while lo < hi and not s[hi].isalnum():
                hi -= 1
            if s[lo].lower() != s[hi].lower():
                return False
            lo += 1
            hi -= 1
        return True
