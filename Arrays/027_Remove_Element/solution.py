from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Repeated .remove() Calls
# Why: Quick to write using the built-in list method, though it shifts the whole list on every removal.
# Time: O(n^2)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
