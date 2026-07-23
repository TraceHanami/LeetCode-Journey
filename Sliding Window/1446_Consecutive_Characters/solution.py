from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Running Streak Counter
# Why: Track the current run length, resetting whenever the character changes, and keep the max.
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def maxPower(self, s: str) -> int:
        best = streak = 1
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                streak += 1
            else:
                streak = 1
            best = max(best, streak)
        return best


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def maxPower(self, s: str) -> int:
        best = streak = 1
        for i in range(1, len(s)):
            streak = streak + 1 if s[i] == s[i - 1] else 1
            best = max(best, streak)
        return best

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
