from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Two-Pass Constraint Propagation (Recommended)
# Time: O(n log n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        restrictions.sort()

        # Forward pass: cap each building by previous constraint
        for i in range(1, len(restrictions)):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i-1][1] + restrictions[i][0] - restrictions[i-1][0]
            )

        # Backward pass: cap each building by next constraint
        for i in range(len(restrictions) - 2, -1, -1):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i+1][1] + restrictions[i+1][0] - restrictions[i][0]
            )

        # Find max height between each pair of adjacent restrictions
        max_h = 0
        for i in range(1, len(restrictions)):
            p1, h1 = restrictions[i-1]
            p2, h2 = restrictions[i]
            # Peak between two buildings: average of heights + half the gap
            peak = (h1 + h2 + p2 - p1) // 2
            max_h = max(max_h, peak)

        return max_h
