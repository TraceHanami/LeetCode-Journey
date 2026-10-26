# 3619 — Count Islands With Total Value Divisible by K

## Problem
You are given an `m x n` matrix `grid` of non-negative integers and a positive integer `k`. An **island** is a group of positive integers (representing land) that are 4-directionally connected (horizontally or vertically). Cells with a value of `0` represent water.

The **total value** of an island is defined as the sum of the values of all cells in that island. Return the number of islands whose total value is divisible by `k`.

**Difficulty:** Medium | **Topic:** Graphs
**[View on LeetCode](https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/)**

**Examples:**
```text
Input: grid = [[0,2,4],[0,2,0],[3,0,6]], k = 4
Output: 1
Explanation:
- Island 1: cells (0,1), (0,2), (1,1) with values 2 + 4 + 2 = 8. Since 8 % 4 == 0, this island is valid.
- Island 2: cell (2,0) with value 3. 3 % 4 != 0, so invalid.
- Island 3: cell (2,2) with value 6. 6 % 4 != 0, so invalid.
Total valid islands = 1.

Input: grid = [[1,1],[1,1]], k = 2
Output: 1
Explanation: The entire grid is one connected island with total value 1 + 1 + 1 + 1 = 4. 4 % 2 == 0, so return 1.
```

---

## My Approaches
### Attempt 1 — 4-Directional Recursive DFS with In-Place Sinking ✅ Final Accepted Solution
**Why I used it:**
Traverse each connected component using four-directional Depth-First Search. Summing the cell values along the way while setting visited land cells to `0` (sinking the island) avoids double counting and avoids allocating an auxiliary visited set.

```python
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
```

**Algorithm Steps:**
1. Determine matrix dimensions `m = len(grid)` and `n = len(grid[0])`, and initialize `count = 0`.
2. Define a recursive helper `dfs(r, c)`:
   - Boundary checks: if `r < 0`, `r >= m`, `c < 0`, or `c >= n`, return `0`.
   - Water / visited check: if `grid[r][c] == 0`, return `0`.
   - Extract the current cell's value and immediately sink it: `grid[r][c] = 0` to mark it as visited.
   - Recursively sum the values of all 4 adjacent neighbors (down, up, right, left) and return the total component value.
3. Iterate through every cell `(r, c)` of `grid`:
   - Whenever an unvisited land cell `grid[r][c] > 0` is found, initiate `dfs(r, c)` to explore and sink the entire island, capturing its `total` value.
   - If `total % k == 0`, increment `count` by 1.
4. Return `count`.

> [!WARNING]
> **Recursion Depth Caveat:** Python's default recursion limit is typically 1,000. If an island forms a long serpentine or spiral component containing more than 1,000 cells on a large grid, this recursive DFS will raise a `RecursionError`. In production or adversarial contest settings, an explicit stack or queue (iterative DFS / BFS) is required to avoid call-stack exhaustion.

**Complexity:**
- Time: O(m · n) — every cell in the grid is visited at most a constant number of times across the outer loops and DFS calls.
- Space: O(m · n) worst case — due to the recursion call stack if a single island spans the entire grid.

---

---

## Standard Approach
### Standard Approach 1 — Iterative Stack DFS ✅ Recommended for Large Inputs
### Idea
To prevent call-stack overflow on deep components, use an explicit iterative stack. We pop cells `(r, c)`, sink them, and push valid unvisited neighbors while accumulating the island sum.

```python
class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
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
```

### Complexity
- Time: O(m · n) — each cell is pushed and popped at most once.
- Space: O(m · n) — heap memory for the explicit stack, immune to Python call-stack recursion limits.

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Approach (Recursive DFS) | O(m · n) | O(m · n) recursion stack | ✅ (Concise; watch recursion depth) |
| Standard Approach (Iterative Stack DFS) | O(m · n) | O(m · n) heap memory | 🚀 (Safe on arbitrary grid sizes) |

---

## Key Takeaway
Setting visited cells to zero directly inside the matrix gives an elegant in-place flood fill that requires no separate hash set or boolean grid. However, whenever recursive DFS is applied to grid traversal in Python, keep recursion limits in mind for large connected components.

---

## Reference
- LeetCode #3619 — Count Islands With Total Value Divisible by K
