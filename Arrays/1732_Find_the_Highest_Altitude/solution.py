from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Running Total, Track the Max
# Why: The altitude at each point is a prefix sum of the gains — track the running total and remember its peak.
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def largestAltitude(self, gain: List[int]) -> int:
        best = 0
        total = 0
        for g in gain:
            total += g
            best = max(best, total)
        return best


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = highest = 0
        for g in gain:
            altitude += g
            highest = max(highest, altitude)
        return highest

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
