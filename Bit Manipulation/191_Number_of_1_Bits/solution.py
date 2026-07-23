from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Count '1's in Binary String
# Why: Convert to binary text and count the characters that equal '1'.
# Time: O(32) = O(1)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def hammingWeight(self, n: int) -> int:
        bits = bin(n)[2:]
        return sum(1 for b in bits if b == '1')


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(k) where k = number of set bits
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
