from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Stack of Expected Closers
# Why: Push the expected closing bracket whenever an opener is seen; any mismatch or leftover bracket at the end means invalid.
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution1:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}
        for ch in s:
            if ch in pairs:
                stack.append(pairs[ch])
            else:
                if not stack or stack.pop() != ch:
                    return False
        return not stack


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(n)
# ─────────────────────────────────────────────────
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}
        for ch in s:
            if ch in pairs:
                stack.append(pairs[ch])
            elif not stack or stack.pop() != ch:
                return False
        return not stack

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
