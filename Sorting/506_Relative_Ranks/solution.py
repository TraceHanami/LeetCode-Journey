from typing import *

# ==================================================
# MY APPROACH (Original Submission)
# ==================================================
# Why:
# Sort a copy of the scores descending to get rank order, build a
# score -> medal/rank map, then relabel the original array via lookup.

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a = sorted(score, reverse=True)

        d = {}

        for i in range(len(a)):
            if i == 0:
                d[a[i]] = "Gold Medal"
            elif i == 1:
                d[a[i]] = "Silver Medal"
            elif i == 2:
                d[a[i]] = "Bronze Medal"
            else:
                d[a[i]] = str(i + 1)

        for i in range(len(score)):
            score[i] = d[score[i]]

        return score
# Time: O(n log n)
# Space: O(n)

# ==================================================
# ALTERNATIVE APPROACHES
# ==================================================

# Approach 2 - Sort (Index, Score) Pairs Directly
class SolutionIndexSort:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        order = sorted(range(n), key=lambda i: score[i], reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result = [""] * n
        for rank, idx in enumerate(order):
            result[idx] = medals[rank] if rank < 3 else str(rank + 1)
        return result
# Time: O(n log n)
# Space: O(n)

# ==================================================
# OPTIMAL APPROACH
# ==================================================
# Same sort-based technique, writing directly into the result array
# by original index instead of round-tripping through a hash map.

class SolutionOptimal:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        order = sorted(range(n), key=lambda i: -score[i])
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result = [""] * n
        for rank, idx in enumerate(order):
            result[idx] = medals[rank] if rank < 3 else str(rank + 1)
        return result
# Time: O(n log n)
# Space: O(n)
