# 506 — Relative Ranks

## Problem

Given the scores of athletes in a competition, assign "Gold Medal", "Silver Medal", "Bronze Medal" to the top 3 scores, and the numeric rank (as a string) to everyone else.

**Difficulty:** Easy | **Topic:** Sorting / Hash Table

**[View on LeetCode](https://leetcode.com/problems/relative-ranks/)**

**Examples:**

```text
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
```

---

## My Approach ✅

### Why I Used This Method

Sorting a copy of the scores descending gives the rank order directly; mapping each score value to its medal/rank string in a dict then makes it easy to relabel the original (unsorted) array in one more pass.

```python
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a = sorted(score, reverse=True)

        d = {}

        for i in range(len(a)):
            if i == 0:
                d[a[i]] = "Gold Medal"
            elif i == 1:
                d[a[i]] = "Silver Medal"
            elif i == 2:
                d[a[i]] = "Bronze Medal"
            else:
                d[a[i]] = str(i + 1)

        for i in range(len(score)):
            score[i] = d[score[i]]

        return score
```

### Complexity

* Time: O(n log n) (dominated by the sort)
* Space: O(n) for the sorted copy and the rank map

---

## Alternative Approaches

### Approach 2 — Sort (Index, Score) Pairs Directly

#### Idea

Instead of sorting scores and then mapping back through a dict, sort `(score, original_index)` pairs so the correct output position is known immediately, and write directly into a fresh result array.

```python
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        order = sorted(range(n), key=lambda i: score[i], reverse=True)
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result = [""] * n
        for rank, idx in enumerate(order):
            result[idx] = medals[rank] if rank < 3 else str(rank + 1)
        return result
```

#### Complexity

* Time: O(n log n)
* Space: O(n)

---

## Optimal Approach 🚀

### Idea

Sorting is unavoidable here since the output fundamentally depends on the relative order of all scores, so O(n log n) is optimal for the comparison-based approach. When scores are known to be distinct integers within a bounded range, a counting-sort-style bucket pass can get this down to O(n + k) where k is the score range, but for the general case the sort-based approach above (using index pairs to avoid an extra hash map) is the standard optimal solution.

```python
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        order = sorted(range(n), key=lambda i: -score[i])
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result = [""] * n
        for rank, idx in enumerate(order):
            result[idx] = medals[rank] if rank < 3 else str(rank + 1)
        return result
```

### Complexity

* Time: O(n log n)
* Space: O(n)

---

## Comparison

| Approach                  | Time       | Space | Recommended |
| -------------------------- | ---------- | ----- | ----------- |
| My Approach (dict lookup)  | O(n log n) | O(n)  | ✅           |
| Sort Index Pairs           | O(n log n) | O(n)  | Optional    |
| Optimal                    | O(n log n) | O(n)  | 🚀          |

---

## Key Takeaway

When output depends on the rank of each element relative to the others, sort once to establish order, then map that order back onto the original positions rather than re-sorting or re-scanning per element.

---

## Reference

* LeetCode #506 — Relative Ranks
