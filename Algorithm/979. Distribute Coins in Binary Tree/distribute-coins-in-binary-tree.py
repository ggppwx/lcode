"""
Problem
Distribute Coins in Binary Tree
(https://leetcode.com/problems/distribute-coins-in-binary-tree)
Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.
In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.
Example 1:
Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

Example 2:
Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.

Example 3:
Input: [1,0,2]
Output: 2

Example 4:
Input: [1,0,0,null,3]
Output: 4
 

Note:
1<= N <= 100
0 <= node.val <= N


"""
import unittest

class Solution:
    # copy the funtion here
    def distributeCoins(self, root: 'TreeNode') -> 'int':
        """
        Looking at the problem with Sub-problem concept in mind
        # of coin current node needs = # missing on left + # surplus on right  + current node surplus
        but # of steps =  # missing on left + # surplus on right
        solve the problem by writing down examples 
        """
        self.steps = 0
        self.visit(root)
        return self.steps



    def visit(self, node):
        if node == None:
            return 0
        
        left = self.visit(node.left)
        right = self.visit(node.right)

        self.steps += abs(left) + abs(right)
        offset = node.val - 1
        return left + right + offset




class TestSolution(unittest.TestCase):
    def test_function(self):
        s = Solution()
        # ret = s.new_function()


if __name__ == '__main__':
    unittest.main()
