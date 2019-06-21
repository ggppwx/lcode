# Problem
[Maximum Binary Tree](https://leetcode.com/problems/maximum-binary-tree)

 Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

    The root is the maximum number in the array.
    The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
    The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
```
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
```

## Thoughts
- constructing a tree => sub-problems 
- recursive solution

## Solution
```python
class Solution:
    """ Notes:
    Simple Binary tree problem
    Divide into sub-problem(recursion) to create sub-tree
    """
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        # find the max number
        if not nums:
            return None


        max_val_and_idx = (-1000, -1)
        for idx, val in enumerate(nums):
            if val > max_val_and_idx[0]:
                max_val_and_idx = (val, idx)


        new_node = TreeNode(max_val_and_idx[0])
        max_val_idx = max_val_and_idx[1]
        new_node.left = self.constructMaximumBinaryTree(nums[:max_val_idx])
        new_node.right = self.constructMaximumBinaryTree(nums[max_val_idx+1:])
        return new_node

```
## Tags
|Tree|

[comment]: <timestamp:2019-06-20>
