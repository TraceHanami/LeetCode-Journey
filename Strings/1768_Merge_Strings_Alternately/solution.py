from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Two Pointer, Alternate Append
# Why: Walk both strings in lockstep, appending one character from each per step, then tack on whatever's left.
# Time: O(n + m)
# Space: O(n + m)
# ─────────────────────────────────────────────────
class Solution1:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = j = 0
        while i < len(word1) and j < len(word2):
            result += word1[i]
            result += word2[j]
            i += 1
            j += 1
        result += word1[i:]
        result += word2[j:]
        return result


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n + m)
# Space: O(n + m)
# ─────────────────────────────────────────────────
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        from itertools import zip_longest
        return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
