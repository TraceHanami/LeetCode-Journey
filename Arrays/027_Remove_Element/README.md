# 27 — Remove Element

## Problem

Two-pointer: overwrite elements equal to val with valid elements.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/remove-element/)**

**Examples:**
```
nums = [3,2,2,3], val = 3 -> 2
nums = [0,1,2,2,3,0,4,2], val = 2 -> 5
```

---

## Approach 1 — Two pointers ✅

**Idea:** Keep a write pointer; copy elements != val to front.

```python
class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for num in nums:
            if num != val:
                nums[write] = num
                write += 1
        return write
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Swap with end

**Idea:** Swap val elements with end of array and shrink size.

```python
class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Two pointers | O(n) | O(1) | ✅ Yes |
| 2 — Swap with end | O(n) | O(1) | No |

---

## Reference

[LeetCode #27 — Remove Element](https://leetcode.com/problems/remove-element/)
