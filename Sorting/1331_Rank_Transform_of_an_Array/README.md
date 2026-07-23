# 1331 — Rank Transform of an Array

## Problem
Given an array of integers, replace each element with its rank — the smallest value gets rank 1, the next distinct value gets rank 2, and so on. Equal elements get the same rank.

**Difficulty:** Easy | **Topic:** Sorting
**[View on LeetCode](https://leetcode.com/problems/rank-transform-of-an-array/)**

**Examples:**
```text
Input: arr = [40,10,20,30]
Output: [4,1,2,3]
```

---

## My Approaches
### Attempt 1 — Sort Unique Values, Map to Rank ✅ Final Accepted Solution
**Why I used it:**
Sorting the deduplicated values directly gives their rank order — position i in the sorted list is rank i+1.

```python
def arrayRankTransform(self, arr: List[int]) -> List[int]:
    sorted_unique = sorted(set(arr))
    rank = {}
    for i, v in enumerate(sorted_unique, 1):
        rank[v] = i
    return [rank[x] for x in arr]
```

**Complexity:**
- Time: O(n log n)
- Space: O(n)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
Deduplicate and sort the values once to establish their rank order, build a value-to-rank lookup map, then map every original element through that lookup in a single pass — avoids re-sorting or re-searching for each element.

```python
def arrayRankTransform(self, arr: List[int]) -> List[int]:
    rank = {v: i + 1 for i, v in enumerate(sorted(set(arr)))}
    return [rank[x] for x in arr]
```

### Complexity
- Time: O(n log n)
- Space: O(n)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Sort Unique Values, Map to Rank) | O(n log n) | O(n) | ✅ |
| Standard Approach 1 | O(n log n) | O(n) | ✅ |


---

## Key Takeaway
Sorting the deduplicated values once and building a lookup map avoids repeatedly searching for each element's rank.

---

## Reference
- LeetCode #1331 — Rank Transform of an Array
