from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: len(str(n))
# Why: Converting to a string makes counting digits trivial.
# Time: O(n * d)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                count += 1
        return count

# ─────────────────────────────────────────────────
# MY APPROACH 2: Count Digits by Division
# Why: Avoids string conversion — divide by 10 repeatedly to count digits directly.
# Time: O(n * d)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            digits = 0
            while n > 0:
                n //= 10
                digits += 1
            if digits % 2 == 0:
                count += 1
        return count


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n * d)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for n in nums if len(str(n)) % 2 == 0)

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
