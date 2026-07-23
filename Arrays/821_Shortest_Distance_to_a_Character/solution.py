from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Brute Force — Compare Against Every Occurrence
# Why: Collect all positions of c, then for each index find the closest one by scanning the whole list.
# Time: O(n * k)
# Space: O(k)
# ─────────────────────────────────────────────────
class Solution1:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        positions = [i for i in range(len(s)) if s[i] == c]
        result = []
        for i in range(len(s)):
            result.append(min(abs(i - p) for p in positions))
        return result

# ─────────────────────────────────────────────────
# MY APPROACH 2: Two-Pass Sweep (Optimal)
# Why: One left-to-right pass tracks distance since the last occurrence; one right-to-left pass tracks distance to the next occurrence — take the min of both.
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution2:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [0] * n
        prev = float('-inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = i - prev
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            result[i] = min(result[i], prev - i)
        return result


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [0] * n
        last = float('-inf')
        for i in range(n):
            if s[i] == c:
                last = i
            ans[i] = i - last
        last = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                last = i
            ans[i] = min(ans[i], last - i)
        return ans

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
