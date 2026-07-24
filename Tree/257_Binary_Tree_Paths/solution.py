from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ==================================================
# MY APPROACH (Original Submission)
# ==================================================
# Why:
# DFS with a shared, mutable path buffer; append on the way down,
# record the path at a leaf, pop on the way back up (backtracking).

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def dfs(node, path):
            if not node:
                return

            path.append(str(node.val))

            if not node.left and not node.right:
                ans.append("->".join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)

            path.pop()

        dfs(root, [])
        return ans
# Time: O(n^2) worst case (output-dominated)
# Space: O(h) recursion + O(n) output

# ==================================================
# ALTERNATIVE APPROACHES
# ==================================================

# Approach 2 - Passing Strings Directly (no explicit backtracking)
class SolutionStringPassing:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def dfs(node, path):
            if not node:
                return
            path = path + str(node.val)
            if not node.left and not node.right:
                ans.append(path)
                return
            dfs(node.left, path + "->")
            dfs(node.right, path + "->")

        dfs(root, "")
        return ans
# Time: O(n^2)
# Space: O(h) recursion + O(n) output

# Approach 3 - Iterative with an Explicit Stack
class SolutionIterative:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        ans = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                ans.append(path)
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
        return ans
# Time: O(n^2)
# Space: O(n)

# ==================================================
# OPTIMAL APPROACH
# ==================================================
# Same backtracking DFS technique as "My Approach" - already optimal;
# output size itself can be O(n^2), so no faster asymptotic solution exists.

class SolutionOptimal:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        path = []

        def dfs(node):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                ans.append("->".join(path))
            else:
                dfs(node.left)
                dfs(node.right)
            path.pop()

        dfs(root)
        return ans
# Time: O(n^2) worst case
# Space: O(h)
