# 136 — Single Number

## Problem
Given a non-empty array where every element appears twice except for one, find that single one.

**Difficulty:** Easy | **Topic:** Bit Manipulation
**[View on LeetCode](https://leetcode.com/problems/single-number/)**

**Examples:**
```text
Input: nums = [4,1,2,1,2]
Output: 4
```

---

## My Approaches
### Attempt 1 — XOR All Elements ✅ Final Accepted Solution
**Why I used it:**
XOR cancels out pairs of equal numbers, leaving only the one without a pair.

```python
def singleNumber(self, nums: List[int]) -> int:
    result = 0
    for n in nums:
        result ^= n
    return result
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
XOR is commutative, associative, and a number XORed with itself is 0. XORing every element together cancels all duplicates in pairs, leaving only the unpaired number.

```python
def singleNumber(self, nums: List[int]) -> int:
    result = 0
    for n in nums:
        result ^= n
    return result
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (XOR All Elements) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
XOR-cancellation is the go-to trick whenever a problem guarantees everything appears in pairs except one element.

---

## Reference
- LeetCode #136 — Single Number
