# Problem
[Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers)

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
Note: A leaf is a node with no children.

Example:
```
Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
```
Example 2:
```
Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```

## Analysis
- Time: O(N)
  
## Thoughts
- Simple DFS
- Be ware of only checking leaf node.
  - if check `none` node, the result will be repeatly added 

## Solution
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.result = 0

        def dfs(node, pre):
            if not node:
                # previous node is leaf                
                return
                        
            curr = pre * 10 + node.val

            if not node.left and not node.right: 
                # leaf node
                self.result += curr
                return 

            dfs(node.left, curr)
            dfs(node.right, curr)
        
        dfs(root, 0)

        return self.result

```

## Tags
Tree

## Marks

[comment]: <timestamp:2019-06-20>