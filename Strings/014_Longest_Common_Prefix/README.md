# 14 — Longest Common Prefix

## Problem

Compare characters column by column across all strings.

**Difficulty:** Easy | **Topic:** Strings

**[View on LeetCode](https://leetcode.com/problems/longest-common-prefix/)**

**Examples:**
```
strs = ["flower","flow","flight"] -> "fl"
strs = ["dog","racecar","car"] -> ""
```
---

## Approach 1 — Vertical scanning ✅

**Idea:** Fix first string as reference. For each character position, check all strings match.

```python
class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i, char in enumerate(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]
        return strs[0]
```

**Complexity:**
- Time: O(n*m)
- Space: O(1)

---

## Approach 2 — Sort and compare ends

**Idea:** Sort array. LCP of sorted array = LCP of first and last strings only.

```python
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        prefix = ""
        for a, b in zip(strs[0], strs[-1]):
            if a == b:
                prefix += a
            else:
                break
        return prefix
```

**Complexity:**
- Time: O(n log n)
- Space: O(1)

---

## Approach 3 — Divide and conquer

**Idea:** Split array in half, find LCP of each half, merge.

```python
class Solution3:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def lcp(s1, s2):
            i = 0
            while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
                i += 1
            return s1[:i]

        def helper(arr, lo, hi):
            if lo == hi:
                return arr[lo]
            mid = (lo + hi) // 2
            left = helper(arr, lo, mid)
            right = helper(arr, mid + 1, hi)
            return lcp(left, right)

        return helper(strs, 0, len(strs) - 1) if strs else ""
```

**Complexity:**
- Time: O(n*m)
- Space: O(m log n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Vertical scanning | O(n*m) | O(1) | ✅ Yes |
| 2 — Sort and compare ends | O(n log n) | O(1) | No |
| 3 — Divide and conquer | O(n*m) | O(m log n) | No |

---

## Reference

[LeetCode #14 — Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
