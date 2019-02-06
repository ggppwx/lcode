"""
Problem
Pancake Sorting
(https://leetcode.com/problems/pancake-sorting)
Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.

 

Example 1:

Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 
Example 2:

Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.
 

Note:

1 <= A.length <= 100
A[i] is a permutation of [1, 2, ..., A.length]



"""
import unittest

class Solution:
    # copy the funtion here
    def pancakeSort(self, A: 'List[int]') -> 'List[int]':
        # 1, 2 3,   len(A)
        def swap(A, length):
            # swap from 0 to length - 1
            if length == 0:
                return

            i = 0
            j = length - 1
            while i < j:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1



        current_max = len(A)
        if current_max == 1:
            return []

        result = []
        while current_max > 0:
            for i in range(current_max):
                if A[i] == current_max:
                    if i == current_max - 1:
                        # no move
                        current_max -= 1
                    elif i == 0:
                        # the max on first
                        swap(A, current_max)
                        result.append(current_max)
                        current_max -= 1
                    else:
                        swap(A, i + 1)
                        result.append(i+1)
                    break


        return result





class TestSolution(unittest.TestCase):
    def test_function(self):
        s = Solution()
        # ret = s.new_function()
        ret = s.pancakeSort([3, 2, 4, 1])
        print(ret)

if __name__ == '__main__':
    unittest.main()
