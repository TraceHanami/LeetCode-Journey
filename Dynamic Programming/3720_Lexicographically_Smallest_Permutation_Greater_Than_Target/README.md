# 3720 — Lexicographically Smallest Permutation Greater Than Target

## Problem
You are given two strings `s` and `target`, both of length `n`, consisting of lowercase English letters. Return the lexicographically smallest permutation of `s` that is strictly greater than `target`. If no such permutation exists, return an empty string `""`.

**Difficulty:** Medium | **Topic:** Dynamic Programming
**[View on LeetCode](https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/)**

**Examples:**
```text
Input: s = "abc", target = "acb"
Output: "bac"
Explanation: The permutations of "abc" in lexicographical order are: "abc", "acb", "bac", "bca", "cab", "cba". The smallest permutation strictly greater than "acb" is "bac".

Input: s = "ab", target = "ba"
Output: ""
Explanation: The only permutations of "ab" are "ab" and "ba". Neither is strictly greater than "ba", so return "".
```

---

## My Approaches
### Attempt 1 — Memoized DFS with Frequency State Tuple ✅ Final Accepted Solution
**Why I used it:**
Builds the resulting string index by index from left to right using available characters from `s`. By trying available distinct characters in sorted order, the first valid permutation found is guaranteed to be the lexicographically smallest.

```python
from collections import Counter
from functools import lru_cache

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)
        chars = sorted(cnt.keys())
        n = len(s)

        @lru_cache(None)
        def dfs(i, greater, state):
            if i == n:
                return "" if greater else None

            freq = list(state)

            for idx, ch in enumerate(chars):
                if freq[idx] == 0:
                    continue

                if not greater:
                    if ch < target[i]:
                        continue
                    next_greater = ch > target[i]
                else:
                    next_greater = True

                freq[idx] -= 1

                suffix = dfs(i + 1, next_greater, tuple(freq))

                if suffix is not None:
                    return ch + suffix

                freq[idx] += 1

            return None

        initial_state = tuple(cnt[ch] for ch in chars)

        ans = dfs(0, False, initial_state)
        return "" if ans is None else ans
```

**Algorithm Steps:**
1. Count the occurrences of each character in `s` using `Counter(s)`.
2. Extract and sort the unique characters `chars = sorted(cnt.keys())`. This ensures we always try smaller characters first.
3. Define the memoized search function `dfs(i, greater, state)`:
   - `i`: Current position in the output string being constructed (`0` to `n`).
   - `greater`: A boolean flag indicating whether the prefix constructed so far is already strictly greater than `target[:i]`.
   - `state`: An immutable tuple representing the remaining frequency counts for each character in `chars`.
4. **Base Case:** When `i == n`, all characters have been placed. Return `""` if `greater` is `True` (strictly greater overall), or `None` if it only tied `target`.
5. **Branching:**
   - Iterate over each candidate character `ch` in sorted order `chars`.
   - If `freq[idx] == 0`, skip it (none remaining).
   - If `greater` is `False`: we cannot choose any character `ch < target[i]`. If `ch == target[i]`, `next_greater` remains `False`. If `ch > target[i]`, `next_greater` becomes `True`.
   - If `greater` is already `True`: any available character can be chosen, and `next_greater` remains `True`.
   - Decrement `freq[idx]`, recurse for position `i + 1`, and if a valid `suffix` string is returned, immediately return `ch + suffix`.
   - Backtrack by restoring `freq[idx] += 1`.
6. Start from `dfs(0, False, initial_state)`. Return the result string or `""` if `None`.

> [!WARNING]
> **State-Space Caveat:** The number of theoretical frequency states is bounded by $\prod_{ch} (\text{cnt}[ch] + 1)$. In the worst theoretical case with many distinct characters and long strings, the state space could grow large. However, in practice:
> 1. While `greater` is `False`, the choices are strictly pruned to `ch >= target[i]` (often just 1 or 2 options).
> 2. Once `greater` becomes `True`, the search immediately takes the smallest available character at every remaining index on the very first try without ever needing to backtrack.
> Nonetheless, this algorithm cannot be claimed as universally O(n) without accounting for the memoized branching overhead on adversarial inputs.

**Complexity:**
- Time: State-space bounded by $O(n \cdot 2 \cdot \Sigma \cdot S)$, where $\Sigma \le 26$ is the number of distinct characters, and $S$ is the number of distinct reachable frequency tuples (heavily pruned by greedy termination once `greater` is set).
- Space: $O(n)$ recursion stack depth + $O(S)$ memoization cache entries in `lru_cache`.

---

---

## Standard Approach
### Standard Approach 1 — Greedy Pivot Match & Suffix Flush 🚀 Optimal
### Idea
The optimal linear-time strategy finds the longest common prefix between `target` and a valid permutation of `s`:
1. Find the deepest index `pivot` from left to right where we can deviate from `target` by picking an available character strictly greater than `target[pivot]` such that the remaining pool can complete the string.
2. Place the smallest character greater than `target[pivot]`.
3. Flush all remaining characters in the pool in ascending order.
This avoids memoization completely and runs in deterministic $O(26 \cdot n)$ time.

```python
from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)
        n = len(s)

        # Find maximum prefix we can match
        matched_prefix = []
        curr_cnt = Counter(cnt)

        # Check if identical prefix is possible up to index i
        prefix_len = 0
        while prefix_len < n and curr_cnt[target[prefix_len]] > 0:
            curr_cnt[target[prefix_len]] -= 1
            prefix_len += 1

        # Search backward from prefix_len down to 0 for a valid pivot
        for i in range(prefix_len, -1, -1):
            # Restore pool up to index i
            pool = Counter(cnt)
            for j in range(i):
                pool[target[j]] -= 1

            if i < n:
                # Find smallest character in pool strictly greater than target[i]
                candidates = sorted(ch for ch in pool if pool[ch] > 0 and ch > target[i])
                if candidates:
                    chosen = candidates[0]
                    pool[chosen] -= 1
                    # Flush remaining characters in ascending order
                    suffix = []
                    for ch in sorted(pool.keys()):
                        suffix.append(ch * pool[ch])
                    return target[:i] + chosen + "".join(suffix)

        return ""
```

### Complexity
- Time: O(26 · n) = O(n) — backward scan checks at most 26 candidate characters per index.
- Space: O(26) = O(1) auxiliary space for character counts.

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Approach (Memoized DFS with State Tuple) | State-dependent / Pruned Search | O(S) cache + O(n) stack | ✅ (Preserved Original) |
| Standard Approach (Greedy Pivot Match & Flush) | O(26 · n) | O(1) extra | 🚀 |

---

## Key Takeaway
Searching in ascending character order ensures that the first valid branch reached is lexicographically minimal. Once the strictly-greater condition is satisfied (`greater = True`), no further backtracking is required: the remaining characters are greedily picked in sorted order.

---

## Reference
- LeetCode #3720 — Lexicographically Smallest Permutation Greater Than Target
