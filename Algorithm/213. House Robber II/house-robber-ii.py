"""
Problem
House Robber II
(https://leetcode.com/problems/house-robber-ii)

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at
this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.

Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.


"""
import unittest

class Solution:
    """ Notes:
    Dynamic programming: first step is to get state function
    dp(n) : the max value <= index n
    usually NOT USING "ending with N" as state function
    circle problem compare 2 arrays (without head and without tail)
    """
    def rob(self, nums: List[int]) -> int:
        def rob_max(houses):
            """DP Find the maximum value could robe """
            if not houses:
                return 0
            dp = [0] * len(houses)
            for i, d in enumerate(dp):
                if i == 0:
                    dp[i] = houses[0]
                elif i == 1:
                    dp[i] = max(houses[0], houses[1])
                else:
                    """only 2 conditions"""
                    dp[i] = max(dp[i-2] + houses[i], dp[i-1])
    
            return dp[len(dp)-1]

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(rob_max(nums[:-1]), rob_max(nums[1:]))


class TestSolution(unittest.TestCase):
    def test_function(self):
        s = Solution()
        # ret = s.new_function()


if __name__ == '__main__':
    unittest.main()
