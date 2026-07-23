from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Fixed-Size Sliding Window Sum
# Why: Maintain a running sum for the current window of size k, adding the new element and subtracting the one that leaves, instead of resumming from scratch each time.
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        best = window_sum / k
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            best = max(best, window_sum / k)
        return best


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        best = curr
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            best = max(best, curr)
        return best / k

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
