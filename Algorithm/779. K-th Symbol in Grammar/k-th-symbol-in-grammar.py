"""
Problem
K-th Symbol in Grammar
(https://leetcode.com/problems/k-th-symbol-in-grammar)

On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001


"""
import unittest
import math

class Solution:
    # copy the funtion here
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1: return 0

        previous = self.kthGrammar(N-1, math.ceil( K/2))
        if previous == 0:
            if K % 2 == 1:
                return 0
            else:
                return 1
        else:
            if K % 2 == 1:
                return 1
            else:
                return 0



class TestSolution(unittest.TestCase):
    def test_function(self):
        s = Solution()
        # ret = s.new_function()
        ret = s.kthGrammar(4, 5)
        print(ret)


if __name__ == '__main__':
    unittest.main()
