from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Sort, Buy Cheapest First
# Why: To maximize the count of bars bought, always buy the cheapest ones first.
# Time: O(n log n)
# Space: O(1) extra
# ─────────────────────────────────────────────────
class Solution1:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for c in costs:
            if coins >= c:
                coins -= c
                count += 1
            else:
                break
        return count


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n log n)
# Space: O(1) extra
# ─────────────────────────────────────────────────
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for cost in costs:
            if cost > coins:
                break
            coins -= cost
            count += 1
        return count

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
