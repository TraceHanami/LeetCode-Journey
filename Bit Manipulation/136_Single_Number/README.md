# 136 — Single Number

## Problem

XOR of all elements — duplicates cancel out, leaving the unique number.

**Difficulty:** Easy | **Topic:** Bit Manipulation

**[View on LeetCode](https://leetcode.com/problems/single-number/)**

**Examples:**
```
nums = [2,2,1] -> 1 
nums = [1] -> 1
nums = [4,1,2,1,2] -> 4
```
---

## Approach 1 — XOR ✅

**Idea:** XOR all numbers. Pairs cancel to 0; result is the single number.

```python
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

```
**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Hash set

**Idea:** Add to set if not present, remove if present. Remaining element is the answer.

```python
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return seen.pop()
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 3 — Math

**Idea:** 2*sum(set(nums)) - sum(nums).

```python
class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
```

**Complexity:**
- Time: O(n)
- Space: O(n)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — XOR | O(n) | O(1) | ✅ Yes |
| 2 — Hash set | O(n) | O(n) | No |
| 3 — Math | O(n) | O(n) | No |

---

## Reference

[LeetCode #136 — Single Number](https://leetcode.com/problems/single-number/)
