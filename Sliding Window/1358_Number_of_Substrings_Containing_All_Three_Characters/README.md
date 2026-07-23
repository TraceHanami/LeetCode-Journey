# 1358 — Number of Substrings Containing All Three Characters

## Problem
Given a string containing only 'a', 'b', and 'c', return the number of substrings containing at least one of each character.

**Difficulty:** Medium | **Topic:** Sliding Window
**[View on LeetCode](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)**

**Examples:**
```text
Input: s = "abcabc"
Output: 10
```

---

## My Approaches
### Attempt 1 — Sliding Window Counting Valid Left Boundaries ✅ Final Accepted Solution
**Why I used it:**
Once the window from left to right contains all 3 characters, every further left boundary from 0 up to left also forms a valid substring when extended to right — so add `left` to the count each step.

```python
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
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
For each right endpoint, shrink the window from the left as much as possible while it still contains all three characters. Once shrunk to the minimal valid window, every substring starting anywhere from index 0 up to (but not including) the final left position and ending at right is also valid — so add `left` directly to the running count instead of counting each one individually.

```python
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
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Sliding Window Counting Valid Left Boundaries) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
When counting valid substrings (not just finding the longest), shrinking the window to its minimal valid size and adding `left` to the count captures all valid left boundaries at once.

---

## Reference
- LeetCode #1358 — Number of Substrings Containing All Three Characters
