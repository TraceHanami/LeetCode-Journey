from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: split() + reversed join
# Why: Python's split() already collapses multiple spaces and strips leading/trailing whitespace, so reversing the resulting list is enough.
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(reversed(words))

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
