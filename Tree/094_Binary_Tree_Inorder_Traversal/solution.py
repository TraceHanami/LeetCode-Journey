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
# Inorder = left, node, right - implemented directly as recursive DFS
# appending into a shared result list.

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root)
        return ans
# Time: O(n)
# Space: O(h) recursion + O(n) output

# ==================================================
# ALTERNATIVE APPROACHES
# ==================================================

# Approach 2 - Iterative with an Explicit Stack
class SolutionIterative:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ans.append(node.val)
            node = node.right
        return ans
# Time: O(n)
# Space: O(h)

# ==================================================
# OPTIMAL APPROACH
# ==================================================
# Morris Traversal - O(1) extra space by threading temporary links
# through null right pointers instead of using a stack.

class SolutionOptimal:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        curr = root
        while curr:
            if not curr.left:
                ans.append(curr.val)
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right is not curr:
                    pred = pred.right
                if not pred.right:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    ans.append(curr.val)
                    curr = curr.right
        return ans
# Time: O(n)
# Space: O(1) extra
