from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Frequency Map
# Why: Count occurrences of every value, then check which one crosses the n/2 threshold.
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for k, v in freq.items():
            if v > len(nums) // 2:
                return k

# ─────────────────────────────────────────────────
# MY APPROACH 2: Boyer-Moore Voting
# Why: Since a true majority element is guaranteed to exist, votes for/against a candidate cancel out and the majority always survives.
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if n == candidate else -1
        return candidate


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if n == candidate else -1
        return candidate

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
