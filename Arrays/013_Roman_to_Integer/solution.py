roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


# ─────────────────────────────────────────────
# APPROACH 1: Brute Force — Replace Subtractive Pairs
# Time: O(1) | Space: O(n)
# ─────────────────────────────────────────────
class Solution1:
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")

        return sum(roman[c] for c in s)


# ─────────────────────────────────────────────
# APPROACH 2: Left-to-Right Comparison (Optimal)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────
class Solution2:
    def romanToInt(self, s: str) -> int:
        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total


# ─────────────────────────────────────────────
# APPROACH 3: Right-to-Left Iteration
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────
class Solution3:
    def romanToInt(self, s: str) -> int:
        total = roman[s[-1]]
        prev = roman[s[-1]]

        for i in range(len(s) - 2, -1, -1):
            curr = roman[s[i]]
            if curr < prev:
                total -= curr
            else:
                total += curr
            prev = curr

        return total


# ─────────────────────────────────────────────
# APPROACH 4: Pairwise Lookup
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────
class Solution4:
    def romanToInt(self, s: str) -> int:
        combined = {
            'I': 1,   'V': 5,   'X': 10,  'L': 50,
            'C': 100, 'D': 500, 'M': 1000,
            'IV': 4,  'IX': 9,  'XL': 40,
            'XC': 90, 'CD': 400,'CM': 900,
        }
        total = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in combined:
                total += combined[s[i:i+2]]
                i += 2
            else:
                total += combined[s[i]]
                i += 1

        return total
