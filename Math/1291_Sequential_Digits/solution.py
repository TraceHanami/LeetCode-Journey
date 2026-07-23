from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Generate from a Fixed Digit Source String
# Why: Every sequential-digit number is a substring of "123456789" — generate all substrings of the right lengths and filter by range.
# Time: O(1) — at most 36 candidates total
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sample = "123456789"
        result = []
        low_len = len(str(low))
        high_len = len(str(high))
        for length in range(low_len, high_len + 1):
            for start in range(10 - length):
                num = int(sample[start:start + length])
                if low <= num <= high:
                    result.append(num)
        return result


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(1)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(len(digits) - length + 1):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    result.append(num)
        return result

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
