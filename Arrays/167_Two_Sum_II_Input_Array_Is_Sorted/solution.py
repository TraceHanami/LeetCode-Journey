from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Two Pointer (Optimal)
# Why: Since the array is sorted, moving pointers inward based on whether the sum is too big or small avoids any extra space.
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1, j + 1]
            elif s > target:
                j -= 1
            else:
                i += 1


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            if total > target:
                right -= 1
            else:
                left += 1

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
