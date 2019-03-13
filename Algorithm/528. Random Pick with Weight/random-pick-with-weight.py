"""
Problem
Random Pick with Weight
(https://leetcode.com/problems/random-pick-with-weight)

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

    1 <= w.length <= 10000
    1 <= w[i] <= 10^5
    pickIndex will be called at most 10000 times.

Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]



"""
import unittest
import random

class Solution:
    """
    Normalize the weight
    then binary search the random generated target value 
    """
    def __init__(self, w: 'List[int]'):
        self.p = []
        sum_weight = 0
        for idx, weight in enumerate(w):
            sum_weight += weight
            self.p.append(sum_weight)

    def pickIndex(self) -> 'int':
        if not self.p:
            return None

        max_sum = self.p[-1]
        chose = random.randint(1, max_sum)

        # binary search
        low = 0
        high = len(self.p) -1
        while low <= high:
            mid = int((low + high)/2)
            if self.p[mid] < chose:
                low = mid + 1
            elif self.p[mid] > chose:
                high = mid - 1
            else:
                return mid

        return high + 1






class TestSolution(unittest.TestCase):
    def test_function(self):
        s = Solution()
        # ret = s.new_function()


if __name__ == '__main__':
    unittest.main()
