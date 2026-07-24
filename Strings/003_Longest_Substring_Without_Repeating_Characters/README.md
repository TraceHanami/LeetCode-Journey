# 3 — Longest Substring Without Repeating Characters

## Problem

Given a string, find the length of the longest substring that does not contain any repeating characters.

**Difficulty:** Medium | **Topic:** Sliding Window / Hash Set

**[View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)**

**Examples:**

```text
Input: s = "abcabcbb"
Output: 3

Input: s = "bbbbb"
Output: 1

Input: s = "pwwkew"
Output: 3
```

---

## My Approach ✅

### Why I Used This Method

A sliding window with a set of currently-seen characters lets me expand the right edge freely and only shrink the left edge when a duplicate shows up, so every character is looked at a bounded number of times.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=set()
        j=0
        r=0
        for i in range(len(s)):
            while s[i] in a:
                a.remove(s[j])
                j+=1
            a.add(s[i])
            r=max(r,i-j+1)
        return r
```

### Complexity

* Time: O(n)
* Space: O(min(n, m)) where m is the size of the character set

---

## Alternative Approaches

### Approach 2 — Brute Force

#### Idea

Check every substring for uniqueness and keep the longest one found. Simple to reason about but far too slow for large inputs.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        best = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                best = max(best, j - i + 1)
        return best
```

#### Complexity

* Time: O(n^2)
* Space: O(min(n, m))

---

## Optimal Approach 🚀

### Idea

A sliding window that uses a hash map of `character -> last seen index` can jump the left pointer directly to just past the previous occurrence, instead of removing one character at a time. This keeps the same asymptotic complexity as my approach but avoids the inner `while` loop doing repeated single-step removals.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            best = max(best, right - left + 1)
        return best
```

### Complexity

* Time: O(n)
* Space: O(min(n, m))

---

## Comparison

| Approach    | Time   | Space           | Recommended |
| ----------- | ------ | --------------- | ----------- |
| My Approach | O(n)   | O(min(n, m))    | ✅           |
| Brute Force | O(n^2) | O(min(n, m))    | Optional    |
| Optimal     | O(n)   | O(min(n, m))    | 🚀          |

---

## Key Takeaway

A sliding window turns "find the longest substring with property X" into a single pass where the left boundary only ever moves forward, giving linear time instead of checking every substring.

---

## Reference

* LeetCode #3 — Longest Substring Without Repeating Characters
