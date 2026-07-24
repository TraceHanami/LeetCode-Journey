# 917 — Reverse Only Letters

## Problem

Reverse only the letters in a string, leaving all non-letter characters (digits, symbols, spaces) exactly where they are.

**Difficulty:** Easy | **Topic:** Two Pointers

**[View on LeetCode](https://leetcode.com/problems/reverse-only-letters/)**

**Examples:**

```text
Input: s = "ab-cd"
Output: "dc-ba"

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
```

---

## My Approach ✅

### Why I Used This Method

Two pointers closing in from both ends only swap when both sides point at letters, and otherwise skip whichever side is a non-letter — that naturally leaves non-letters in place while reversing everything else.

```python
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        while(i<j):
            if s[i].isalpha() and s[j].isalpha():
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif not s[i].isalpha():
                i+=1
            else:
                j-=1
        return "".join(s)
```

### Complexity

* Time: O(n)
* Space: O(n) (converting the string to a list to allow in-place swaps)

---

## Alternative Approaches

### Approach 2 — Stack of Letters

#### Idea

Collect all letters into a stack, then rebuild the string, popping a letter off the stack whenever the original position held a letter and leaving everything else untouched.

```python
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [ch for ch in s if ch.isalpha()]
        result = []
        for ch in s:
            if ch.isalpha():
                result.append(letters.pop())
            else:
                result.append(ch)
        return "".join(result)
```

#### Complexity

* Time: O(n)
* Space: O(n)

---

## Optimal Approach 🚀

### Idea

The two-pointer in-place swap (my approach) is already the optimal technique for this problem — linear time with only the unavoidable O(n) space to hold a mutable copy of the string, since Python strings are immutable.

```python
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = list(s)
        i, j = 0, len(chars) - 1
        while i < j:
            if not chars[i].isalpha():
                i += 1
            elif not chars[j].isalpha():
                j -= 1
            else:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
        return "".join(chars)
```

### Complexity

* Time: O(n)
* Space: O(n)

---

## Comparison

| Approach          | Time | Space | Recommended |
| ------------------ | ---- | ----- | ----------- |
| My Approach         | O(n) | O(n)  | ✅           |
| Stack of Letters    | O(n) | O(n)  | Optional    |
| Optimal             | O(n) | O(n)  | 🚀          |

---

## Key Takeaway

Two pointers that skip whichever side fails a condition (here, "is not a letter") is a reusable pattern for "reverse/rearrange only the elements matching some property, leave the rest untouched."

---

## Reference

* LeetCode #917 — Reverse Only Letters
