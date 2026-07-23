from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Direct String Simulation
# Why: Simulate each operation directly against a growing string result, following the rules exactly as specified.
# Time: O(n * L) where L grows with duplication
# Space: O(L)
# ─────────────────────────────────────────────────
class Solution1:
    def processStr(self, s: str) -> str:
        r = ""
        for ch in s:
            if ch == '*':
                if r:
                    r = r[:-1]
            elif ch == '#':
                r = r + r
            elif ch == '%':
                r = r[::-1]
            else:
                r += ch
        return r


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n * L)
# Space: O(L)
# ─────────────────────────────────────────────────
class Solution:
    def processStr(self, s: str) -> str:
        result = ""
        for ch in s:
            if ch == '*':
                result = result[:-1] if result else result
            elif ch == '#':
                result += result
            elif ch == '%':
                result = result[::-1]
            else:
                result += ch
        return result

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
