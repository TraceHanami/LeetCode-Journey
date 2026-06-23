# 205 — Isomorphic Strings

## Problem

Map each character in s to corresponding character in t; check consistency both ways.

**Difficulty:** Easy | **Topic:** Hash Tables

**[View on LeetCode](https://leetcode.com/problems/isomorphic-strings/)**

**Examples:**
```
s = "egg", t = "add" -> true
s = "f11", t = "b23" -> false
s = "paper", t = "title" -> true 
```
---

## Approach 1 — Two hash maps ✅

**Idea:** Map s→t and t→s. Reject if any inconsistency found.

```python
class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t, t_to_s = {}, {}
        for cs, ct in zip(s, t):
            if s_to_t.get(cs, ct) != ct or t_to_s.get(ct, cs) != cs:
                return False
            s_to_t[cs] = ct
            t_to_s[ct] = cs
        return True
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Encode pattern

**Idea:** Replace each char with its first-seen index. If encoded s == encoded t, isomorphic.

```python
class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def encode(string):
            mapping = {}
            return [mapping.setdefault(c, len(mapping)) for c in string]
        return encode(s) == encode(t)
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Two hash maps | O(n) | O(1) | ✅ Yes |
| 2 — Encode pattern | O(n) | O(n) | No |

---

## Reference

[LeetCode #205 — Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)
