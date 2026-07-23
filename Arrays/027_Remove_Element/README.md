# 027 — Remove Element

## Problem
Remove all occurrences of val from nums in-place and return the new length.

**Difficulty:** Easy | **Topic:** Arrays
**[View on LeetCode](https://leetcode.com/problems/remove-element/)**

**Examples:**
```text
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
```

---

## My Approaches
### Attempt 1 — Repeated .remove() Calls ✅ Final Accepted Solution
**Why I used it:**
Quick to write using the built-in list method, though it shifts the whole list on every removal.

```python
def removeElement(self, nums: List[int], val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)
```

**Complexity:**
- Time: O(n^2)
- Space: O(1)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Use a write pointer that only advances when the current value is not the one being removed — every kept value gets copied to the front of the array in one pass.

```python
def removeElement(self, nums: List[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Repeated .remove() Calls) | O(n^2) | O(1) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
A single write-pointer pass avoids the O(n) shifting cost that list.remove() pays on every call.

---

## Reference
- LeetCode #27 — Remove Element
