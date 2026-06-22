from typing import List

# ─────────────────────────────────────────────────
# APPROACH 1: Greedy — Sort and Buy Cheapest First (Recommended)
# Time: O(n log n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for cost in costs:
            if coins >= cost:
                coins -= cost
                count += 1
            else:
                break
        return count


# ─────────────────────────────────────────────────
# APPROACH 2: Counting Sort (Optimal for bounded values)
# Time: O(n + max_cost) | Space: O(max_cost)
# ─────────────────────────────────────────────────
class Solution2:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        freq = [0] * (max_cost + 1)
        for cost in costs:
            freq[cost] += 1

        count = 0
        for price in range(1, max_cost + 1):
            if coins < price:
                break
            # Buy as many bars at this price as we can afford
            can_buy = min(freq[price], coins // price)
            count += can_buy
            coins -= can_buy * price

        return count
