# ─────────────────────────────────────────────────
# APPROACH 1: Reverse Half the Number (Recommended)
# Time: O(log n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        return x == reversed_half or x == reversed_half // 10

# ─────────────────────────────────────────────────
# APPROACH 2: String Conversion
# Time: O(log n) | Space: O(log n)
# ─────────────────────────────────────────────────
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
