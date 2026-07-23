from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Manual Substring Scan
# Why: For each pattern, manually slide a window across word checking for an exact match, rather than relying on the 'in' operator.
# Time: O(k * n * m)
# Space: O(1) extra
# ─────────────────────────────────────────────────
class Solution1:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        n = len(word)
        for p in patterns:
            m = len(p)
            if m > n:
                continue
            for i in range(n - m + 1):
                if word[i:i + m] == p:
                    count += 1
                    break
        return count


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(k * n) average
# Space: O(1) extra
# ─────────────────────────────────────────────────
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(1 for p in patterns if p in word)

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
