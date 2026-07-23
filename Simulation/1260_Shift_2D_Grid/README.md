# 1260 — Shift 2D Grid

## Problem
Given a 2D grid and an integer k, shift the grid k times, where each shift moves every element to the next position (wrapping around row-by-row and grid-to-grid).

**Difficulty:** Easy | **Topic:** Simulation
**[View on LeetCode](https://leetcode.com/problems/shift-2d-grid/)**

**Examples:**
```text
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
```

---

## My Approaches
### Attempt 1 — Flatten, Rotate, Reshape ✅ Final Accepted Solution
**Why I used it:**
A 2D wrap-around shift is equivalent to rotating the flattened 1D version of the grid, then splitting it back into rows.

```python
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
```

**Complexity:**
- Time: O(m * n)
- Space: O(m * n)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Treat the grid as a flattened 1D array. A single grid-shift is exactly a right rotation of that flattened array by 1 (with wraparound); k shifts is a rotation by k mod (m*n). Rotate using slicing, then chop the flattened result back into rows of length n.

```python
def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    flat = [val for row in grid for val in row]
    k %= m * n
    rotated = flat[-k:] + flat[:-k] if k else flat
    return [rotated[i:i + n] for i in range(0, m * n, n)]
```

### Complexity
- Time: O(m * n)
- Space: O(m * n)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Flatten, Rotate, Reshape) | O(m * n) | O(m * n) | ✅ |
| Standard Approach 1 | O(m * n) | O(m * n) | ✅ |


---

## Key Takeaway
A 2D wrap-around shift is just a 1D array rotation in disguise — flatten, rotate, then re-chunk into rows.

---

## Reference
- LeetCode #1260 — Shift 2D Grid
