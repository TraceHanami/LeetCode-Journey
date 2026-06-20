from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Reverse Check (Recommended)
# Time: O(n*m) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""

# ─────────────────────────────────────────────────
# APPROACH 2: Two Pointers
# Time: O(n*m) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(w):
            lo, hi = 0, len(w) - 1
            while lo < hi:
                if w[lo] != w[hi]:
                    return False
                lo += 1
                hi -= 1
            return True

        for word in words:
            if is_palindrome(word):
                return word
        return ""
