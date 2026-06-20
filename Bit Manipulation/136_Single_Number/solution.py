from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: XOR (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

# ─────────────────────────────────────────────────
# APPROACH 2: Hash Set
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return seen.pop()

# ─────────────────────────────────────────────────
# APPROACH 3: Math
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
