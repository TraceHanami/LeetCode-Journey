# 904 — Fruit Into Baskets

## Problem
Given an array of fruit types, find the length of the longest subarray containing at most 2 distinct types (you have exactly 2 baskets, one type per basket).

**Difficulty:** Medium | **Topic:** Sliding Window
**[View on LeetCode](https://leetcode.com/problems/fruit-into-baskets/)**

**Examples:**
```text
Input: fruits = [1,2,1]
Output: 3

Input: fruits = [0,1,2,2]
Output: 3
```

---

## My Approaches
### Attempt 1 — Variable-Size Sliding Window with Type Counts ✅ Final Accepted Solution
**Why I used it:**
Expand the window by adding fruits; whenever more than 2 distinct types appear, shrink from the left until back down to 2.

```python
def totalFruit(self, fruits: List[int]) -> int:
    i = 0
    counts = {}
    best = 0
    for j in range(len(fruits)):
        counts[fruits[j]] = counts.get(fruits[j], 0) + 1
        while len(counts) > 2:
            counts[fruits[i]] -= 1
            if counts[fruits[i]] == 0:
                del counts[fruits[i]]
            i += 1
        best = max(best, j - i + 1)
    return best
```

**Complexity:**
- Time: O(n)
- Space: O(1) (at most 3 keys)

---

---

## Standard Approach
### Standard Approach 1 — Recommended ✅
### Idea
This is 'longest subarray with at most K distinct elements' with K=2, phrased as a fruit-picking story. Expand the right edge of the window, and whenever the distinct-type count exceeds 2, shrink from the left until it's valid again — each element is added and removed from the window at most once.

```python
def totalFruit(self, fruits: List[int]) -> int:
    left = 0
    count = {}
    best = 0
    for right, fruit in enumerate(fruits):
        count[fruit] = count.get(fruit, 0) + 1
        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1
        best = max(best, right - left + 1)
    return best
```

### Complexity
- Time: O(n)
- Space: O(1)

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Final Solution (Variable-Size Sliding Window with Type Counts) | O(n) | O(1) (at most 3 keys) | ✅ |
| Standard Approach 1 | O(n) | O(1) | ✅ |


---

## Key Takeaway
This is the classic 'longest substring/subarray with at most K distinct values' pattern — expand right, shrink left only when the constraint is violated.

---

## Reference
- LeetCode #904 — Fruit Into Baskets
