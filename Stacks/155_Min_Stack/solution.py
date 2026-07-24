from typing import *

# ==================================================
# MY APPROACH (Original Submission)
# ==================================================
# Why:
# A second, parallel stack always tracks "the minimum so far at this
# depth"; popping the main stack keeps the min stack in sync for free.

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
# Time: O(1) per operation
# Space: O(n)

# ==================================================
# ALTERNATIVE APPROACHES
# ==================================================

# Approach 2 - Single Stack of (value, current_min) Pairs
class MinStackTuples:

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
# Time: O(1) per operation
# Space: O(n)

# Approach 3 - Encode the Min Delta (single scalar instead of a second stack)
class MinStackDelta:

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
# Time: O(1) per operation
# Space: O(n)

# ==================================================
# OPTIMAL APPROACH
# ==================================================
# Same two-stack technique as "My Approach" - already O(1) per
# operation and the clearest/most maintainable of the variants.

class MinStackOptimal:

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
# Time: O(1) per operation
# Space: O(n)
