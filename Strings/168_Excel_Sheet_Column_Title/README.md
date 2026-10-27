# 168 — Excel Sheet Column Title

## Problem
Given an integer `columnNumber`, return its corresponding Excel column title.

Excel columns use letters instead of numbers:

- `A` → `1`, `B` → `2`, ..., `Z` → `26`
- `AA` → `27`, `AB` → `28`, ..., `ZY` → `701`

**Difficulty:** Easy | **Topic:** Math, String

**[View on LeetCode](https://leetcode.com/problems/excel-sheet-column-title/)**

**Examples:**
```text
Input: columnNumber = 1
Output: "A"

Input: columnNumber = 28
Output: "AB"

Input: columnNumber = 701
Output: "ZY"
```

---

## My Approaches

### Attempt 1 — Iterative Base-26 Conversion ✅ Final Accepted Solution

**Why I used it:**

Excel column numbering resembles a base-26 number system, but it has no zero-valued letter. Each letter represents a value from `1` to `26`. Subtracting one before applying modulo converts the numbering to a zero-based range from `0` to `25`.

Using modulo, integer division, and character conversion, I construct the title from right to left.

```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""

        while columnNumber > 0:
            columnNumber -= 1
            r = columnNumber % 26
            s = chr(r + ord('A')) + s
            columnNumber //= 26

        return s
```

### Algorithm Steps

1. Initialize an empty string `s` to store the resulting column title.
2. Continue while `columnNumber > 0`.
3. Subtract `1` from `columnNumber` to handle Excel's 1-based numbering.
4. Calculate `r = columnNumber % 26` to determine the last letter's zero-based index.
5. Convert the index to a character using `chr(r + ord('A'))` and prepend it to `s`.
6. Divide `columnNumber` by `26` using integer division to process the remaining digits.
7. Return `s` when the number becomes zero.

### Example Walkthrough

For `columnNumber = 701`:

| Iteration | Adjusted Number | Remainder | Letter | Result |
|---|---:|---:|---|---|
| 1 | 700 | 24 | Y | Y |
| 2 | 25 | 25 | Z | ZY |

The final answer is `"ZY"`.

### Complexity

- **Time:** `O(log₂₆ n)` — Each iteration divides the number by `26`.
- **Space:** `O(log₂₆ n)` — The resulting string contains one character per base-26 digit.

---

## Standard Approach

### Standard Approach 1 — Base-26 Conversion with a Character List ✅

### Idea

The standard approach uses the same conversion logic but stores the generated letters in a list. Since the least significant letter is discovered first, the list is reversed before joining the characters.

This avoids repeatedly prepending characters to an immutable string.

```python
class SolutionStandard:
    def convertToTitle(self, columnNumber: int) -> str:
        a = []

        while columnNumber > 0:
            columnNumber -= 1
            r = columnNumber % 26
            a.append(chr(r + ord('A')))
            columnNumber //= 26

        return "".join(a[::-1])
```

### Algorithm Steps

1. Initialize an empty list `a` to store individual letters.
2. Subtract `1` from `columnNumber` during each iteration.
3. Calculate the remainder using `% 26`.
4. Convert the remainder to its corresponding uppercase letter and append it to `a`.
5. Divide `columnNumber` by `26` using integer division.
6. Reverse the list because letters are generated from right to left.
7. Join the reversed list into a string and return it.

### Complexity

- **Time:** `O(log₂₆ n)` — Each iteration processes one base-26 digit, followed by reversing and joining the letters.
- **Space:** `O(log₂₆ n)` — The list stores the generated letters.

---

## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| My Approach (String Prepending) | `O(log₂₆ n)` | `O(log₂₆ n)` | ✅ |
| Standard Approach (Character List) | `O(log₂₆ n)` | `O(log₂₆ n)` | ✅ |

Both approaches have the same asymptotic complexity. The character-list approach avoids repeated string construction and is generally preferable for longer titles. Under the given constraint, both are efficient.

---

## Key Takeaway

Excel column titles use a 1-based alphabetic numbering system rather than a conventional zero-based positional system.

The critical operation is:

```python
columnNumber -= 1
```

It ensures that multiples of `26` map correctly. For example, `26` becomes `Z`, `27` becomes `AA`, and `52` becomes `AZ`.

**Core idea:** Subtract one, extract a base-26 digit using modulo, convert it to a letter, and repeat using integer division.

---

## Reference

- LeetCode #168 — Excel Sheet Column Title
