from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Filter and Compare Reversed
# Why: Build a cleaned lowercase-alphanumeric version of the string, then compare it to its reverse.
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
        return cleaned == cleaned[::-1]


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1) extra
# ─────────────────────────────────────────────────
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
