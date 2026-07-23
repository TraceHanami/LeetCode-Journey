from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Sliding Window Counting Valid Left Boundaries
# Why: Once the window from left to right contains all 3 characters, every further left boundary from 0 up to left also forms a valid substring when extended to right — so add `left` to the count each step.
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        freq = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        for right in range(len(s)):
            freq[s[right]] += 1
            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                freq[s[left]] -= 1
                left += 1
            count += left
        return count


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = {'a': 0, 'b': 0, 'c': 0}
        left = total = 0
        for right, ch in enumerate(s):
            freq[ch] += 1
            while all(freq[c] > 0 for c in 'abc'):
                freq[s[left]] -= 1
                left += 1
            total += left
        return total

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
