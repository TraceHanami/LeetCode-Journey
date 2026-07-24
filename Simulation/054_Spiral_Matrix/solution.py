from typing import *

# ==================================================
# MY APPROACH (Original Submission)
# ==================================================
# Why:
# Simulate the walk directly: track current direction, step, and
# turn 90 degrees when the next cell is out of bounds or visited.

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
# Time: O(m*n)
# Space: O(m*n) for the visited set

# ==================================================
# ALTERNATIVE APPROACHES
# ==================================================

# Approach 2 - Shrinking Boundaries
class SolutionBoundaries:
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
# Time: O(m*n)
# Space: O(1) extra

# ==================================================
# OPTIMAL APPROACH
# ==================================================
# Same shrinking-boundaries technique as Approach 2 - four boundary
# pointers fully describe the unvisited region, no extra set needed.

class SolutionOptimal:
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
# Time: O(m*n)
# Space: O(1) extra
