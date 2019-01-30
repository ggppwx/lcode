"""
Problem
All Possible Full Binary Trees
(https://leetcode.com/problems/all-possible-full-binary-trees)




"""
import unittest

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # copy the funtion here
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
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

class TestSolution(unittest.TestCase):
    

    def test_function(self):
        def printt(node):
            if not node:
                print('X', end="")
                return
            print(node.val, end="")
            printt(node.left)
            printt(node.right)


        s = Solution()
        # ret = s.new_function()
        ret = s.allPossibleFBT(7)
        print(len(ret))
        for r in ret:
            printt(r)
            print('----')

if __name__ == '__main__': 
    unittest.main()
