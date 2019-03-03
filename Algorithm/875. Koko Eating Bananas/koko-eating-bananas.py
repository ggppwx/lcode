"""
Problem
Koko Eating Bananas
(https://leetcode.com/problems/koko-eating-bananas)

Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  
The guards have gone and will come back in H hours.
Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, 
and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, 
and won't eat any more bananas during this hour.
Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
Return the minimum integer K such that she can eat all the bananas within H hours.
Example 1:

Input: piles = [3,6,7,11], H = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], H = 5
Output: 30

Example 3:

Input: piles = [30,11,23,4,20], H = 6
Output: 23
"""
import unittest
import math
class Solution:
    """
    Binary serach to find the two pile which the target number sits in between
    then do another bianry search to get the actual target number.
    A easier approach is:
    start = 1
    end = max(piles).
    directly do bianry serach
    
    special case: start == end, target = start
    if meet the condition, the target is in [start, mid], otherwise (mid, end]
    """
    def minEatingSpeed(self, piles: 'List[int]', H: 'int') -> 'int':
        piles = sorted(piles)
        low = 0
        high = len(piles) - 1
        while low <=  high:
            mid = int((low + high) / 2)
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p/piles[mid])

            if total_hours <= H:
                high = mid - 1
            else:
                low = mid + 1

        if low >= len(piles):
            return  None

        start  = piles[high] if high >= 0 else 1
        end = piles[high + 1]
        while start < end:
            mid = int((start + end)/2)
            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p/mid)

            if total_hours <= H:
                end  = mid
            else:
                start = mid + 1
            
        return start




class TestSolution(unittest.TestCase):
    def test_function(self):
        s = Solution()
        # ret = s.new_function()
        piles = [30,11,23,4,20]
        H = 5
        ret = s.minEatingSpeed(piles, H)
        print(ret)
        piles = [30,11,23,4,20]
        H = 6
        ret = s.minEatingSpeed(piles, H)
        print(ret)

if __name__ == '__main__':
    unittest.main()
