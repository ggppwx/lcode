# Problem
[All Possible Full Binary Trees](https://leetcode.com/problems/all-possible-full-binary-trees)

A full binary tree is a binary tree where each node has exactly 0 or 2 children.
Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.
Each node of each tree in the answer must have node.val = 0.
You may return the final list of trees in any order.

## Thoughts
- obviously it's a recursion
- convert problem to sub-problem 
  ```
  alltrees(n) => alltrees(1) + alltrees(n-1-1)
  ```

## Solution
```python
class Solution:
    # copy the funtion here
    def allPossibleFBT(self, N):
        """
        Thinking as sub-problem
        left, right all possible trees are sub-problems 
        """
        if N % 2 == 0:
            return []

        if N == 1:
            return [TreeNode(0)]

        result = []
        for i in range(N):
            leftN = i
            rightN = N - i - 1
            for rootLeft in self.allPossibleFBT(leftN):
                for rootRight in self.allPossibleFBT(rightN):
                    node = TreeNode(0)
                    node.left = rootLeft
                    node.right = rootRight
                    result.append(node)
        return result
```

## Tags
|Recursion|Tree|
## Marks
Help

[comment]: <timestamp:2019-06-23>
