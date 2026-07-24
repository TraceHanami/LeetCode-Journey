from typing import *

# ==================================================
# MY APPROACH (Original Submission)
# ==================================================
# Why:
# Two pointers closing in from both ends; only swap when both sides
# are letters, otherwise skip whichever side is a non-letter.

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        while(i<j):
            if s[i].isalpha() and s[j].isalpha():
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif not s[i].isalpha():
                i+=1
            else:
                j-=1
        return "".join(s)
# Time: O(n)
# Space: O(n)

# ==================================================
# ALTERNATIVE APPROACHES
# ==================================================

# Approach 2 - Stack of Letters
class SolutionStack:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [ch for ch in s if ch.isalpha()]
        result = []
        for ch in s:
            if ch.isalpha():
                result.append(letters.pop())
            else:
                result.append(ch)
        return "".join(result)
# Time: O(n)
# Space: O(n)

# ==================================================
# OPTIMAL APPROACH
# ==================================================
# Same two-pointer technique as "My Approach" - already optimal,
# just written with an explicit early-continue style.

class SolutionOptimal:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = list(s)
        i, j = 0, len(chars) - 1
        while i < j:
            if not chars[i].isalpha():
                i += 1
            elif not chars[j].isalpha():
                j -= 1
            else:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
        return "".join(chars)
# Time: O(n)
# Space: O(n)
