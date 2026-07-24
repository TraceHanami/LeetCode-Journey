from typing import *

# ==================================================
# MY APPROACH (Original Submission)
# ==================================================
# Why:
# Python's built-in ** operator already handles integer exponentiation
# correctly, including negative exponents and zero.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
# Time: O(log n) in practice (CPython uses exponentiation by squaring internally)
# Space: O(1)

# ==================================================
# ALTERNATIVE APPROACHES
# ==================================================

# Approach 2 - Naive Repeated Multiplication
class SolutionNaive:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        result = 1.0
        for _ in range(n):
            result *= x
        return result
# Time: O(n)
# Space: O(1)

# ==================================================
# OPTIMAL APPROACH
# ==================================================
# Exponentiation by squaring, made explicit: halve the exponent each
# recursive step instead of decrementing by one.

class SolutionOptimal:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(base: float, exp: int) -> float:
            if exp == 0:
                return 1.0
            half = fast_pow(base, exp // 2)
            if exp % 2 == 0:
                return half * half
            return half * half * base

        if n < 0:
            x = 1 / x
            n = -n
        return fast_pow(x, n)
# Time: O(log n)
# Space: O(log n) recursion depth
