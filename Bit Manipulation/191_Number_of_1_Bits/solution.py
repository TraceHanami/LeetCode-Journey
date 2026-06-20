# ─────────────────────────────────────────────────
# APPROACH 1: Bit Mask Loop (Recommended)
# Time: O(1) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

# ─────────────────────────────────────────────────
# APPROACH 2: Brian Kernighan's Algorithm
# Time: O(k) where k = number of set bits | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1  # clears lowest set bit
            count += 1
        return count

# ─────────────────────────────────────────────────
# APPROACH 3: Built-in bin()
# Time: O(1) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution3:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
