# ─────────────────────────────────────────────────
# APPROACH 1: Hash Set Cycle Detection (Recommended)
# Time: O(log n) | Space: O(log n)
# ─────────────────────────────────────────────────
class Solution1:
    def isHappy(self, n: int) -> bool:
        def digit_square_sum(num):
            return sum(int(d) ** 2 for d in str(num))

        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = digit_square_sum(n)
        return True

# ─────────────────────────────────────────────────
# APPROACH 2: Floyd's Cycle Detection
# Time: O(log n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def isHappy(self, n: int) -> bool:
        def digit_square_sum(num):
            return sum(int(d) ** 2 for d in str(num))

        slow, fast = n, digit_square_sum(n)
        while fast != 1 and slow != fast:
            slow = digit_square_sum(slow)
            fast = digit_square_sum(digit_square_sum(fast))
        return fast == 1
