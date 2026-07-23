# 980 — Unique Paths III

## Problem
Given a grid with a start (1), an end (2), obstacles (-1), and empty squares (0), count the number of paths from start to end that walk over every non-obstacle square exactly once.

**Difficulty:** Hard | **Topic:** Backtracking
**[View on LeetCode](https://leetcode.com/problems/unique-paths-iii/)**

**Examples:**
```text
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
```

---

## My Approaches
### Attempt 1 — DFS Backtracking with Visit Marking ✅ Final Accepted Solution
**Why I used it:**
Since every empty square must be visited exactly once, explore all four directions recursively, marking cells visited (and un-marking on backtrack) while counting steps taken.

```python
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
```

**Complexity:**
- Time: O(4^(r*c)) worst case (bounded by small grid constraints)
- Space: O(r*c) recursion depth

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
This is a Hamiltonian-path-style counting problem, which generally requires exhaustive backtracking since there's no known polynomial algorithm for the general case. DFS from the start square, marking each visited cell temporarily as an obstacle (-1) to prevent revisits, and restoring it on backtrack. A path only counts when it reaches the end square having visited every non-obstacle cell exactly once.

```python
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
```

### Complexity
- Time: Exponential worst case, fine for the small grids in this problem
- Space: O(r*c)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (DFS Backtracking with Visit Marking) | O(4^(r*c)) worst case (bounded by small grid constraints) | O(r*c) recursion depth | ✅ |
| Standard Approach 1 | Exponential worst case, fine for the small grids in this problem | O(r*c) | ✅ |


---

## Key Takeaway
Path problems requiring every cell to be visited exactly once are Hamiltonian-path variants — backtracking with a 'mark visited, explore, unmark' pattern is the standard approach since no efficient general algorithm exists.

---

## Reference
- LeetCode #980 — Unique Paths III
