"""
Problem
Maximum Product Subarray
(https://leetcode.com/problems/maximum-product-subarray)

Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
import unittest

class Solution:
    """ Notes:
    Dynamic programming 
    Since it has +/-, maintain 2 states 
    initial state: NOT 0, for positive state, negative value means Will not chose
    But if you always compare with nums[i], it should be safe, that gives us an elegant solution 
    i.e. -2 3 => (-2 -2), (3=max(-2 *3, 3), -6)
    """
    def maxProduct(self, nums: List[int]) -> int:
        max_ends = [None] * len(nums) # max positive
        min_ends = [None] * len(nums) # min negative
        for i in range(len(nums)):
            if i == 0:
                max_ends[i] = nums[i]
                min_ends[i] = nums[i]
                continue

            if nums[i] > 0:
                max_ends[i] = max(max_ends[i-1] * nums[i], nums[i])
                min_ends[i] = min(min_ends[i-1] * nums[i], nums[i]) 
            elif nums[i] < 0:
                max_ends[i] = max(min_ends[i-1] * nums[i], nums[i])
                min_ends[i] = min(max_ends[i-1] * nums[i], nums[i])
            else:
                max_ends[i] = 0
                min_ends[i] = 0

        return max(max_ends)



class TestSolution(unittest.TestCase):
    def test_function(self):
        s = Solution()
        # ret = s.new_function()


if __name__ == '__main__':
    unittest.main()
