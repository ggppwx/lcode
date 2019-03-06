"""
Problem
Kth Smallest Element in a BST
(https://leetcode.com/problems/kth-smallest-element-in-a-bst)



Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Note: You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
Follow up: What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?



"""
import unittest

class Solution:
    """ Notes:
    should be an in-order traversal
    Be aware: closure in python, use nolocal if you wanna change the value
    """
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.result = None
        def visit(node):
            if not node:
                return 

            visit(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return

            visit(node.right)

        visit(root)
        return self.result




class TestSolution(unittest.TestCase):
    def test_function(self):
        s = Solution()
        # ret = s.new_function()


if __name__ == '__main__':
    unittest.main()
