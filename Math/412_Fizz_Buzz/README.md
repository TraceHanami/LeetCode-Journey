# 412 — Fizz Buzz

## Problem

Given an integer `n`, return a string array where each number from 1 to n is replaced by "Fizz" if divisible by 3, "Buzz" if divisible by 5, "FizzBuzz" if divisible by both, and the number itself (as a string) otherwise.

**Difficulty:** Easy | **Topic:** Math / Simulation

**[View on LeetCode](https://leetcode.com/problems/fizz-buzz/)**

**Examples:**

```text
Input: n = 3
Output: ["1","2","Fizz"]

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
```

---

## My Approach ✅

### Why I Used This Method

Checking the "divisible by both" case first, then each individual case, directly mirrors the problem statement's rules and avoids ever double-labeling a multiple of 15.

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                a.append("FizzBuzz")
            elif i%3==0:
                a.append("Fizz")
            elif i%5==0:
                a.append("Buzz")
            else:
                a.append(str(i))
        return a
```

### Complexity

* Time: O(n)
* Space: O(1) extra (excluding the required output array)

---

## Alternative Approaches

### Approach 2 — String Concatenation

#### Idea

Build up the answer by concatenating "Fizz" and/or "Buzz" instead of branching on the combined condition; falls back to the number itself only if nothing got appended.

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            s = ""
            if i % 3 == 0:
                s += "Fizz"
            if i % 5 == 0:
                s += "Buzz"
            ans.append(s or str(i))
        return ans
```

#### Complexity

* Time: O(n)
* Space: O(1) extra

---

## Optimal Approach 🚀

### Idea

Every one of the n numbers must be examined and produce one output string, so O(n) time is unavoidable — both submitted-style approaches are already optimal. The concatenation version is marginally preferred in practice since it scales cleanly if more divisibility rules were ever added (e.g. "Jazz" for divisible by 7), without needing a combinatorial explosion of `elif` branches.

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            label = ("Fizz" if i % 3 == 0 else "") + ("Buzz" if i % 5 == 0 else "")
            result.append(label if label else str(i))
        return result
```

### Complexity

* Time: O(n)
* Space: O(1) extra

---

## Comparison

| Approach              | Time | Space | Recommended |
| ---------------------- | ---- | ----- | ----------- |
| My Approach (branching) | O(n) | O(1)  | ✅           |
| String Concatenation    | O(n) | O(1)  | Optional    |
| Optimal                 | O(n) | O(1)  | 🚀          |

---

## Key Takeaway

FizzBuzz is a good reminder that "combined condition first" branching and "build up the string piece by piece" are equally valid ways to avoid double-labeling multiples of both divisors — the latter generalizes better if more rules get added later.

---

## Reference

* LeetCode #412 — Fizz Buzz
