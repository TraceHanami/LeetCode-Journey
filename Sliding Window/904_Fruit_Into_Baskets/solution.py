from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Variable-Size Sliding Window with Type Counts
# Why: Expand the window by adding fruits; whenever more than 2 distinct types appear, shrink from the left until back down to 2.
# Time: O(n)
# Space: O(1) (at most 3 keys)
# ─────────────────────────────────────────────────
class Solution1:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        counts = {}
        best = 0
        for j in range(len(fruits)):
            counts[fruits[j]] = counts.get(fruits[j], 0) + 1
            while len(counts) > 2:
                counts[fruits[i]] -= 1
                if counts[fruits[i]] == 0:
                    del counts[fruits[i]]
                i += 1
            best = max(best, j - i + 1)
        return best


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        count = {}
        best = 0
        for right, fruit in enumerate(fruits):
            count[fruit] = count.get(fruit, 0) + 1
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            best = max(best, right - left + 1)
        return best

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
