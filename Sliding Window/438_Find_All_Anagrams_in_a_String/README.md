# 438 — Find All Anagrams in a String

## Problem
Given strings s and p, return the starting indices of all anagrams of p found within s.

**Difficulty:** Medium | **Topic:** Sliding Window
**[View on LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/)**

**Examples:**
```text
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
```

---

## My Approaches
### Attempt 1 — Fixed-Size Sliding Window with Frequency Maps ✅ Final Accepted Solution
**Why I used it:**
Maintain a frequency map of the current window and compare it to p's frequency map, sliding one character at a time instead of re-counting from scratch.

```python
def findAnagrams(self, s: str, p: str) -> List[int]:
    result = []
    if len(p) > len(s):
        return result
    need = {}
    for ch in p:
        need[ch] = need.get(ch, 0) + 1
    window = {}
    for i in range(len(p)):
        window[s[i]] = window.get(s[i], 0) + 1
    if need == window:
        result.append(0)
    for i in range(len(p), len(s)):
        left_ch, right_ch = s[i - len(p)], s[i]
        window[left_ch] -= 1
        if window[left_ch] == 0:
            del window[left_ch]
        window[right_ch] = window.get(right_ch, 0) + 1
        if need == window:
            result.append(i - len(p) + 1)
    return result
```

**Complexity:**
- Time: O(n)
- Space: O(k) (bounded alphabet)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Maintain a fixed-size window of length len(p) sliding across s. Track character counts incrementally — remove the character leaving the window and add the one entering — and compare against p's target frequency map. Comparing full dictionaries each step is O(26) at worst, effectively O(1).

```python
def findAnagrams(self, s: str, p: str) -> List[int]:
    from collections import Counter
    if len(p) > len(s):
        return []
    need, window = Counter(p), Counter(s[:len(p)])
    result = [0] if need == window else []
    for i in range(len(p), len(s)):
        window[s[i]] += 1
        window[s[i - len(p)]] -= 1
        if window[s[i - len(p)]] == 0:
            del window[s[i - len(p)]]
        if window == need:
            result.append(i - len(p) + 1)
    return result
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
A fixed-size sliding window that incrementally updates counts (rather than recomputing from scratch each shift) turns an O(n*k) brute force into O(n).

---

## Reference
- LeetCode #438 — Find All Anagrams in a String
