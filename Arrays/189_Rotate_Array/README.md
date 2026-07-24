# 189 — Rotate Array

## Problem

Rotate an array to the right by k steps, in-place.

**Difficulty:** Medium | **Topic:** Array / Two Pointers

**[View on LeetCode](https://leetcode.com/problems/rotate-array/)**

**Examples:**

```text
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
```

---

## My Approach ✅

### Why I Used This Method

Slicing the last `k` elements and putting them in front of the rest is the most direct expression of "rotate right by k" in Python.

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        nums[:]=nums[-k:]+nums[:-k]
```

### Complexity

* Time: O(n)
* Space: O(n) (slicing builds new list objects before assigning back)

---

## Alternative Approaches

### Approach 2 — Extra Array with Index Mapping

#### Idea

Compute the destination index `(i + k) % len(nums)` for every element, write into a new array `d`, then copy `d` back into `nums`.

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        d=[0]*len(nums)
        for i in range(len(nums)):
            n=(i+k)%len(nums)
            d[n]=nums[i]
        for i in range(len(nums)):
            nums[i]=d[i]
```

#### Complexity

* Time: O(n)
* Space: O(n)

---

## Optimal Approach 🚀

### Idea

The classic "three reversals" trick achieves the rotation with true O(1) extra space: reverse the whole array, then reverse the first `k` elements, then reverse the remaining `n - k` elements. No auxiliary array or slice copy is needed.

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
```

### Complexity

* Time: O(n)
* Space: O(1)

---

## Comparison

| Approach                  | Time | Space | Recommended |
| -------------------------- | ---- | ----- | ----------- |
| My Approach (slicing)      | O(n) | O(n)  | ✅           |
| Extra Array Index Mapping  | O(n) | O(n)  | Optional    |
| Optimal (three reversals)  | O(n) | O(1)  | 🚀          |

---

## Key Takeaway

Rotating an array is really three reversals in disguise — it's the standard way to get true in-place O(1)-space rotation instead of paying for a second array.

---

## Reference

* LeetCode #189 — Rotate Array
