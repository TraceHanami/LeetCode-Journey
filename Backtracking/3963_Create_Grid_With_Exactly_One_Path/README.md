# 3963 — Create Grid With Exactly One Path

## Problem
Given two integers `m` and `n`, construct an `m x n` grid containing only `'.'` and `'#'`, such that exactly one valid path exists from the top-left cell `(0, 0)` to the bottom-right cell `(m - 1, n - 1)`.

- `'.'` represents a free cell.
- `'#'` represents an obstacle.
- Movement is allowed only to the right or down.

**Difficulty:** Easy | **Topic:** Greedy, Matrix

**[View on LeetCode](https://leetcode.com/problems/create-grid-with-exactly-one-path/)**

**Examples:**
```text
Input: m = 2, n = 3
Output: ["..#", "#.."]

Input: m = 3, n = 3
Output: ["..#", "#..", "##."]

Input: m = 1, n = 4
Output: ["...."]
```

---

## My Approaches

### Attempt 1 — Construct a Single L-Shaped Path ✅ Final Accepted Solution

**Why I used it:**

Instead of using DFS, BFS, or dynamic programming to count paths, I construct a grid in which only one route is available. The route moves right across the first row and then down the last column. All other cells remain blocked.

This guarantees exactly one valid path without requiring path counting or backtracking.

```python
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        g = [["#"] * n for _ in range(m)]

        for j in range(n):
            g[0][j] = "."

        for i in range(m):
            g[i][n - 1] = "."

        return ["".join(r) for r in g]
```

### Algorithm Steps

1. **Initialize the grid:** Create an `m x n` grid filled entirely with `'#'`. Initially, every cell is blocked.
2. **Open the first row:** Iterate through all columns using `j` and replace every cell in row `0` with `'.'`.
3. **Open the last column:** Iterate through all rows using `i` and replace every cell in column `n - 1` with `'.'`.
4. **Convert rows to strings:** Use `"".join(r)` to convert each row from a list of characters into a string.
5. **Return the grid:** Return the list of strings representing the constructed grid.

### Why It Works

The only free cells are those in the first row and the last column.

- From `(0, 0)`, the path can move right along the first row.
- Once it reaches `(0, n - 1)`, it can move down the last column.
- All alternative routes are blocked by `'#'`.
- The destination `(m - 1, n - 1)` is reachable through this single route.

Therefore, exactly one valid path exists.

### Complexity

- **Time:** `O(m * n)` — Initializing the grid requires `O(m * n)` time. Opening the first row and last column takes `O(m + n)`, and converting the rows to strings takes `O(m * n)`.
- **Space:** `O(m * n)` — The grid stores `m * n` cells, and the returned list of strings also requires space proportional to the grid size.

---

## Standard Approach

### Standard Approach 1 — Construct a Single Monotonic Path ✅

### Idea

A valid path can be constructed by selecting any route that moves only right and down, then blocking every cell that does not belong to that route.

The simplest choice is to move right until reaching the last column and then move down until reaching the destination.

This is a constructive algorithm: instead of searching for a path, we design the grid so that the desired path is the only possible one.

```python
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        g = []

        for i in range(m):
            r = ""

            for j in range(n):
                if i == 0 or j == n - 1:
                    r += "."
                else:
                    r += "#"

            g.append(r)

        return g
```

### Algorithm Steps

1. Initialize an empty list `g` to store the completed rows.
2. Iterate through each row using `i`.
3. Create an empty string `r` for the current row.
4. Iterate through every column using `j`.
5. If `i == 0` or `j == n - 1`, append `'.'` because the cell belongs to the intended path.
6. Otherwise, append `'#'` to block the cell.
7. Append the completed row `r` to `g`.
8. Return `g` after all rows have been constructed.

### Complexity

- **Time:** `O(m * n)` — Every cell is visited exactly once.
- **Space:** `O(m * n)` — The output grid contains `m * n` cells.

---

## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| My Approach (Initialize with Obstacles, Open Path) | `O(m * n)` | `O(m * n)` | ✅ |
| Standard Approach (Build Each Row Directly) | `O(m * n)` | `O(m * n)` | ✅ |

Both approaches produce a valid grid. The first approach is easier to understand because it starts with every cell blocked and explicitly opens the required path. The second approach constructs the same grid directly.

---

## Key Takeaway

For constructive problems, it is not always necessary to search for a solution using graph traversal or dynamic programming. Sometimes, the simplest approach is to design the input so that the required property is guaranteed.

Here, opening the first row and the last column creates a single L-shaped route. Blocking every other cell prevents alternative paths.

**Core idea:** Construct one valid path and block all alternative routes.

---

## Reference

- LeetCode #3963 — Create Grid With Exactly One Path
