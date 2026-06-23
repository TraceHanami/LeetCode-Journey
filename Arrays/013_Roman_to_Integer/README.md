# 13 — Roman to Integer

## Problem

Given a roman numeral string `s`, convert it to an integer.

Roman numerals use 7 symbols: `I(1) V(5) X(10) L(50) C(100) D(500) M(1000)`.
Subtractive notation applies in 6 cases: `IV(4) IX(9) XL(40) XC(90) CD(400) CM(900)`.

**Constraints:** `1 <= s.length <= 15` · `s` contains only valid Roman numeral characters

**Difficulty:** Easy | **Topic:** Hashtable / String

**[View on LeetCode](https://leetcode.com/problems/roman-to-integer)**

**Examples:**
```
"III"   →  3
"IV"    →  4
"IX"    →  9
"LVIII" →  58   (L=50, V=5, III=3)
"MCMXCIV" → 1994
```

---

## Approach 1 — Brute Force: Replace Subtractive Pairs

**Idea:** Before summing, replace all 6 subtractive pairs with their additive equivalents.
After replacement, every character is simply added — no conditional logic needed.

```python
class Solution1:
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", "IIII")
        s = s.replace("IX", "VIIII")
        s = s.replace("XL", "XXXX")
        s = s.replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC")
        s = s.replace("CM", "DCCCC")

        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        return sum(roman[c] for c in s)
```

**Complexity:**
- Time: O(1) — exactly 6 replacements on a string bounded by length 15
- Space: O(n) — new string created per replacement

**When to mention it:** Great as a first step in an interview to show you understand the problem before optimising.

---

## Approach 2 — Left-to-Right Comparison (Recommended)

**Idea:** Traverse left to right. If the current symbol's value is less than the next one, it's a subtractive pair — subtract it. Otherwise add it.

```python
class Solution2:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        return total
```

**Complexity:**
- Time: O(n) — single pass
- Space: O(1) — fixed-size lookup table

**When to use:** The cleanest and most intuitive solution. Best default answer in an interview.

---

## Approach 3 — Right-to-Left Iteration

**Idea:** Iterate from right to left, tracking the previously seen value. If current < previous, subtract; otherwise add. Avoids the `i+1` boundary check entirely.

```python
class Solution3:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = roman[s[-1]]
        prev  = roman[s[-1]]

        for i in range(len(s) - 2, -1, -1):
            curr = roman[s[i]]
            if curr < prev:
                total -= curr
            else:
                total += curr
            prev = curr

        return total
```

**Complexity:**
- Time: O(n)
- Space: O(1)

**When to use:** A good alternative to show you can think about traversal direction as a design choice.

---

## Approach 4 — Pairwise Lookup

**Idea:** Build a combined map that includes all 6 subtractive pairs alongside the 7 base symbols. At each position, check the two-character window first — if it's a known pair, consume both characters at once; otherwise consume one.

```python
class Solution4:
    def romanToInt(self, s: str) -> int:
        combined = {
            'I': 1,   'V': 5,   'X': 10,  'L': 50,
            'C': 100, 'D': 500, 'M': 1000,
            'IV': 4,  'IX': 9,  'XL': 40,
            'XC': 90, 'CD': 400,'CM': 900,
        }
        total = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in combined:
                total += combined[s[i:i+2]]
                i += 2
            else:
                total += combined[s[i]]
                i += 1

        return total
```

**Complexity:**
- Time: O(n)
- Space: O(1) — combined map is fixed size (13 keys)

**When to use:** Most explicit and readable. Good if you want to make the subtractive pairs visually obvious in the code.

---

## Comparison

| Approach | Time | Space | Best For |
|---|---|---|---|
| 1 — Replace Pairs | O(1) | O(n) | Explaining the problem simply |
| 2 — Left-to-Right | O(n) | O(1) | Default interview answer |
| 3 — Right-to-Left | O(n) | O(1) | Showing directional thinking |
| 4 — Pairwise Lookup | O(n) | O(1) | Maximum readability |

---

## Reference

[LeetCode #13 — Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
