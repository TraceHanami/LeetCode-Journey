# 3699 — Number of ZigZag Arrays I

## Problem
Count the number of length-n arrays with values in [l, r] that strictly alternate between rising and falling at every step (a zigzag pattern), modulo 1e9+7.

**Difficulty:** Hard | **Topic:** Dynamic Programming
**[View on LeetCode](https://leetcode.com/problems/number-of-zigzag-arrays-i/)**

**Examples:**
```text
Input: n = 2, l = 1, r = 3
Output: 9

Input: n = 3, l = 1, r = 3
Output: 14
```

---

## My Approaches
### Attempt 1 — Prefix-Sum DP over Value Range ✅ Final Accepted Solution
**Why I used it:**
For each position, track how many zigzag arrays end at each value going 'up' vs 'down' next, using prefix sums to update whole ranges in O(m) per step instead of O(m^2).

```python
def zigZagArrays(self, n: int, l: int, r: int) -> int:
    mod = 10**9 + 7
    m = r - l + 1
    if n == 1:
        return m
    up = [0] * (m + 1)
    down = [0] * (m + 1)
    for i in range(1, m + 1):
        up[i] = i - 1
        down[i] = m - i
    if n == 2:
        return (sum(up) + sum(down)) % mod
    for _ in range(n - 2):
        pu = [0] * (m + 1)
        pd = [0] * (m + 1)
        for i in range(1, m + 1):
            pu[i] = (pu[i - 1] + up[i]) % mod
            pd[i] = (pd[i - 1] + down[i]) % mod
        total_up = pu[m]
        nu = [0] * (m + 1)
        nd = [0] * (m + 1)
        for i in range(1, m + 1):
            nu[i] = pd[i - 1]
            nd[i] = (total_up - pu[i]) % mod
        up, down = nu, nd
    return (sum(up) + sum(down)) % mod
```

**Complexity:**
- Time: O(n * m)
- Space: O(m)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Define up[i] and down[i] as the number of zigzag sequences of the current length ending at value i, where the next move must go up or down respectively. Transitioning to the next length requires summing over a range of previous values — using prefix sums turns each O(m) transition into O(1) per value instead of O(m), giving O(n*m) total instead of O(n*m^2).

```python
def zigZagArrays(self, n: int, l: int, r: int) -> int:
    MOD = 10**9 + 7
    m = r - l + 1
    if n == 1:
        return m % MOD
    up = [i for i in range(m + 1)]      # up[i] placeholder, real init below
    up = [0] + [1] * m
    down = [0] + [1] * m
    for _ in range(n - 2):
        prefix_up = [0] * (m + 1)
        prefix_down = [0] * (m + 1)
        for i in range(1, m + 1):
            prefix_up[i] = (prefix_up[i - 1] + up[i]) % MOD
            prefix_down[i] = (prefix_down[i - 1] + down[i]) % MOD
        new_up, new_down = [0] * (m + 1), [0] * (m + 1)
        for i in range(1, m + 1):
            new_up[i] = prefix_down[i - 1]
            new_down[i] = (prefix_up[m] - prefix_up[i]) % MOD
        up, down = new_up, new_down
    return (sum(up) + sum(down)) % MOD
```

### Complexity
- Time: O(n * m)
- Space: O(m)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Prefix-Sum DP over Value Range) | O(n * m) | O(m) | ✅ |
| Standard Approach 1 | O(n * m) | O(m) | ✅ |


---

## Key Takeaway
When a DP transition needs a range sum over previous states, computing a prefix sum first turns an O(m) transition per state into O(1), which is the difference between an O(n·m²) and O(n·m) solution.

---

## Reference
- LeetCode #3699 — Number of ZigZag Arrays I
