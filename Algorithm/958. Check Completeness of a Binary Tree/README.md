# Problem
[Check Completeness of a Binary Tree](https://leetcode.com/problems/check-completeness-of-a-binary-tree)

Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

## Analysis

## Thoughts
- first thoughts, BFS
- But we found it is not neccessary to go through all 
  - 分类讨论法
  - if has left/right
  - if ont has right X
  - if only has left, next_must_be_leaf
  - **if is leaf, next_must_be_leaf** 
- 分类讨论每种情况都要仔细考虑，尤其是全局变量的设置

## Solution
```python
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return False
        queue = [root]
        next_must_be_leaf = False
        while queue:
            front = queue.pop(0)
            if next_must_be_leaf:                
                if front.left or front.right:
                    # not leaf
                    return False

            if front.left and front.right:
                queue.append(front.left)
                queue.append(front.right)
            elif not front.left and front.right:
                return False
            elif front.left and not front.right:
                queue.append(front.left)
                next_must_be_leaf = True
            else:
                # Dont forget this 
                next_must_be_leaf = True
            
        return True
        
```
## Tags
Tree

## Marks

[comment]: <timestamp:>