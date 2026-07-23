# 567 — Permutation in String

## Problem
Given two strings s1 and s2, return true if s2 contains a permutation of s1 as a substring.

**Difficulty:** Medium | **Topic:** Sliding Window
**[View on LeetCode](https://leetcode.com/problems/permutation-in-string/)**

**Examples:**
```text
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
```

---

## My Approaches
### Attempt 1 — Fixed-Size Sliding Window with Frequency Maps ✅ Final Accepted Solution
**Why I used it:**
A permutation of s1 is any substring with the same character frequency — slide a window of s1's length across s2 checking for a frequency match.

```python
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
```

**Complexity:**
- Time: O(n)
- Space: O(k) (bounded alphabet)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Same fixed-size sliding window idea as Find All Anagrams: a substring is a permutation of s1 exactly when its character frequency matches s1's. Slide the window one character at a time, updating counts incrementally instead of recomputing them.

```python
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
```

### Complexity
- Time: O(n)
- Space: O(k)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Fixed-Size Sliding Window with Frequency Maps) | O(n) | O(k) (bounded alphabet) | ✅ |
| Standard Approach 1 | O(n) | O(k) | ✅ |


---

## Key Takeaway
This is structurally identical to 'Find All Anagrams' — a permutation check is just an anagram frequency-match check in a fixed-size sliding window.

---

## Reference
- LeetCode #567 — Permutation in String
