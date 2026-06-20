# ─────────────────────────────────────────────────
# APPROACH 1: Math Formula (Recommended)
# Time: O(1) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = 6 * minutes                   # 360/60 = 6 degrees per minute
        hour_angle = 30 * (hour % 12) + 0.5 * minutes  # 360/12 = 30 per hour + 0.5 per minute
        diff = abs(hour_angle - minute_angle)
        return min(diff, 360 - diff)
