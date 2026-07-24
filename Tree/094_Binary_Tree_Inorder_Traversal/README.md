# 94 — Binary Tree Inorder Traversal

## Problem

Given the root of a binary tree, return the values of its nodes in inorder traversal order (left, root, right).

**Difficulty:** Easy | **Topic:** Tree / DFS

**[View on LeetCode](https://leetcode.com/problems/binary-tree-inorder-traversal/)**

**Examples:**

```text
Input: root = [1,null,2,3]
Output: [1,3,2]

Input: root = []
Output: []
```

---

## My Approach ✅

### Why I Used This Method

Inorder traversal is defined recursively (left subtree, then node, then right subtree), so a recursive DFS that appends to a shared result list is the most direct way to implement the definition.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
```

### Complexity

* Time: O(n)
* Space: O(h) for the recursion stack, where h is the tree height, plus O(n) for the output

---

## Alternative Approaches

### Approach 2 — Iterative with an Explicit Stack

#### Idea

Simulate the recursion using an explicit stack: push left children until there are none, then visit a node and move to its right subtree. This avoids Python's recursion depth limit on very unbalanced trees.

```python
class Solution:
    def inorderTraversal(self, root):
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
```

#### Complexity

* Time: O(n)
* Space: O(h)

---

## Optimal Approach 🚀

### Idea

Every node must be visited once, so O(n) time is optimal. If O(1) extra space (excluding the output) is required, Morris Traversal threads temporary links through the tree's null right pointers instead of using a stack, then restores the tree structure as it goes.

```python
class Solution:
    def inorderTraversal(self, root):
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
```

### Complexity

* Time: O(n)
* Space: O(1) extra (excluding the output array)

---

## Comparison

| Approach              | Time | Space | Recommended |
| ---------------------- | ---- | ----- | ----------- |
| My Approach (recursive) | O(n) | O(h)  | ✅           |
| Iterative Stack         | O(n) | O(h)  | Optional    |
| Optimal (Morris)        | O(n) | O(1)  | 🚀          |

---

## Key Takeaway

Recursive DFS is the most natural fit for tree traversal definitions; when true O(1) space matters, Morris Traversal trades a temporary rewiring of the tree for dropping the stack entirely.

---

## Reference

* LeetCode #94 — Binary Tree Inorder Traversal
