from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Linear Scan, Check Reversal
# Why: Walk the list in order and return the first word that equals its own reverse.
# Time: O(n * k)
# Space: O(k) per check
# ─────────────────────────────────────────────────
class Solution1:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ""


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n * k)
# Space: O(k) per check
# ─────────────────────────────────────────────────
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
