"""
Problem
Binary Tree Pruning
(https://leetcode.com/problems/binary-tree-pruning)
We are given the head node root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]
 
Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.


Example 2:
Input: [1,0,1,0,0,0,1]
Output: [1,null,1,null,1]



Example 3:
Input: [1,1,0,1,1,0,1,0]
Output: [1,1,0,1,1,null,1]

"""
import unittest

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None

        if root.val == 0 and root.left == None and root.right == None:
            return None

        self.visit(root, None, -1)
        return root


    def visit(self, node, parent, leftorright):
        """
        This is a post-order traversal
        Rremove the node from the bottom
        in order to remove current node, pass parent node to the function 
        """
        if node == None:
            return

        self.visit(node.left, node, 0)
        self.visit(node.right, node, 1)

        if node.val == 0 and node.left == None and node.right == None:
            # remove the node
            if leftorright == 0:
                parent.left = None
            else:
                parent.right = None


class TestSolution(unittest.TestCase):
    def test_function(self):
        s = Solution()
        # ret = s.new_function()


if __name__ == '__main__':
    unittest.main()
