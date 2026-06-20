# ─────────────────────────────────────────────────
# APPROACH 1: Two Pointers Greedy (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in t:
            if i < len(s) and c == s[i]:
                i += 1
        return i == len(s)

# ─────────────────────────────────────────────────
# APPROACH 2: Recursive
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        if s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        return self.isSubsequence(s, t[1:])
