# 283 — Move Zeroes

## Problem

Two pointers: keep a write pointer for non-zero elements, fill rest with zeros.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/move-zeroes/)**

**Examples:**
```
nums = [0,1,0,3,12] -> [1,3,12,0,0]
nums = [0] ->[0]
```

---

## Approach 1 — Two pointers ✅

**Idea:** Write pointer advances only on non-zero. After loop, fill rest with 0.

```python
class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for num in nums:
            if num != 0:
                nums[write] = num
                write += 1
        while write < len(nums):
            nums[write] = 0
            write += 1
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Partition

**Idea:** Swap non-zero with write pointer position.

```python
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write], nums[i] = nums[i], nums[write]
                write += 1
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Two pointers | O(n) | O(1) | ✅ Yes |
| 2 — Partition | O(n) | O(1) | No |

---

## Reference

[LeetCode #283 — Move Zeroes](https://leetcode.com/problems/move-zeroes/)
