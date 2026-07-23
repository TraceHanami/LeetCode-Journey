from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: XOR All Characters
# Why: XORing every character of both strings together cancels all matching pairs, leaving only the extra character's code.
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def findTheDifference(self, s: str, t: str) -> str:
        r = 0
        for ch in s + t:
            r ^= ord(ch)
        return chr(r)


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for ch in s + t:
            result ^= ord(ch)
        return chr(result)

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
