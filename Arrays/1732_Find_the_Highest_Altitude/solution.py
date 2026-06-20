from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Prefix Sum (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = curr = 0
        for g in gain:
            curr += g
            max_alt = max(max_alt, curr)
        return max_alt
