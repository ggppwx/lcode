# Problem
[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal)

Given a binary tree, return the inorder traversal of its nodes' values.
do it iteratively

## Thoughts
- recursive solution is simple. the difficult part is iterate solution
    1. pushing all left nodes to **stack** until no left
    2. pop up the **statck** , add to result
    3. check the popped node, if it has right, push right to queue
    4. set the node to the right node just pushed in
    5. go back to step 1. 

## Solution
```python
class Solution:
    """ Notes:
    iteration solution is harder
    pushing all left nodes to stack
    special cases:
    all left, all right, one node,     
    """
    # copy the funtion here
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        queue = []
        while queue:

            # putting all left nodes to queue
            while node.left:
                queue.append(node.left)
                node = node.left

            last = queue.pop()
            result.append(last.val)

            if last.right:
                queue.append(last.right)
                node = last.right

        return result
```


## Tags
Tree

[comment]: <timestamp:2019-06-15>
