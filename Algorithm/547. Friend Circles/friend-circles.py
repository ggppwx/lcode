"""
Problem
Friend Circles
(https://leetcode.com/problems/friend-circles)

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.

"""
import unittest

class Solution:
    """ Notes:
    DFS solution is easy. let's use Union-find
    Union first. union will put all nodes belonging to the same root together 
    find how many union = find how many root number represents union
    O(n^3) time 
    """
    def init(self, M):
        self.parent = [i for i in range(len(M))

    def find_root(self, x):
        """ Use a descriptive name will help thinking """
        if self.parent[x] == x:
            return x

        # recursion is to find its parent's root 
        return self.find_root(self.parent[x])

    def union(self, x, y):
        x_parent = self.find_root(x)
        y_parent = self.find_root(y)
        if x_parent != y_parent:
            self.parent[x_parent] = y_parent

    def findCircleNum(self, M: List[List[int]]) -> int:
        self.init(M)
        for x in range(len(M)):
            for y in range(len(M)):
                if M[x][y] == 1:
                    # union
                    self.union(x,y)

        # find how many union => find how many root 
        find_map = {}
        for i in range(len(M))
            find_map[self.find_root(i)] = True

        return len(find_map)




class TestSolution(unittest.TestCase):
    def test_function(self):
        s = Solution()
        # ret = s.new_function()


if __name__ == '__main__':
    unittest.main()
