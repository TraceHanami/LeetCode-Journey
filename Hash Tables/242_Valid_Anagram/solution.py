from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Sort and Compare
# Why: Two strings are anagrams exactly when their sorted characters are identical.
# Time: O(n log n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1) (bounded alphabet)
# ─────────────────────────────────────────────────
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        from collections import Counter
        return Counter(s) == Counter(t)

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
