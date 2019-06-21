# Problem
[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree)

 Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length
of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree

          1
         / \
        2   3
       / \     
      4   5    

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3]. 

## Thoughts
- Treat the problem as sub-problems
  - if diamter cross the root, recursively finding max depth
  - if not cross the root, 2 sub problem: left/ right

## Solution
```python
class Solution:
    """ Notes:
    treat subtree as sub-problem
    3 cases: on left, on right, across the root
    """
    def find_max_depth_path(self, node):
        '''depth by node number '''
        if not node:
            return 0
        left_path_depth = self.find_max_depth_path(node.left)
        right_path_depth = self.find_max_depth_path(node.right)
        if left_path_depth < right_path_depth:
            return right_path_depth + 1
        else:
            return left_path_depth + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        case1 = self.find_max_depth_path(root.left) + self.find_max_depth_path(root.right)
        case2 = self.diameterOfBinaryTree(root.left)
        case3 = self.diameterOfBinaryTree(root.right)
        return max([case1, case2, case3])
```

## Tags
Tree

[comment]: <timestamp:2019-06-20>
