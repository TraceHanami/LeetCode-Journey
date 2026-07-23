from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Track Length, Then Replay Backward to Locate Index k
# Why: Since '#' can double the string length repeatedly (making it too large to build), first track the length after each operation, then walk operations backward mapping index k through each transformation to find its origin.
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def processStr(self, s: str, k: int) -> str:
        n = []
        c = 0
        for ch in s:
            if ch == "*":
                if c > 0:
                    c -= 1
            elif ch == "#":
                c *= 2
            elif ch not in "*#%":
                c += 1
            n.append(c)
        if k >= c:
            return "."
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch == "#":
                half = n[i] // 2
                k %= half
            elif ch == "%":
                k = n[i] - 1 - k
            elif ch not in "#%*":
                if k == n[i] - 1:
                    return ch
        return "."


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = []
        length = 0
        for ch in s:
            if ch == "*":
                length = max(0, length - 1)
            elif ch == "#":
                length *= 2
            else:
                length += 1
            lengths.append(length)
        if k >= length:
            return "."
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch == "#":
                k %= lengths[i] // 2
            elif ch == "%":
                k = lengths[i] - 1 - k
            elif ch != "*":
                if k == lengths[i] - 1:
                    return ch
        return "."

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
