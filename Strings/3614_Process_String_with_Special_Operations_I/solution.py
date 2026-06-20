# ─────────────────────────────────────────────────
# APPROACH 1: Modular Length Tracking (Recommended)
# Time: O(n) | Space: O(n)
# Note: Uses modular arithmetic to handle exponential string growth
# ─────────────────────────────────────────────────
class Solution1:
    def processStr(self, s: str) -> str:
        # Track operations without building huge intermediate strings
        MOD = 10**9 + 7
        length = 0
        ops = []

        for c in s:
            if c == '*':
                length = (length * 2) % MOD
                ops.append(('*', None))
            elif c == '#':
                if length > 0:
                    length = (length - 1) % MOD
                    ops.append(('#', None))
            else:
                length = (length + 1) % MOD
                ops.append(('char', c))

        # Reconstruct only final needed characters (reverse pass)
        result = []
        size = length
        for op_type, val in reversed(ops):
            if op_type == 'char' and size > 0:
                result.append(val)
                size -= 1
            elif op_type == '#':
                size += 1
            elif op_type == '*':
                size = (size + 1) // 2

        return ''.join(reversed(result))
