# 022 — Generate Parentheses

## Problem
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

**Difficulty:** Medium | **Topic:** Backtracking
**[View on LeetCode](https://leetcode.com/problems/generate-parentheses/)**

**Examples:**
```text
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]
```

---

## My Approaches
### Attempt 1 — Recursive Backtracking with Balance Constraints ✅ Final Accepted Solution
**Why I used it:**
Recursively constructs valid parentheses strings by maintaining counts of placed opening (`i`) and closing (`j`) parentheses, pruning invalid branches immediately.

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a=[]
        def sol(s,i,j):
            if len(s)==2*n:
                a.append(s)
                return 
            if i<n:
                sol(s+"(",i+1,j)
            if j<i:
                sol(s+")",i,j+1)
        sol("",0,0)
        return a
```

**Algorithm Steps:**
1. Initialize an empty list `a` to collect all completed valid combinations.
2. Define a recursive helper `sol(s, i, j)` where:
   - `s` is the current string being built.
   - `i` tracks the number of opening parentheses `(` placed so far.
   - `j` tracks the number of closing parentheses `)` placed so far.
3. **Base Case:** When `len(s) == 2 * n`, all `n` pairs have been placed correctly; append `s` to `a` and return.
4. **Opening Parenthesis Constraint (`i < n`):** An opening parenthesis `(` can be added whenever fewer than `n` opening parentheses have been placed. Recurse with `s + "("`, `i + 1`, and `j`.
5. **Closing Parenthesis Constraint (`j < i`):** A closing parenthesis `)` can only be added when the number of placed closing parentheses is strictly less than the number of opening parentheses (`j < i`). This ensures every prefix never has unmatched closing brackets. Recurse with `s + ")"`, `i`, and `j + 1`.
6. Start the recursion with `sol("", 0, 0)` and return `a`.

**Complexity:**
- Time: O(4^n / √n) — bounded by the n-th Catalan number $C_n = \frac{1}{n+1}\binom{2n}{n} \approx \frac{4^n}{n^{1.5}\sqrt{\pi}}$. Each valid string has length $2n$, taking O(n) work to build/copy, giving $O(\frac{4^n}{\sqrt{n}})$ overall.
- Space: O(n) auxiliary space for the recursion call stack (maximum depth $2n$), plus $O(\frac{4^n}{\sqrt{n}} \cdot n)$ to store the generated combinations in the output list.

---

---

## Standard Approach
### Standard Approach 1 — Backtracking with Character Buffer / Array ✅
### Idea
The standard backtracking approach follows the exact same constraints (`open_count < n` and `close_count < open_count`). In environments where string immutability causes repeated copies, maintaining a mutable character list and popping on backtrack (`path.append('(')`, `recurse()`, `path.pop()`) avoids intermediate string allocations until a complete valid sequence is formed.

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrack(open_count: int, close_count: int):
            if len(path) == 2 * n:
                res.append("".join(path))
                return

            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, close_count)
                path.pop()

            if close_count < open_count:
                path.append(")")
                backtrack(open_count, close_count + 1)
                path.pop()

        backtrack(0, 0)
        return res
```

### Complexity
- Time: O(4^n / √n) — bounded by the n-th Catalan number $C_n$.
- Space: O(n) auxiliary space for the call stack and mutable `path` buffer.

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Approach (Recursive String Concatenation) | O(4^n / √n) | O(n) auxiliary | ✅ |
| Standard Approach (Backtracking with Buffer) | O(4^n / √n) | O(n) auxiliary | ✅ |

---

## Key Takeaway
Well-formed parentheses sequences are defined by two invariant rules: we cannot place more than `n` opening brackets (`i < n`), and we can never place a closing bracket without an unmatched preceding opening bracket (`j < i`). Enforcing these rules during generation eliminates all invalid branches up front.

---

## Reference
- LeetCode #22 — Generate Parentheses
