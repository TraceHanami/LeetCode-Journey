from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Convert to String
# Why: Simplest check — reverse the string form and compare.
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]

# ─────────────────────────────────────────────────
# MY APPROACH 2: Reverse Half the Number
# Why: Avoids string conversion and stops halfway once the reversed part meets or passes the remaining part.
# Time: O(log10 n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(log10 n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
