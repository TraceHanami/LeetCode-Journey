```python
# ─────────────────────────────────────────────────
# MY APPROACH: Initialize with Obstacles, Open Path
# Why: Start with all cells blocked, then open the
#      first row and last column to create one path.
# Time: O(m * n)
# Space: O(m * n)
# ─────────────────────────────────────────────────
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        g = [["#"] * n for _ in range(m)]

        for j in range(n):
            g[0][j] = "."

        for i in range(m):
            g[i][n - 1] = "."

        return ["".join(r) for r in g]


# ─────────────────────────────────────────────────
# STANDARD APPROACH: Build Each Row Directly
# Why: Construct the grid cell by cell. Keep cells
#      in the first row or last column free.
# Time: O(m * n)
# Space: O(m * n)
# ─────────────────────────────────────────────────
class SolutionStandard:
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


# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    std = SolutionStandard()

    # Test 1: m = 2, n = 3
    exp = ["..#", "#.."]
    assert sol.createGrid(2, 3) == exp
    assert std.createGrid(2, 3) == exp
    print("Test 1 passed:", sol.createGrid(2, 3))

    # Test 2: m = 3, n = 3
    exp = ["..#", "##.", "##."]
    assert sol.createGrid(3, 3) == exp
    assert std.createGrid(3, 3) == exp
    print("Test 2 passed:", sol.createGrid(3, 3))

    # Test 3: m = 1, n = 4
    exp = ["...."]
    assert sol.createGrid(1, 4) == exp
    assert std.createGrid(1, 4) == exp
    print("Test 3 passed:", sol.createGrid(1, 4))

    # Test 4: m = 4, n = 1
    exp = [".", ".", ".", "."]
    assert sol.createGrid(4, 1) == exp
    assert std.createGrid(4, 1) == exp
    print("Test 4 passed:", sol.createGrid(4, 1))

    print("All tests passed!")
```
