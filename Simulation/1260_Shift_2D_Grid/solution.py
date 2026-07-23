from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Flatten, Rotate, Reshape
# Why: A 2D wrap-around shift is equivalent to rotating the flattened 1D version of the grid, then splitting it back into rows.
# Time: O(m * n)
# Space: O(m * n)
# ─────────────────────────────────────────────────
class Solution1:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
        flat = [grid[r][c] for r in range(m) for c in range(n)]
        shifted = flat[-k:] + flat[:-k] if k > 0 else flat
        result = []
        for i in range(m):
            result.append(shifted[i * n:(i + 1) * n])
        return result


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(m * n)
# Space: O(m * n)
# ─────────────────────────────────────────────────
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        flat = [val for row in grid for val in row]
        k %= m * n
        rotated = flat[-k:] + flat[:-k] if k else flat
        return [rotated[i:i + n] for i in range(0, m * n, n)]

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
