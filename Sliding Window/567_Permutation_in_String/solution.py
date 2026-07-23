from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Fixed-Size Sliding Window with Frequency Maps
# Why: A permutation of s1 is any substring with the same character frequency — slide a window of s1's length across s2 checking for a frequency match.
# Time: O(n)
# Space: O(k) (bounded alphabet)
# ─────────────────────────────────────────────────
class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = {}
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1
        window = {}
        k = len(s1)
        for i in range(k):
            window[s2[i]] = window.get(s2[i], 0) + 1
        if need == window:
            return True
        for i in range(k, len(s2)):
            left, right = s2[i - k], s2[i]
            window[right] = window.get(right, 0) + 1
            if window[left] == 1:
                del window[left]
            else:
                window[left] -= 1
            if need == window:
                return True
        return False


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(k)
# ─────────────────────────────────────────────────
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if len(s1) > len(s2):
            return False
        need, window = Counter(s1), Counter(s2[:len(s1)])
        if need == window:
            return True
        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1
            left = s2[i - len(s1)]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            if window == need:
                return True
        return False

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
