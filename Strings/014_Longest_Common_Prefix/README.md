# 014 — Longest Common Prefix

## Problem
Given an array of strings, find the longest common prefix string among them. Return an empty string if there is none.

**Difficulty:** Easy | **Topic:** Strings
**[View on LeetCode](https://leetcode.com/problems/longest-common-prefix/)**

**Examples:**
```text
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

---

## My Approaches
### Attempt 1 — Character-by-Character Vertical Scan ✅ Final Accepted Solution
**Why I used it:**
Compare column by column against the first string — stop the moment any string diverges or runs out.

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""
    prefix = ""
    first = strs[0]
    for i in range(len(first)):
        for word in strs:
            if i >= len(word) or word[i] != first[i]:
                return prefix
        prefix += first[i]
    return prefix
```

**Complexity:**
- Time: O(S) where S = total characters
- Space: O(1) extra

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Scan character positions one at a time (using the first string as reference), checking every other string at that same position. Stop as soon as a mismatch or a string that's too short is found — this is optimal since every character in the answer must be checked.

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""
    for i, ch in enumerate(strs[0]):
        for word in strs[1:]:
            if i >= len(word) or word[i] != ch:
                return strs[0][:i]
    return strs[0]
```

### Complexity
- Time: O(S)
- Space: O(1) extra

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Character-by-Character Vertical Scan) | O(S) where S = total characters | O(1) extra | ✅ |
| Standard Approach 1 | O(S) | O(1) extra | ✅ |


---

## Key Takeaway
A vertical (column-by-column) scan stops as early as possible on the first mismatch, avoiding wasted comparisons beyond the actual common prefix length.

---

## Reference
- LeetCode #14 — Longest Common Prefix
