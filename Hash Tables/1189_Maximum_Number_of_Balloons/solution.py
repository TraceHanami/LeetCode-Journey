from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Frequency Count, Then Divide by Needed Count
# Why: Count only the letters that appear in 'balloon', then the answer is limited by whichever letter is scarcest relative to how many copies each 'balloon' needs.
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {}
        for ch in text:
            if ch in "balloon":
                freq[ch] = freq.get(ch, 0) + 1
        return min(freq.get("b", 0), freq.get("a", 0),
                   freq.get("l", 0) // 2, freq.get("o", 0) // 2,
                   freq.get("n", 0))


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(1)
# ─────────────────────────────────────────────────
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        count = Counter(text)
        return min(count['b'], count['a'], count['l'] // 2,
                   count['o'] // 2, count['n'])

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
