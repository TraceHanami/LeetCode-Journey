from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Prefix-Sum DP over Value Range
# Why: For each position, track how many zigzag arrays end at each value going 'up' vs 'down' next, using prefix sums to update whole ranges in O(m) per step instead of O(m^2).
# Time: O(n * m)
# Space: O(m)
# ─────────────────────────────────────────────────
class Solution1:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7
        m = r - l + 1
        if n == 1:
            return m
        up = [0] * (m + 1)
        down = [0] * (m + 1)
        for i in range(1, m + 1):
            up[i] = i - 1
            down[i] = m - i
        if n == 2:
            return (sum(up) + sum(down)) % mod
        for _ in range(n - 2):
            pu = [0] * (m + 1)
            pd = [0] * (m + 1)
            for i in range(1, m + 1):
                pu[i] = (pu[i - 1] + up[i]) % mod
                pd[i] = (pd[i - 1] + down[i]) % mod
            total_up = pu[m]
            nu = [0] * (m + 1)
            nd = [0] * (m + 1)
            for i in range(1, m + 1):
                nu[i] = pd[i - 1]
                nd[i] = (total_up - pu[i]) % mod
            up, down = nu, nd
        return (sum(up) + sum(down)) % mod


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n * m)
# Space: O(m)
# ─────────────────────────────────────────────────
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        if n == 1:
            return m % MOD
        up = [i for i in range(m + 1)]      # up[i] placeholder, real init below
        up = [0] + [1] * m
        down = [0] + [1] * m
        for _ in range(n - 2):
            prefix_up = [0] * (m + 1)
            prefix_down = [0] * (m + 1)
            for i in range(1, m + 1):
                prefix_up[i] = (prefix_up[i - 1] + up[i]) % MOD
                prefix_down[i] = (prefix_down[i - 1] + down[i]) % MOD
            new_up, new_down = [0] * (m + 1), [0] * (m + 1)
            for i in range(1, m + 1):
                new_up[i] = prefix_down[i - 1]
                new_down[i] = (prefix_up[m] - prefix_up[i]) % MOD
            up, down = new_up, new_down
        return (sum(up) + sum(down)) % MOD

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
