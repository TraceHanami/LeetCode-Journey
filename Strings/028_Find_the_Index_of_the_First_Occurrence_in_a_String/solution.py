from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Built-in str.find()
# Why: Python's find() implements substring search directly and efficiently.
# Time: O(n * m) worst case
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n * m) worst case
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
