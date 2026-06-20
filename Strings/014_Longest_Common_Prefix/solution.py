from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Vertical Scanning (Recommended)
# Time: O(n*m) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i, char in enumerate(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        return strs[0]

# ─────────────────────────────────────────────────
# APPROACH 2: Sort and Compare Extremes
# Time: O(n log n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        prefix = ""
        for a, b in zip(strs[0], strs[-1]):
            if a == b:
                prefix += a
            else:
                break
        return prefix

# ─────────────────────────────────────────────────
# APPROACH 3: Divide and Conquer
# Time: O(n*m) | Space: O(m log n)
# ─────────────────────────────────────────────────
class Solution3:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp(s1, s2):
            i = 0
            while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
                i += 1
            return s1[:i]

        def helper(arr, lo, hi):
            if lo == hi:
                return arr[lo]
            mid = (lo + hi) // 2
            left = helper(arr, lo, mid)
            right = helper(arr, mid + 1, hi)
            return lcp(left, right)

        return helper(strs, 0, len(strs) - 1) if strs else ""
