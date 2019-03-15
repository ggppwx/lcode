"""
Problem
Longest Substring Without Repeating Characters
(https://leetcode.com/problems/longest-substring-without-repeating-characters)

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

"""
import unittest

class Solution:
    """ Notes:
    This problem has multiple solutions, but to make it O(N), you need sliding
    window. 
    considering the example:
    abba.
    sliding left of window to RIGHT ( can't slide back )
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        existing_index = {}
        max_len = 1
        i = 0
        j = 0
        # window is [i, j]
        existing_index[s[0]] = 0
        while j < len(s) - 1:
            j += 1
            if s[j] in existing_index:
                # not always find the existing index
                i = max(i, existing_index[s[j]] + 1) 

            existing_index[s[j]] = j
            current_len = j - i + 1
            max_len = current_len if current_len > max_len 

        return max_len



class TestSolution(unittest.TestCase):
    def test_function(self):
        s = Solution()
        # ret = s.new_function()


if __name__ == '__main__':
    unittest.main()
