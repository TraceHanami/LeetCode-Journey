# ─────────────────────────────────────────────────
# APPROACH 1: Simulation (Recommended)
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def processStr(self, s: str) -> str:
        result = []
        for c in s:
            if c == '*':
                result = result * 2
            elif c == '#':
                if result:
                    result.pop()
            else:
                result.append(c)
        return ''.join(result)
