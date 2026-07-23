from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: DFS Backtracking with Visit Marking
# Why: Since every empty square must be visited exactly once, explore all four directions recursively, marking cells visited (and un-marking on backtrack) while counting steps taken.
# Time: O(4^(r*c)) worst case (bounded by small grid constraints)
# Space: O(r*c) recursion depth
# ─────────────────────────────────────────────────
class Solution1:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        start_r, start_c = 0, 0
        empty_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                if grid[r][c] != -1:
                    empty_count += 1
        self.paths = 0

        def dfs(r, c, steps):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == -1:
                return
            if grid[r][c] == 2:
                if steps == empty_count:
                    self.paths += 1
                return
            temp, grid[r][c] = grid[r][c], -1
            dfs(r + 1, c, steps + 1)
            dfs(r, c + 1, steps + 1)
            dfs(r - 1, c, steps + 1)
            dfs(r, c - 1, steps + 1)
            grid[r][c] = temp

        dfs(start_r, start_c, 1)
        return self.paths


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: Exponential worst case, fine for the small grids in this problem
# Space: O(r*c)
# ─────────────────────────────────────────────────
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        empty = sum(row.count(0) for row in grid) + 1  # +1 for the start square
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    sr, sc = r, c

        self.count = 0

        def backtrack(r, c, remaining):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == -1:
                return
            if grid[r][c] == 2:
                if remaining == 0:
                    self.count += 1
                return
            grid[r][c] = -1
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                backtrack(r + dr, c + dc, remaining - 1)
            grid[r][c] = 0

        backtrack(sr, sc, empty)
        return self.count

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
