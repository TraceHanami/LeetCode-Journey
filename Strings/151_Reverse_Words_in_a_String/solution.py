# ─────────────────────────────────────────────────
# APPROACH 1: Split and Reverse (Recommended)
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

# ─────────────────────────────────────────────────
# APPROACH 2: Two Pointers In-Place Reverse
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution2:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        lo, hi = 0, len(words) - 1
        while lo < hi:
            words[lo], words[hi] = words[hi], words[lo]
            lo += 1
            hi -= 1
        return ' '.join(words)
