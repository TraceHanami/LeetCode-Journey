from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Two-Way Mapping Dictionaries
# Why: A one-to-one mapping must be consistent in both directions, so track mappings from s->t and t->s simultaneously.
# Time: O(n)
# Space: O(1) (bounded alphabet)
# ─────────────────────────────────────────────────
class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m, z = {}, {}
        for i, j in zip(s, t):
            if i in m and m[i] != j:
                return False
            if j in z and z[j] != i:
                return False
            m[i] = j
            z[j] = i
        return True


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1) (bounded alphabet)
# ─────────────────────────────────────────────────
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t, t_to_s = {}, {}
        for a, b in zip(s, t):
            if a in s_to_t and s_to_t[a] != b:
                return False
            if b in t_to_s and t_to_s[b] != a:
                return False
            s_to_t[a] = b
            t_to_s[b] = a
        return True

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
