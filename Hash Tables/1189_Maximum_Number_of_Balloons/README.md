# 1189 — Maximum Number of Balloons

## Problem
Given a string of lowercase letters, return the maximum number of times the word 'balloon' can be formed using its characters.

**Difficulty:** Easy | **Topic:** Hash Tables
**[View on LeetCode](https://leetcode.com/problems/maximum-number-of-balloons/)**

**Examples:**
```text
Input: text = "nlaebolko"
Output: 1

Input: text = "loonbalxballpoon"
Output: 2
```

---

## My Approaches
### Attempt 1 — Frequency Count, Then Divide by Needed Count ✅ Final Accepted Solution
**Why I used it:**
Count only the letters that appear in 'balloon', then the answer is limited by whichever letter is scarcest relative to how many copies each 'balloon' needs.

```python
def maxNumberOfBalloons(self, text: str) -> int:
    freq = {}
    for ch in text:
        if ch in "balloon":
            freq[ch] = freq.get(ch, 0) + 1
    return min(freq.get("b", 0), freq.get("a", 0),
               freq.get("l", 0) // 2, freq.get("o", 0) // 2,
               freq.get("n", 0))
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
'balloon' needs 1 b, 1 a, 2 l's, 2 o's, and 1 n. Count the letters available in text, then the number of times the word can be formed is limited by the letter (after dividing by how many copies it needs) that runs out first.

```python
def maxNumberOfBalloons(self, text: str) -> int:
    from collections import Counter
    count = Counter(text)
    return min(count['b'], count['a'], count['l'] // 2,
               count['o'] // 2, count['n'])
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Frequency Count, Then Divide by Needed Count) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
Whenever a target word needs multiple copies of a letter, divide that letter's available count by how many copies are needed before taking the min across all letters.

---

## Reference
- LeetCode #1189 — Maximum Number of Balloons
