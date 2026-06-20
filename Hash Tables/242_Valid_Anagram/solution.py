# ─────────────────────────────────────────────────
# APPROACH 1: Counter Comparison (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)

# ─────────────────────────────────────────────────
# APPROACH 2: Sort and Compare
# Time: O(n log n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
