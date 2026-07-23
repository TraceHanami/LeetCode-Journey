# 344 — Reverse String

## Problem
Reverse a string in place, given as an array of characters.

**Difficulty:** Easy | **Topic:** Strings
**[View on LeetCode](https://leetcode.com/problems/reverse-string/)**

**Examples:**
```text
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

---

## My Approaches
### Attempt 1 — Built-in list.reverse() ✅ Final Accepted Solution
**Why I used it:**
Python's list already has an in-place reverse method that does exactly what's required.

```python
def reverseString(self, s: List[str]) -> None:
    s.reverse()
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Two pointers starting at each end, swapping inward until they meet — this is what list.reverse() does internally, and is the standard technique to implement in-place reversal manually.

```python
def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Built-in list.reverse()) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
This is the foundational two-pointer swap-from-both-ends pattern that shows up throughout array/string problems.

---

## Reference
- LeetCode #344 — Reverse String
