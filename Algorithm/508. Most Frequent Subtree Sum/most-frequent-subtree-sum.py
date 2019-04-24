"""
Problem
Most Frequent Subtree Sum
(https://leetcode.com/problems/most-frequent-subtree-sum)
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
import unittest

class Solution:
    """ Notes: 
    """
    # copy the funtion here
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        sum_counter = Counter()
        def getsum(node):
            if not node:
                return 0
            current_sum = node.val + getsum(node.left) + getsum(node.right)
            sum_counter[current_sum] += 1
        getsum(root)
        return [pair[0] for pair in sum_counter.most_common(1)]

class TestSolution(unittest.TestCase):
    def test_function(self):
        s = Solution()
        # ret = s.new_function()


if __name__ == '__main__':
    unittest.main()
