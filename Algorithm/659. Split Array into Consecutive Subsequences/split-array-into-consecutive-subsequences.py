"""
Problem
Split Array into Consecutive Subsequences
(https://leetcode.com/problems/split-array-into-consecutive-subsequences)
You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.


Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5
Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5
Example 3:
Input: [1,2,3,4,4,5]
Output: False

"""

import unittest

class Solution:
    """ Notes:
    Be aware of break, continue, return. 
    Even when time = O(n), we still can do some optimization:
    1. defensive check
    2. less cost operation
    3. return once condition meets 
    """
    def isPossible(self, nums: List[int]) -> bool:
        seq_list = []
        for num in nums:
            can_append = False
            for seq in reversed(seq_list):
                if seq[-1] == num - 1:
                    # we can add
                    can_append = True
                    seq.append(num)
                    break #once added, not need to keep looping !!!

            # if unable to add, create a new
            if not can_append:
                # this optimization makes sure no need to go through all numbers 
                for seq in seq_list:
                    if seq[-1] != num and len(seq) < 3:
                        return False

                seq_list.append([num])

        for seq in seq_list:
            if len(seq) < 3:
                return False

        return True






class TestSolution(unittest.TestCase):
    def test_function(self):
        s = Solution()

        # ret = s.new_function()


if __name__ == '__main__':
    unittest.main()
