from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Propagate Restrictions Left-to-Right and Right-to-Left, Then Sweep
# Why: Turn the restrictions into a sorted list of (position, cap) pairs including the fixed endpoints, then tighten every cap based on its neighbors in both directions before computing the achievable peak between each adjacent pair.
# Time: O(n log n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        r = restrictions[:]
        r.append([1, 0])
        r.sort()
        if r[-1][0] != n:
            r.append([n, n - 1])
        m = len(r)
        for i in range(1, m):
            d = r[i][0] - r[i - 1][0]
            r[i][1] = min(r[i][1], r[i - 1][1] + d)
        for i in range(m - 2, -1, -1):
            d = r[i + 1][0] - r[i][0]
            r[i][1] = min(r[i][1], r[i + 1][1] + d)
        best = 0
        for i in range(1, m):
            x, h = r[i - 1]
            y, k = r[i]
            d = y - x
            best = max(best, (h + k + d) // 2)
        return best


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n log n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        points = sorted(restrictions + [[1, 0]])
        if points[-1][0] != n:
            points.append([n, n - 1])
        for i in range(1, len(points)):
            dist = points[i][0] - points[i - 1][0]
            points[i][1] = min(points[i][1], points[i - 1][1] + dist)
        for i in range(len(points) - 2, -1, -1):
            dist = points[i + 1][0] - points[i][0]
            points[i][1] = min(points[i][1], points[i + 1][1] + dist)
        best = 0
        for (x1, h1), (x2, h2) in zip(points, points[1:]):
            dist = x2 - x1
            best = max(best, (h1 + h2 + dist) // 2)
        return best

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
