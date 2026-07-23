# 283 — Move Zeroes

## Problem
Given an array, move all 0's to the end while maintaining the relative order of the non-zero elements, in-place.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/move-zeroes/)**

**Examples:**
```text
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

---

## My Approaches
### Attempt 1 — Swap Every Non-Zero Forward
**Why I used it:**
First pass — always swap, even when i == l, which does redundant self-swaps but is still correct.

```python
def moveZeroes(self, nums: List[int]) -> None:
    l = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---
### Attempt 2 — Swap Only When Needed ✅ Final Accepted Solution
**Why I used it:**
Skip the swap when i == l to avoid pointless self-swaps — a small but meaningful cleanup.

```python
def moveZeroes(self, nums: List[int]) -> None:
    l = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            if i != l:
                nums[l], nums[i] = nums[i], nums[l]
            l += 1
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Use a slow pointer marking where the next non-zero value should go. Scan with a fast pointer; whenever a non-zero is found, swap it into the slow pointer's position and advance both. This naturally pushes all zeros to the end while preserving order.

```python
def moveZeroes(self, nums: List[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Swap Only When Needed) | O(n) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |
| Swap Every Non-Zero Forward | O(n) | O(1) | ❌ |


---

## Key Takeaway
Skipping the self-swap when the pointers coincide is a nice micro-optimization, though both versions are O(n) in the same single pass.

---

## Reference
- LeetCode #283 — Move Zeroes
