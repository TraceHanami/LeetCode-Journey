from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Fixed-Size Window with Sum + Frequency Map
# Why: Track both a running sum and a frequency count for the window of size k, only counting it as a candidate answer when the frequency map shows exactly k distinct values.
# Time: O(n)
# Space: O(k)
# ─────────────────────────────────────────────────
class Solution1:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = {}
        curr = 0
        for i in range(k):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            curr += nums[i]
        best = curr if len(freq) == k else 0
        for i in range(k, len(nums)):
            left, right = nums[i - k], nums[i]
            curr += right - left
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]
            freq[right] = freq.get(right, 0) + 1
            if len(freq) == k:
                best = max(best, curr)
        return best


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(k)
# ─────────────────────────────────────────────────
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        from collections import Counter
        freq = Counter(nums[:k])
        curr = sum(nums[:k])
        best = curr if len(freq) == k else 0
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            freq[nums[i]] += 1
            freq[nums[i - k]] -= 1
            if freq[nums[i - k]] == 0:
                del freq[nums[i - k]]
            if len(freq) == k:
                best = max(best, curr)
        return best

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
