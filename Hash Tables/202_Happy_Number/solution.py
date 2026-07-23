from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Cycle Detection with a Seen Set
# Why: If a number repeats, the sequence is stuck in an infinite loop that will never reach 1 — track seen values to detect that.
# Time: O(log n) per step, bounded overall
# Space: O(k) for the seen set
# ─────────────────────────────────────────────────
class Solution1:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            total = 0
            while n > 0:
                d = n % 10
                total += d ** 2
                n //= 10
            n = total
        return n == 1


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(log n) per step
# Space: O(k)
# ─────────────────────────────────────────────────
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(d) ** 2 for d in str(n))
        return n == 1

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
