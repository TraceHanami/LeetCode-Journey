from typing import List

# ─────────────────────────────────────────────────
# MY APPROACH: Recursive Backtracking with Balance Constraints
# Why: Prunes invalid branches using two counters: i < n allows
#      adding '(', and j < i ensures ')' never exceeds '('.
# Time: O(4^n / √n) — asymptotically bounded by the Catalan number
# Space: O(n) auxiliary recursion depth + output storage
# ─────────────────────────────────────────────────
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a = []

        def sol(s, i, j):
            if len(s) == 2 * n:
                a.append(s)
                return
            if i < n:
                sol(s + "(", i + 1, j)
            if j < i:
                sol(s + ")", i, j + 1)

        sol("", 0, 0)
        return a


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH: Backtracking with Character Buffer
# Why: Same branching invariants, using an in-place list buffer to
#      avoid intermediate string allocations across recursion frames.
# Time: O(4^n / √n)
# Space: O(n) auxiliary space (recursion stack and path buffer)
# ─────────────────────────────────────────────────
class SolutionBacktrackBuffer:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrack(open_count: int, close_count: int):
            if len(path) == 2 * n:
                res.append("".join(path))
                return

            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, close_count)
                path.pop()

            if close_count < open_count:
                path.append(")")
                backtrack(open_count, close_count + 1)
                path.pop()

        backtrack(0, 0)
        return res


# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    sol_buffer = SolutionBacktrackBuffer()

    # Test 1: n = 1
    expected_1 = ["()"]
    assert sol.generateParenthesis(1) == expected_1
    assert sol_buffer.generateParenthesis(1) == expected_1
    print("Test 1 (n=1) passed:", sol.generateParenthesis(1))

    # Test 2: n = 3
    expected_3 = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sol.generateParenthesis(3) == expected_3
    assert sol_buffer.generateParenthesis(3) == expected_3
    print("Test 2 (n=3) passed:", sol.generateParenthesis(3))

    print("All tests passed!")
