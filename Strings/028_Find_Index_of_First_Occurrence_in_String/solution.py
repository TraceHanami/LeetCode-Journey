# ─────────────────────────────────────────────────
# APPROACH 1: Sliding Window (Recommended)
# Time: O(n*m) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1

# ─────────────────────────────────────────────────
# APPROACH 2: Built-in find
# Time: O(n*m) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# ─────────────────────────────────────────────────
# APPROACH 3: KMP Algorithm
# Time: O(n+m) | Space: O(m)
# ─────────────────────────────────────────────────
class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:
        def build_lps(pattern):
            lps = [0] * len(pattern)
            length, i = 0, 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                elif length:
                    length = lps[length - 1]
                else:
                    i += 1
            return lps

        lps = build_lps(needle)
        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == len(needle):
                return i - j
            elif i < len(haystack) and haystack[i] != needle[j]:
                if j:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1
