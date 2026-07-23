from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: String Reversal via bin()
# Why: Convert to a zero-padded 32-bit binary string, reverse it, and parse it back to an int.
# Time: O(32) = O(1)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:].zfill(32)
        return int(bits[::-1], 2)


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(32) = O(1)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
