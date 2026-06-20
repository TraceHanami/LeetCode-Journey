from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Boyer-Moore Voting (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate

# ─────────────────────────────────────────────────
# APPROACH 2: Hash Map
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        return Counter(nums).most_common(1)[0][0]

# ─────────────────────────────────────────────────
# APPROACH 3: Sort
# Time: O(n log n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
