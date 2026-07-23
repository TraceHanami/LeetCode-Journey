from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Character-by-Character Vertical Scan
# Why: Compare column by column against the first string — stop the moment any string diverges or runs out.
# Time: O(S) where S = total characters
# Space: O(1) extra
# ─────────────────────────────────────────────────
class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = ""
        first = strs[0]
        for i in range(len(first)):
            for word in strs:
                if i >= len(word) or word[i] != first[i]:
                    return prefix
            prefix += first[i]
        return prefix


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(S)
# Space: O(1) extra
# ─────────────────────────────────────────────────
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i, ch in enumerate(strs[0]):
            for word in strs[1:]:
                if i >= len(word) or word[i] != ch:
                    return strs[0][:i]
        return strs[0]

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
