# 3731 — Find Missing Elements

## Problem
You are given an integer array `nums` consisting of unique integers. Originally, the array contained every integer sequentially within a contiguous range from its minimum value to its maximum value. However, some elements may be missing.

Return a sorted list of all the missing integers in the range `[min(nums), max(nums)]`. If no integers are missing or if `nums` is empty, return an empty list.

**Difficulty:** Easy | **Topic:** Hash Tables
**[View on LeetCode](https://leetcode.com/problems/find-missing-elements/)**

**Examples:**
```text
Input: nums = [1, 4, 2, 5]
Output: [3]
Explanation: The minimum value is 1 and the maximum is 5. The full expected range is [1, 2, 3, 4, 5]. The only missing element is 3.

Input: nums = [1, 2, 3]
Output: []
Explanation: All values in range [1, 3] are present. No elements are missing.
```

---

## My Approaches
### Attempt 1 — Hash Set Range Scan with Empty Guard ✅ Final Accepted Solution
**Why I used it:**
Converts `nums` into a hash set for average O(1) membership lookups. Iterating sequentially from `min(nums)` to `max(nums)` directly identifies missing values in sorted order.

```python
from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        s = set(nums)
        missing = []
        for num in range(min(nums), max(nums) + 1):
            if num not in s:
                missing.append(num)
        return missing
```

**Algorithm Steps:**
1. **Empty-List Guard:** Check `if not nums: return []`. If the input is empty, immediately return an empty list, safely avoiding a `ValueError` when evaluating `min(nums)` and `max(nums)`.
2. Convert `nums` into a hash set `s = set(nums)` to enable O(1) presence checks.
3. Compute the range bounds `min(nums)` and `max(nums)`.
4. Iterate through every integer `num` from `min(nums)` up to `max(nums)` inclusive:
   - If `num not in s`, append `num` to `missing`.
5. Because the loop iterates in ascending order, `missing` is naturally sorted without requiring an extra sorting step.
6. Return `missing`.

**Complexity:**
- Time: O(n + R) — where `n = len(nums)` and `R = max(nums) - min(nums) + 1`. Creating the set takes O(n) time, finding min/max takes O(n), and the range loop runs `R` times with O(1) average lookup per iteration.
- Space: O(n) auxiliary space — to store the elements of `nums` in the hash set `s`, plus O(k) for the output list `missing` where `k` is the count of missing numbers.

---

---

## Standard Approach
### Standard Approach 1 — Sorting and Adjacent Gap Scan
### Idea
Sort the array in ascending order, then scan through adjacent elements `nums[i - 1]` and `nums[i]`. If `nums[i] - nums[i - 1] > 1`, add all integers strictly between them to the result list. This uses O(1) auxiliary space beyond the output list, at the expense of an O(n log n) sort.

```python
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        missing = []

        for i in range(1, len(nums)):
            for val in range(nums[i - 1] + 1, nums[i]):
                missing.append(val)

        return missing
```

### Complexity
- Time: O(n log n + k) — sorting takes O(n log n), and appending `k` missing numbers takes O(k).
- Space: O(1) auxiliary space (or O(n) for Timsort scratch space).

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Approach (Hash Set Range Scan) | O(n + R) | O(n) | ✅ |
| Sorting and Adjacent Gaps | O(n log n + k) | O(1) auxiliary | Optional |

---

## Key Takeaway
A hash set offers O(1) membership testing, making an interval scan straightforward and producing naturally sorted output as long as the range `[min, max]` is reasonably sized. An upfront empty-list guard ensures safety before invoking `min()` and `max()`.

---

## Reference
- LeetCode #3731 — Find Missing Elements
