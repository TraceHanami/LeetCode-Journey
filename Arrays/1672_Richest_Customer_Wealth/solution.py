from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Running List of Prefix Sums
# Why: Accumulated sums per row into a flat list, then took the max — works but does more bookkeeping than necessary.
# Time: O(n * m)
# Space: O(n * m)
# ─────────────────────────────────────────────────
class Solution1:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sums = []
        for row in accounts:
            s = 0
            for v in row:
                s += v
                sums.append(s)
        return max(sums)

# ─────────────────────────────────────────────────
# MY APPROACH 2: Sum Each Row, Take the Max
# Why: Only the final row total matters, so no need to store every partial sum.
# Time: O(n * m)
# Space: O(1) extra
# ─────────────────────────────────────────────────
class Solution2:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(row) for row in accounts)


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n * m)
# Space: O(1) extra
# ─────────────────────────────────────────────────
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(row) for row in accounts)

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
