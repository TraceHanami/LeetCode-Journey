# 392 — Is Subsequence

## Problem

Determine whether string `s` is a subsequence of string `t` (characters of `s` appear in `t` in the same relative order, not necessarily contiguously).

**Difficulty:** Easy | **Topic:** Two Pointers

**[View on LeetCode](https://leetcode.com/problems/is-subsequence/)**

**Examples:**

```text
Input: s = "abc", t = "ahbgdc"
Output: true

Input: s = "axc", t = "ahbgdc"
Output: false
```

---

## My Approach ✅

### Why I Used This Method

Two pointers walking through `s` and `t` at the same time is the natural way to check ordered containment: advance the `t` pointer always, and only advance the `s` pointer on a match.

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
```

### Complexity

* Time: O(n) where n = len(t)
* Space: O(1)

---

## Alternative Approaches

### Approach 2 — Python Iterator Trick

#### Idea

Build an iterator over `t` and check that every character of `s` can be pulled from it in order, using `all()` with `next()`.

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        it = iter(t)
        return all(ch in it for ch in s)
```

#### Complexity

* Time: O(n)
* Space: O(1)

---

## Optimal Approach 🚀

### Idea

The two-pointer scan is already the optimal approach for a single query. If this check needed to run many times against the same `t` (the classic LeetCode follow-up), the standard trick is to pre-process `t` into a map of `character -> sorted list of indices` and binary-search the next valid position for each character of `s`.

```python
import bisect
from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        positions = defaultdict(list)
        for idx, ch in enumerate(t):
            positions[ch].append(idx)

        prev = -1
        for ch in s:
            idxs = positions.get(ch)
            if not idxs:
                return False
            pos = bisect.bisect_right(idxs, prev)
            if pos == len(idxs):
                return False
            prev = idxs[pos]
        return True
```

### Complexity

* Time: O(len(t)) to preprocess + O(len(s) log len(t)) per query
* Space: O(len(t))

---

## Comparison

| Approach              | Time                              | Space     | Recommended |
| ---------------------- | ---------------------------------- | --------- | ----------- |
| My Approach            | O(len(t))                          | O(1)      | ✅           |
| Iterator Trick         | O(len(t))                          | O(1)      | Optional    |
| Optimal (many queries) | O(len(t)) preprocess + O(log n)/ch | O(len(t)) | 🚀          |

---

## Key Takeaway

For a single subsequence check, a simple two-pointer scan is already optimal; the binary-search-over-indices version only pays off when the same `t` is queried many times.

---

## Reference

* LeetCode #392 — Is Subsequence
