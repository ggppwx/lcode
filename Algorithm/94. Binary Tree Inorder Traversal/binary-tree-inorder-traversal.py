"""
Problem
Binary Tree Inorder Traversal
(https://leetcode.com/problems/binary-tree-inorder-traversal)

Given a binary tree, return the inorder traversal of its nodes' values.
do it iteratively

"""
import unittest

class Solution:
    """ Notes:
    iteration solution is harder
    pushing all left nodes to stack
    special cases:
    all left, all right, one node, 
    1. pushing all left nodes to queue until no left
    2. pop up the queue, add to result
    3. check the popped node, if it has right, push right to queue
    4. set the node to the right node just pushed in
    5. go back to step 1. 
    """
    # copy the funtion here
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = []
        node = root
        queue = [node]
        while queue:
            # push all left nodes until the end 
            while node.left:
                queue.append(node.left)
                node = node.left

            out = queue.pop()
            result.append(out.val)
            if out.right:
                queue.append(out.right)
                node = out.right

        return result

class TestSolution(unittest.TestCase):
    def test_function(self):
        s = Solution()
        # ret = s.new_function()


if __name__ == '__main__':
    unittest.main()
