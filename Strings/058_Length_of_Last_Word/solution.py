# ─────────────────────────────────────────────────
# APPROACH 1: Strip and Split (Recommended)
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])

# ─────────────────────────────────────────────────
# APPROACH 2: Reverse Scan
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1
        return count
