# 54 — Spiral Matrix

## Problem

Given an `m x n` matrix, return all elements of the matrix in spiral order (right, down, left, up, repeating and shrinking inward).

**Difficulty:** Medium | **Topic:** Simulation

**[View on LeetCode](https://leetcode.com/problems/spiral-matrix/)**

**Examples:**

```text
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6]
```

---

## My Approach ✅

### Why I Used This Method

Simulating the walk directly is the most literal reading of "spiral order": keep a current direction, take one step, and turn 90° whenever the next cell would go out of bounds or somewhere already visited — a `visited` set makes "already visited" a simple, safe check to reason about.

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        ans = []
        visited = set()

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0

        r = c = 0

        for _ in range(m * n):
            ans.append(matrix[r][c])
            visited.add((r, c))

            nr = r + dirs[d][0]
            nc = c + dirs[d][1]

            if (
                nr < 0 or nr >= m or
                nc < 0 or nc >= n or
                (nr, nc) in visited
            ):
                d = (d + 1) % 4
                nr = r + dirs[d][0]
                nc = c + dirs[d][1]

            r, c = nr, nc

        return ans
```

### Complexity

* Time: O(m·n)
* Space: O(m·n) for the `visited` set (beyond the required output)

---

## Alternative Approaches

### Approach 2 — Shrinking Boundaries

#### Idea

Instead of tracking visited cells, maintain four boundaries (`top`, `bottom`, `left`, `right`) and walk each of the four edges of the current boundary box, shrinking it after each side is consumed. No membership checks are needed since the boundaries themselves define what's left to visit.

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                ans.append(matrix[top][c])
            top += 1

            for r in range(top, bottom + 1):
                ans.append(matrix[r][right])
            right -= 1

            if top <= bottom:
                for c in range(right, left - 1, -1):
                    ans.append(matrix[bottom][c])
                bottom -= 1

            if left <= right:
                for r in range(bottom, top - 1, -1):
                    ans.append(matrix[r][left])
                left += 1

        return ans
```

#### Complexity

* Time: O(m·n)
* Space: O(1) extra (beyond the required output)

---

## Optimal Approach 🚀

### Idea

Every cell must be visited exactly once, so O(m·n) time is optimal regardless of technique. The shrinking-boundaries approach (Approach 2) is the standard optimal solution because it achieves this without any auxiliary `visited` structure — the four boundary pointers alone fully describe the remaining unvisited region.

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                ans.append(matrix[top][c])
            top += 1

            for r in range(top, bottom + 1):
                ans.append(matrix[r][right])
            right -= 1

            if top <= bottom:
                for c in range(right, left - 1, -1):
                    ans.append(matrix[bottom][c])
                bottom -= 1

            if left <= right:
                for r in range(bottom, top - 1, -1):
                    ans.append(matrix[r][left])
                left += 1

        return ans
```

### Complexity

* Time: O(m·n)
* Space: O(1) extra

---

## Comparison

| Approach                | Time   | Space  | Recommended |
| ------------------------ | ------ | ------ | ----------- |
| My Approach (visited set)| O(m·n) | O(m·n) | ✅           |
| Shrinking Boundaries      | O(m·n) | O(1)   | 🚀 (also Optimal) |

---

## Key Takeaway

A `visited` set is a safe, general way to avoid re-walking cells, but for a fixed, predictable traversal pattern like a spiral, four shrinking boundary pointers encode exactly the same information with no extra memory.

---

## Reference

* LeetCode #54 — Spiral Matrix
