# 1189 — Maximum Number of Balloons

## Problem

Given a string `text`, return the maximum number of times the word `"balloon"` can be formed using the characters from `text`. Each character may be used only once.

**Difficulty:** Easy | **Topic:** Hash Tables / Strings

**[View on LeetCode](https://leetcode.com/problems/maximum-number-of-balloons/)**

**Examples:**
```
text = "nlaebolko"      →  1
text = "loonbalxballpoon"  →  2
text = "leetcode"       →  0
```

**Key observation:** `"balloon"` = b×1, a×1, l×2, o×2, n×1. The letters `l` and `o` each appear **twice** per word.

---

## Approach 1 — Counter with Min Frequency ✅

**Idea:** Count all characters. The answer is the minimum of how many complete sets of each required character we have. Divide `l` and `o` counts by 2 since each word needs 2 of them.

```python
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
```

**Complexity:**
- Time: O(n)
- Space: O(1) — Counter has at most 26 keys

---

## Approach 2 — Manual Count with Needed Map

**Idea:** Define a `needed` dict mapping each character to how many times it appears in `"balloon"`. Count frequencies for only those characters, then divide each frequency by its requirement and return the minimum.

```python
class Solution2:
    def maxNumberOfBalloons(self, text: str) -> int:
        needed = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        freq = {}
        for c in text:
            if c in needed:
                freq[c] = freq.get(c, 0) + 1

        return min(freq.get(c, 0) // needed[c] for c in needed)
```

**Complexity:**
- Time: O(n)
- Space: O(1)

**Why it's useful:** More generalizable — swap `"balloon"` for any target word with no code changes beyond updating `needed`.

---

## Approach 3 — Binary Search on Answer

**Idea:** Binary search on the number of words `k` we can form. For a given `k`, check whether each character's frequency in `text` is at least `k × frequency_in_word`. A nice pattern for "how many times can I form X" problems.

```python
class Solution3:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter

        freq = Counter(text)
        word_freq = Counter("balloon")

        lo, hi = 0, len(text)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if all(freq[c] >= word_freq[c] * mid for c in word_freq):
                lo = mid
            else:
                hi = mid - 1

        return lo
```

**Complexity:**
- Time: O(n log n)
- Space: O(1)

**When to use:** Overkill here, but a powerful pattern when the feasibility check is expensive or the search space is large.

---

## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Counter Min | O(n) | O(1) | ✅ Yes |
| 2 — Needed Map | O(n) | O(1) | No |
| 3 — Binary Search | O(n log n) | O(1) | No |

---

## Reference

[LeetCode #1189 — Maximum Number of Balloons](https://leetcode.com/problems/maximum-number-of-balloons/)
