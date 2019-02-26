"""
Problem
Construct Binary Tree from Preorder and Postorder Traversal
(https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal)




"""
import unittest

class Solution:
    """ Notes:
    The difficult part is the corner case:
    1, 2, 3, 4
    4, 3, 2, 1
    we put 2,3,4 in the left (or right ) and None on the right 
    """
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre or not post:
            return None

        new_node = TreeNode(pre[0])

        if len(pre) == 1 or len(post) == 1:
            return new_node


        left_pre = []
        right_pre = []
        left_post = []
        right_post = []
        for idx, val in enumerate(pre):
            if val == post[-2]: 
                # idx is the right node
                if idx == 1:
                    left_pre = pre[1:]
                    right_pre = []
                else:
                    left_pre = pre[1:idx]
                    right_pre = pre[idx:]

        for idx, val in enumerate(post):
            if val == pre[1]: # pre[1] left child root node
                if idx == len(post) - 2:
                    left_post = post[:-1]
                    right_post = []
                else:
                    left_post = post[:idx+1]
                    right_post = post[idx+1:-1]

        new_node.left = self.constructFromPrePost(left_pre, left_post )
        new_node.right = self.constructFromPrePost(right_pre, right_post )
        return new_node

    



class TestSolution(unittest.TestCase):
    def test_function(self):
        s = Solution()
        # ret = s.new_function()


if __name__ == '__main__':
    unittest.main()
