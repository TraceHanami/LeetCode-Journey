# 169 — Majority Element

## Problem

Boyer-Moore Voting: the majority element cancels out all others.

**Difficulty:** Easy | **Topic:** Arrays

**[View on LeetCode](https://leetcode.com/problems/majority-element/)**

**Examples:**
```
nums = [3,2,3] -> 3
nums = [2,2,1,1,1,2,2] -> 2
```

---

## Approach 1 — Boyer-Moore Voting ✅

**Idea:** Maintain candidate and count. Increment if same, decrement if different, reset at 0.

```python
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate
```

**Complexity:**
- Time: O(n)
- Space: O(1)

---

## Approach 2 — Hash map count

**Idea:** Count frequencies with Counter, return element with count > n//2.

```python
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        return Counter(nums).most_common(1)[0][0]

```

**Complexity:**
- Time: O(n)
- Space: O(n)

---

## Approach 3 — Sort

**Idea:** Sorted array — majority element always occupies index n//2.

```python
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
```

**Complexity:**
- Time: O(n log n)
- Space: O(1)

---



## Comparison

| Approach | Time | Space | Recommended |
|---|---|---|---|
| 1 — Boyer-Moore Voting | O(n) | O(1) | ✅ Yes |
| 2 — Hash map count | O(n) | O(n) | No |
| 3 — Sort | O(n log n) | O(1) | No |

---

## Reference

[LeetCode #169 — Majority Element](https://leetcode.com/problems/majority-element/)
