# 3014 — Minimum Number of Pushes to Type Word I

## Problem
You are given a string `word` containing distinct lowercase English letters. Telephone keypads map 8 keys (keys 2 through 9) to letters. You can map each letter to any key, and each key can map to any number of distinct letters. Pressing a key once types its first mapped letter, pressing it twice types its second mapped letter, and so on.

Return the minimum number of key pushes needed to type `word`.

**Difficulty:** Easy | **Topic:** Greedy
**[View on LeetCode](https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/)**

**Examples:**
```text
Input: word = "abcde"
Output: 5
Explanation: The 5 distinct characters can each be mapped as the 1st letter on 5 different keys (1 push each). Total = 5 * 1 = 5.

Input: word = "xycdefghij"
Output: 12
Explanation: The first 8 characters are mapped to the 1st position across all 8 keys (8 * 1 = 8 pushes). The remaining 2 characters are mapped to the 2nd position on 2 keys (2 * 2 = 4 pushes). Total = 8 + 4 = 12.
```

---

## My Approaches
### Attempt 1 — Greedy Push-Tier Allocation ✅ Final Accepted Solution
**Why I used it:**
Since all letters in `word` are distinct, each letter appears exactly once. To minimize keystrokes, greedily fill the cheapest push positions across the 8 available keypad buttons (keys 2–9) before moving to higher push tiers.

```python
class Solution:
    def minimumPushes(self, word: str) -> int:
        cost = {1: 8,2: 8,3: 8,4:2}
        n = len(word)
        ans = 0
        for pushes, cnt in cost.items():
            take = min(n, cnt)
            ans += take * pushes
            n -= take
            if n == 0:
                break
        return ans
```

**Algorithm Steps:**
1. Define a tier map `cost = {1: 8, 2: 8, 3: 8, 4: 2}`:
   - Tier 1: 8 keys available at 1 push each.
   - Tier 2: 8 keys available at 2 pushes each.
   - Tier 3: 8 keys available at 3 pushes each.
   - Tier 4: The remaining 2 alphabet letters on 2 keys at 4 pushes each (total 26 lowercase letters).
2. Get the number of distinct characters `n = len(word)`.
3. Iterate through each tier `(pushes, cnt)`:
   - Determine how many letters can be placed in this tier: `take = min(n, cnt)`.
   - Add the keystrokes for these letters: `ans += take * pushes`.
   - Decrement the remaining unassigned letters: `n -= take`.
   - If `n == 0`, all characters have been assigned; break early.
4. Return the accumulated total pushes `ans`.

**Complexity:**
- Time: O(len(word)) or O(1) — `len(word)` takes O(len(word)) time, while the loop runs at most 4 times (since the English alphabet has 26 letters distributed over 4 tiers).
- Space: O(1) auxiliary space — only the small 4-element dictionary and scalar variables are allocated.

---

---

## Standard Approach
### Standard Approach 1 — Direct Mathematical Formula ✅
### Idea
Since characters are assigned in blocks of 8 keys:
- The first full block of 8 costs $8 \times 1 = 8$.
- The second full block of 8 costs $8 \times 2 = 16$.
- The third full block of 8 costs $8 \times 3 = 24$.
We can compute this via arithmetic progression for the full blocks plus the remainder characters multiplied by their tier.

```python
class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        full_blocks, rem = divmod(n, 8)
        # Sum of 8 * i for i from 1 to full_blocks: 8 * (full_blocks * (full_blocks + 1) // 2)
        total = 4 * full_blocks * (full_blocks + 1) + rem * (full_blocks + 1)
        return total
```

### Complexity
- Time: O(len(word)) — to get the length of the string.
- Space: O(1) auxiliary space.

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Approach (Greedy Tier Allocation) | O(len(word)) | O(1) | ✅ |
| Standard Approach (Math Formula) | O(len(word)) | O(1) | ✅ |

---

## Key Takeaway
When every element has equal frequency, minimizing cost is purely a greedy assignment: fill all slots of cost $k$ before utilizing any slots of cost $k + 1$.

---

## Reference
- LeetCode #3014 — Minimum Number of Pushes to Type Word I
