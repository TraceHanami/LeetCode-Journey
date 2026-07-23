from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Single Pass Building Both Values Digit-by-Digit
# Why: Process digits from the least significant end, skipping zeros, building the concatenated result with a positional multiplier while simultaneously accumulating the digit sum.
# Time: O(log n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def sumAndMultiply(self, n: int) -> int:
        concat = digit_sum = 0
        place = 1
        while n > 0:
            d = n % 10
            if d != 0:
                digit_sum += d
                concat += d * place
                place *= 10
            n //= 10
        return concat * digit_sum


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(log n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        concat, digit_sum, place = 0, 0, 1
        while n > 0:
            digit = n % 10
            n //= 10
            if digit == 0:
                continue
            digit_sum += digit
            concat += digit * place
            place *= 10
        return concat * digit_sum

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
