# 257 — Binary Tree Paths

## Problem

Given the root of a binary tree, return all root-to-leaf paths, formatted as strings like `"1->2->5"`.

**Difficulty:** Easy | **Topic:** Tree / DFS / Backtracking

**[View on LeetCode](https://leetcode.com/problems/binary-tree-paths/)**

**Examples:**

```text
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Input: root = [1]
Output: ["1"]
```

---

## My Approach ✅

### Why I Used This Method

A DFS that builds up a running `path` list and only converts it to a string when a leaf is reached naturally captures every root-to-leaf path; popping after recursing lets the same `path` list be reused across branches instead of allocating a new one at every call.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
```

### Complexity

* Time: O(n^2) worst case — building each of up to n leaf paths costs O(n) for the `"->".join`, and there can be O(n) leaves in a skewed-ish tree
* Space: O(h) for the recursion stack and running path, where h is the tree height, plus O(n) for the output

---

## Alternative Approaches

### Approach 2 — Passing Strings Directly (No Backtracking)

#### Idea

Instead of mutating a shared list and popping afterward, pass a new path string down each recursive call. This avoids explicit backtracking at the cost of allocating a new string per call.

```python
class Solution:
    def binaryTreePaths(self, root):
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
```

#### Complexity

* Time: O(n^2)
* Space: O(h) recursion depth + O(n) output

---

### Approach 3 — Iterative with an Explicit Stack

#### Idea

Simulate the DFS using an explicit stack of `(node, path_so_far)` pairs, avoiding Python's recursion limit for very deep trees.

```python
class Solution:
    def binaryTreePaths(self, root):
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
```

#### Complexity

* Time: O(n^2)
* Space: O(n) for the stack and output in the worst case

---

## Optimal Approach 🚀

### Idea

There's no way to beat O(n^2) time in the worst case, since the total length of all root-to-leaf path strings can itself be quadratic (a full binary tree has many long leaf paths). The backtracking DFS from "My Approach" is already the accepted, standard optimal solution: it visits each node once and reuses a single mutable buffer instead of repeatedly copying strings.

```python
class Solution:
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
```

### Complexity

* Time: O(n^2) worst case (dominated by output size)
* Space: O(h)

---

## Comparison

| Approach                  | Time    | Space       | Recommended |
| -------------------------- | ------- | ----------- | ----------- |
| My Approach (backtracking) | O(n^2)  | O(h)        | ✅           |
| String-Passing (no pop)    | O(n^2)  | O(h)        | Optional    |
| Iterative Stack            | O(n^2)  | O(n)        | Optional    |
| Optimal                    | O(n^2)  | O(h)        | 🚀          |

---

## Key Takeaway

Backtracking (append, recurse, pop) lets a DFS reuse one mutable buffer across all branches instead of copying a growing string or list at every recursive call.

---

## Reference

* LeetCode #257 — Binary Tree Paths
