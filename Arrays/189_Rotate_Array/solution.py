from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Three Reverses (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(lo, hi):
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

# ─────────────────────────────────────────────────
# APPROACH 2: Extra Array
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        temp = nums[:]
        for i in range(n):
            nums[(i + k) % n] = temp[i]

# ─────────────────────────────────────────────────
# APPROACH 3: Cyclic Replacement
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        count = 0
        start = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                if current == start:
                    break
            start += 1
