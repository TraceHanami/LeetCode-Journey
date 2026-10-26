from typing import List

# ─────────────────────────────────────────────────
# MY APPROACH: 4-Directional Recursive DFS with Sinking
# Why: Sinks visited land cells to 0 to prevent re-exploration;
#      accumulates connected component sums to test divisibility by k.
# Caveat: Deep recursion may exceed Python's recursion limit on large grids.
# Time: O(m * n)
# Space: O(m * n) worst-case recursion call stack
# ─────────────────────────────────────────────────
class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0

            if grid[r][c] == 0:
                return 0

            value = grid[r][c]
            grid[r][c] = 0

            value += dfs(r + 1, c)
            value += dfs(r - 1, c)
            value += dfs(r, c + 1)
            value += dfs(r, c - 1)

            return value

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    total = dfs(r, c)

                    if total % k == 0:
                        count += 1

        return count


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH: Iterative Stack DFS
# Why: Employs an explicit stack to traverse islands without
#      exceeding Python's recursion call stack limit.
# Time: O(m * n)
# Space: O(m * n) heap memory for the explicit stack
# ─────────────────────────────────────────────────
class SolutionIterative:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    island_sum = 0
                    stack = [(r, c)]
                    island_sum += grid[r][c]
                    grid[r][c] = 0

                    while stack:
                        cr, cc = stack.pop()
                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0
                                stack.append((nr, nc))

                    if island_sum % k == 0:
                        count += 1

        return count


# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    sol_iter = SolutionIterative()

    # Test 1: Grid with 3 islands, one divisible by k=4
    grid1_a = [[0, 2, 4], [0, 2, 0], [3, 0, 6]]
    grid1_b = [[0, 2, 4], [0, 2, 0], [3, 0, 6]]
    res1 = sol.countIslands(grid1_a, 4)
    res1_iter = sol_iter.countIslands(grid1_b, 4)
    assert res1 == 1 and res1_iter == 1
    print("Test 1 passed:", res1)

    # Test 2: Grid where all land connects, total=4 divisible by k=2
    grid2_a = [[1, 1], [1, 1]]
    grid2_b = [[1, 1], [1, 1]]
    res2 = sol.countIslands(grid2_a, 2)
    res2_iter = sol_iter.countIslands(grid2_b, 2)
    assert res2 == 1 and res2_iter == 1
    print("Test 2 passed:", res2)

    print("All tests passed!")
