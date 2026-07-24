from typing import *

# ==================================================
# MY APPROACH (Original Submission)
# ==================================================
# Why:
# Base-26 conversion where 'A'-'Z' stand in for digits 1-26;
# multiply the running total by 26 and add the next letter's value.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        r=0
        for i in columnTitle:
            r=r*26+(ord(i)-64)
        return r
# Time: O(n)
# Space: O(1)

# ==================================================
# ALTERNATIVE APPROACHES
# ==================================================

# Approach 2 - reduce One-Liner
from functools import reduce

class SolutionReduce:
    def titleToNumber(self, columnTitle: str) -> int:
        return reduce(lambda acc, ch: acc * 26 + (ord(ch) - 64), columnTitle, 0)
# Time: O(n)
# Space: O(1)

# ==================================================
# OPTIMAL APPROACH
# ==================================================
# Same base-26 accumulation as "My Approach" - already optimal,
# just spelled out with ord('A') for clarity instead of the magic number 64.

class SolutionOptimal:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for ch in columnTitle:
            result = result * 26 + (ord(ch) - ord('A') + 1)
        return result
# Time: O(n)
# Space: O(1)
