from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Convert to Int, Add, Convert Back to Binary
# Why: Python's built-in int(..., 2) and bin() make this a one-liner.
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(max(n, m))
# Space: O(max(n, m))
# ─────────────────────────────────────────────────
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i]); i -= 1
            if j >= 0:
                total += int(b[j]); j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return "".join(reversed(result))

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
