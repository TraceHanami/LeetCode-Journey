from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Set Membership While Scanning
# Why: Check membership before adding, so the first repeat is caught immediately without a second pass.
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

# ─────────────────────────────────────────────────
# MY APPROACH 2: Compare Lengths of List vs Set
# Why: A set automatically discards duplicates — if its length differs from the original list, duplicates exist.
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
