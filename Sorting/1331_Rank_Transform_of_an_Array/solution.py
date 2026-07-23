from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Sort Unique Values, Map to Rank
# Why: Sorting the deduplicated values directly gives their rank order — position i in the sorted list is rank i+1.
# Time: O(n log n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_unique = sorted(set(arr))
        rank = {}
        for i, v in enumerate(sorted_unique, 1):
            rank[v] = i
        return [rank[x] for x in arr]


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n log n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {v: i + 1 for i, v in enumerate(sorted(set(arr)))}
        return [rank[x] for x in arr]

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
