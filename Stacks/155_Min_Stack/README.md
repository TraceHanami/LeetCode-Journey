# 155 — Min Stack

## Problem

Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element, all in O(1) time.

**Difficulty:** Medium | **Topic:** Stack Design

**[View on LeetCode](https://leetcode.com/problems/min-stack/)**

**Examples:**

```text
Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output:
[null,null,null,null,-3,null,0,-2]
```

---

## My Approach ✅

### Why I Used This Method

Keeping a second, parallel stack that always tracks "the minimum so far at this depth" means popping the main stack automatically keeps the minimum stack in sync — no recomputation needed, and every operation stays O(1).

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

### Complexity

* Time: O(1) for every operation (`push`, `pop`, `top`, `getMin`)
* Space: O(n) — the min-stack duplicates one entry per element in the main stack

---

## Alternative Approaches

### Approach 2 — Single Stack of (value, current_min) Pairs

#### Idea

Instead of two parallel arrays, push a tuple of `(value, min_so_far)` onto one stack. This keeps everything in a single data structure, trading slightly more memory per entry for one less list to keep synchronized.

```python
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        current_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
```

#### Complexity

* Time: O(1) for every operation
* Space: O(n)

---

### Approach 3 — Encode the Min Delta (O(1) Extra Space per Push)

#### Idea

Store only the difference between each pushed value and the running minimum, updating the tracked minimum in-place. This avoids a second stack entirely at the cost of trickier bookkeeping on `pop`.

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_val = val
        else:
            self.stack.append(val - self.min_val)
            if val < self.min_val:
                self.min_val = val

    def pop(self) -> None:
        diff = self.stack.pop()
        if diff < 0:
            self.min_val = self.min_val - diff

    def top(self) -> int:
        diff = self.stack[-1]
        return self.min_val if diff < 0 else self.min_val + diff

    def getMin(self) -> int:
        return self.min_val
```

#### Complexity

* Time: O(1) for every operation
* Space: O(n) for the stack, but only a single `min_val` scalar of extra tracking state instead of a second stack

---

## Optimal Approach 🚀

### Idea

All three approaches above already achieve O(1) time for every operation, which is optimal — none of the four operations can beat constant time. "My Approach" (two parallel stacks) is the clearest and most maintainable of the three, and is the version most commonly recommended in practice.

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(val if not self.minStack else min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
```

### Complexity

* Time: O(1) per operation
* Space: O(n)

---

## Comparison

| Approach                  | Time | Space | Recommended |
| -------------------------- | ---- | ----- | ----------- |
| My Approach (two stacks)   | O(1) | O(n)  | ✅           |
| Tuple Stack                | O(1) | O(n)  | Optional    |
| Min-Delta Encoding         | O(1) | O(n)  | Optional    |
| Optimal (two stacks)       | O(1) | O(n)  | 🚀          |

---

## Key Takeaway

Any stack-augmentation problem where you need "the current best of some property" in O(1) can be solved by keeping a second, synchronized stack that always reflects that property at the current depth — pop it in lockstep and the invariant maintains itself.

---

## Reference

* LeetCode #155 — Min Stack
