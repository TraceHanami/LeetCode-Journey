# ─────────────────────────────────────────────────
# APPROACH 1: Bit-by-Bit (Recommended)
# Time: O(1) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

# ─────────────────────────────────────────────────
# APPROACH 2: Python String Reverse
# Time: O(1) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)
