# ─────────────────────────────────────────────────
# APPROACH 1: XOR (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for c in s + t:
            result ^= ord(c)
        return chr(result)


# ─────────────────────────────────────────────────
# APPROACH 2: Counter Difference
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        diff = Counter(t) - Counter(s)
        return list(diff.keys())[0]


# ─────────────────────────────────────────────────
# APPROACH 3: Sum of ASCII Values
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution3:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(ord(c) for c in t) - sum(ord(c) for c in s))


# ─────────────────────────────────────────────────
# APPROACH 4: Sort and Compare
# Time: O(n log n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution4:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = sorted(s), sorted(t)
        for cs, ct in zip(s, t):
            if cs != ct:
                return ct
        return t[-1]
