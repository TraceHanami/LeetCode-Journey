from typing import *

# ==================================================
# MY APPROACH (Original Submission)
# ==================================================
# Why:
# Sliding window with a set of characters currently in the window;
# shrink from the left one step at a time whenever a duplicate is found.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=set()
        j=0
        r=0
        for i in range(len(s)):
            while s[i] in a:
                a.remove(s[j])
                j+=1
            a.add(s[i])
            r=max(r,i-j+1)
        return r
# Time: O(n)
# Space: O(min(n, m))

# ==================================================
# ALTERNATIVE APPROACHES
# ==================================================

# Approach 2 - Brute Force
class SolutionBruteForce:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        best = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                best = max(best, j - i + 1)
        return best
# Time: O(n^2)
# Space: O(min(n, m))

# ==================================================
# OPTIMAL APPROACH
# ==================================================

class SolutionOptimal:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            best = max(best, right - left + 1)
        return best
# Time: O(n)
# Space: O(min(n, m))
