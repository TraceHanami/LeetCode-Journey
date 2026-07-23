from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Compute Both Hand Angles Directly
# Why: Each hand moves at a constant rate per minute — compute both angles from 12 o'clock and take the difference.
# Time: O(1)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = minutes * 6
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360 - diff)


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(1)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = minutes * 6
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360 - diff)

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
