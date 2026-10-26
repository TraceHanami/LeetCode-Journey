# 056 — Merge Intervals

## Problem
Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

**Difficulty:** Medium | **Topic:** Sorting
**[View on LeetCode](https://leetcode.com/problems/merge-intervals/)**

**Examples:**
```text
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

---

## My Approaches
### Attempt 1 — Sort by Interval Start and Greedy Merge ✅ Final Accepted Solution
**Why I used it:**
Sorting intervals by their starting times ensures that any overlapping intervals become adjacent in the sequence. A single linear pass can then merge overlaps by extending the end boundary.

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        m=[intervals[0]]
        for i in intervals[1:]:
            if m[-1][1]>=i[0]:
                m[-1][1]=max(m[-1][1],i[1])
            else:
                m.append(i)
        return m
```

**Algorithm Steps:**
1. Sort `intervals` in place. Python sorts lists lexicographically by default, meaning intervals are ordered primarily by start time (`intervals[i][0]`) and secondarily by end time (`intervals[i][1]`).
2. Initialize the merged result list `m` with the first interval `intervals[0]`.
   > [!NOTE]
   > This implementation assumes the input `intervals` is non-empty. On LeetCode, problem constraints guarantee `1 <= intervals.length <= 10^4`, so `intervals[0]` is guaranteed to succeed. In a general defensive programming context, an empty list check `if not intervals: return []` would be needed to avoid an `IndexError`.
3. Iterate through each subsequent interval `i` from index 1 onward:
   - Check if the end of the last merged interval `m[-1][1]` is greater than or equal to the start of the current interval `i[0]`.
   - If they overlap (`m[-1][1] >= i[0]`), merge them by updating `m[-1][1] = max(m[-1][1], i[1])`.
   - If they do not overlap, append the current interval `i` as a new entry in `m`.
4. Return the merged list `m`.

**Complexity:**
- Time: O(n log n) — sorting `n` intervals dominates the runtime with O(n log n). The subsequent single pass through the array takes O(n) time.
- Space: O(n) — for the output list `m` storing the merged intervals, plus O(n) auxiliary space used internally by Python's Timsort algorithm.

---

---

## Standard Approach
### Standard Approach 1 — Sorting with Guard Check ✅ Recommended
### Idea
The standard approach follows the exact same sorting and linear merging logic, adding a defensive check for empty inputs at the start.

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            prev = merged[-1]
            if prev[1] >= current[0]:
                prev[1] = max(prev[1], current[1])
            else:
                merged.append(current)

        return merged
```

### Complexity
- Time: O(n log n) — dominated by the sort step.
- Space: O(n) — for output storage and Timsort scratch space.

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Approach (Sort & In-Place Merge) | O(n log n) | O(n) | ✅ |
| Standard Approach (Sort with Guard) | O(n log n) | O(n) | ✅ |

---

## Key Takeaway
Sorting intervals by their starting value transforms a potentially quadratic pair-comparison problem into a linear scan: once sorted, any interval can only ever overlap with its immediate predecessor in the merged list.

---

## Reference
- LeetCode #56 — Merge Intervals
