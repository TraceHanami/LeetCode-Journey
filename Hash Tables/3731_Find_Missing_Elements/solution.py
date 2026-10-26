from typing import List

# ─────────────────────────────────────────────────
# MY APPROACH: Hash Set Range Scan with Empty Guard
# Why: Hash set provides O(1) membership check; scanning from
#      min to max yields missing elements in sorted order.
# Time: O(n + R) where R = max(nums) - min(nums) + 1
# Space: O(n) auxiliary space for the set
# ─────────────────────────────────────────────────
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        s = set(nums)
        missing = []
        for num in range(min(nums), max(nums) + 1):
            if num not in s:
                missing.append(num)
        return missing


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH: Sorting and Adjacent Gap Scan
# Why: Sorts in place and detects gaps between adjacent values.
# Time: O(n log n + k) where k is the count of missing elements
# Space: O(1) auxiliary space beyond the output list
# ─────────────────────────────────────────────────
class SolutionSortGap:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        missing = []

        for i in range(1, len(nums)):
            for val in range(nums[i - 1] + 1, nums[i]):
                missing.append(val)

        return missing


# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    sol_gap = SolutionSortGap()

    # Test 1: Missing middle element
    input_1 = [1, 4, 2, 5]
    expected_1 = [3]
    assert sol.findMissingElements(list(input_1)) == expected_1
    assert sol_gap.findMissingElements(list(input_1)) == expected_1
    print("Test 1 passed:", expected_1)

    # Test 2: No missing elements
    input_2 = [1, 2, 3]
    expected_2 = []
    assert sol.findMissingElements(list(input_2)) == expected_2
    assert sol_gap.findMissingElements(list(input_2)) == expected_2
    print("Test 2 passed:", expected_2)

    # Test 3: Empty list guard
    input_3 = []
    expected_3 = []
    assert sol.findMissingElements(list(input_3)) == expected_3
    assert sol_gap.findMissingElements(list(input_3)) == expected_3
    print("Test 3 passed:", expected_3)

    print("All tests passed!")
