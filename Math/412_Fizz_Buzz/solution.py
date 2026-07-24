from typing import *

# ==================================================
# MY APPROACH (Original Submission)
# ==================================================
# Why:
# Check the "divisible by both" case first, then each individual
# case, directly mirroring the problem statement's rules.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                a.append("FizzBuzz")
            elif i%3==0:
                a.append("Fizz")
            elif i%5==0:
                a.append("Buzz")
            else:
                a.append(str(i))
        return a
# Time: O(n)
# Space: O(1) extra

# ==================================================
# ALTERNATIVE APPROACHES
# ==================================================

# Approach 2 - String Concatenation
class SolutionConcat:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            s = ""
            if i % 3 == 0:
                s += "Fizz"
            if i % 5 == 0:
                s += "Buzz"
            ans.append(s or str(i))
        return ans
# Time: O(n)
# Space: O(1) extra

# ==================================================
# OPTIMAL APPROACH
# ==================================================
# Same O(n) lower bound as any approach here - every number must be
# examined once. Concatenation style shown for clean generalizability.

class SolutionOptimal:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            label = ("Fizz" if i % 3 == 0 else "") + ("Buzz" if i % 5 == 0 else "")
            result.append(label if label else str(i))
        return result
# Time: O(n)
# Space: O(1) extra
