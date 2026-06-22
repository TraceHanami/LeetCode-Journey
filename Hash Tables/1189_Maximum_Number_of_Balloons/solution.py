# ─────────────────────────────────────────────────
# APPROACH 1: Counter with Min Frequency (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
# "balloon" needs: b×1, a×1, l×2, o×2, n×1
# Divide l and o counts by 2 since each word needs 2 of them.
class Solution1:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        freq = Counter(text)
        return min(
            freq['b'],
            freq['a'],
            freq['l'] // 2,
            freq['o'] // 2,
            freq['n'],
        )


# ─────────────────────────────────────────────────
# APPROACH 2: Manual Count Array
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution2:
    def maxNumberOfBalloons(self, text: str) -> int:
        needed = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        freq = {}
        for c in text:
            if c in needed:
                freq[c] = freq.get(c, 0) + 1

        return min(freq.get(c, 0) // needed[c] for c in needed)


# ─────────────────────────────────────────────────
# APPROACH 3: Generic "can form k words" check (Binary Search)
# Time: O(n log n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution3:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter

        freq = Counter(text)
        word_freq = Counter("balloon")

        lo, hi = 0, len(text)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            # Can we form `mid` copies of "balloon"?
            if all(freq[c] >= word_freq[c] * mid for c in word_freq):
                lo = mid
            else:
                hi = mid - 1

        return lo
