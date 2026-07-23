# 205 — Isomorphic Strings

## Problem
Given two strings s and t, return true if the characters in s can be replaced to get t, with each character mapping to exactly one other character (a consistent, one-to-one mapping in both directions).

**Difficulty:** Easy | **Topic:** Hash Tables
**[View on LeetCode](https://leetcode.com/problems/isomorphic-strings/)**

**Examples:**
```text
Input: s = "egg", t = "add"
Output: true

Input: s = "foo", t = "bar"
Output: false
```

---

## My Approaches
### Attempt 1 — Two-Way Mapping Dictionaries ✅ Final Accepted Solution
**Why I used it:**
A one-to-one mapping must be consistent in both directions, so track mappings from s->t and t->s simultaneously.

```python
def isIsomorphic(self, s: str, t: str) -> bool:
    m, z = {}, {}
    for i, j in zip(s, t):
        if i in m and m[i] != j:
            return False
        if j in z and z[j] != i:
            return False
        m[i] = j
        z[j] = i
    return True
```

**Complexity:**
- Time: O(n)
- Space: O(1) (bounded alphabet)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Maintain two hash maps — one for the s-to-t character mapping, one for t-to-s — and verify both stay consistent while scanning. This catches cases where two different source characters would need to map to the same target character, which a single one-directional map would miss.

```python
def isIsomorphic(self, s: str, t: str) -> bool:
    s_to_t, t_to_s = {}, {}
    for a, b in zip(s, t):
        if a in s_to_t and s_to_t[a] != b:
            return False
        if b in t_to_s and t_to_s[b] != a:
            return False
        s_to_t[a] = b
        t_to_s[b] = a
    return True
```

### Complexity
- Time: O(n)
- Space: O(1) (bounded alphabet)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Two-Way Mapping Dictionaries) | O(n) | O(1) (bounded alphabet) | ✅ |
| Standard Approach 1 | O(n) | O(1) (bounded alphabet) | ✅ |


---

## Key Takeaway
A mapping that must be one-to-one (a bijection) needs to be validated in both directions — a single forward map isn't enough.

---

## Reference
- LeetCode #205 — Isomorphic Strings
