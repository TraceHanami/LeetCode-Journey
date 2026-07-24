from typing import *

# ==================================================
# MY APPROACH (Original Submission)
# ==================================================
# Why:
# Two pointers walking s and t together; advance t always,
# advance s only on a match.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
# Time: O(len(t))
# Space: O(1)

# ==================================================
# ALTERNATIVE APPROACHES
# ==================================================

# Approach 2 - Python Iterator Trick
class SolutionIterator:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        return all(ch in it for ch in s)
# Time: O(len(t))
# Space: O(1)

# ==================================================
# OPTIMAL APPROACH
# ==================================================
# For the "many queries against the same t" follow-up:
# pre-index t by character, binary-search next valid position.

import bisect
from collections import defaultdict

class SolutionOptimal:
    def isSubsequence(self, s: str, t: str) -> bool:
        positions = defaultdict(list)
        for idx, ch in enumerate(t):
            positions[ch].append(idx)

        prev = -1
        for ch in s:
            idxs = positions.get(ch)
            if not idxs:
                return False
            pos = bisect.bisect_right(idxs, prev)
            if pos == len(idxs):
                return False
            prev = idxs[pos]
        return True
# Time: O(len(t)) preprocess + O(len(s) log len(t)) per query
# Space: O(len(t))
