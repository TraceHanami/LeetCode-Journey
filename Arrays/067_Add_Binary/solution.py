# ─────────────────────────────────────────────────
# APPROACH 1: Simulation with Carry (Recommended)
# Time: O(max(n,m)) | Space: O(max(n,m))
# ─────────────────────────────────────────────────
class Solution1:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return ''.join(reversed(result))

# ─────────────────────────────────────────────────
# APPROACH 2: Python int conversion
# Time: O(n+m) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
