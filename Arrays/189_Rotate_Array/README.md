# 189 — Rotate Array

## Problem

Reverse the whole array, then reverse each part separately.

**Difficulty:** Med | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/rotate-array/)**

**Examples:**
```
nums = [1,2,3,4,5,6,7], k = 3 -> [5,6,7,1,2,3,4]
nums = [-1,-100,3,99], k = 2 -> [3,99,-1,-100]
```

---

## Approach 1 — Three reverses ✅

**Idea:** Reverse all, reverse first k, reverse remaining n-k.

```python
class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(lo, hi):
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Extra array

**Idea:** Place each element at (i+k)%n in a new array.

```python
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        temp = nums[:]
        for i in range(n):
            nums[(i + k) % n] = temp[i]

```
**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 3 — Cyclic replacement

**Idea:** Follow cycles — place each element at its final position.

```python
class Solution3:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        count = 0
        start = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                if current == start:
                    break
            start += 1
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Three reverses | O(n) | O(1) | ✅ Yes |
| 2 — Extra array | O(n) | O(n) | No |
| 3 — Cyclic replacement | O(n) | O(1) | No |

---

## Reference

[LeetCode #189 — Rotate Array](https://leetcode.com/problems/rotate-array/)
