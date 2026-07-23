from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Strip Trailing Spaces, Scan Backward
# Why: Trim trailing whitespace, then count characters from the end until hitting a space.
# Time: O(n)
# Space: O(1) extra
# ─────────────────────────────────────────────────
class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        s = s.rstrip()
        for ch in reversed(s):
            if ch == ' ':
                break
            length += 1
        return length


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
