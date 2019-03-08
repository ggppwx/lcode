"""
Problem
Longest Word in Dictionary
(https://leetcode.com/problems/longest-word-in-dictionary)

Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character
at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.
If there is no answer, return the empty string.

Example 1:

Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:

Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

"""
import unittest

class Solution:
    """ Notes:
    Dictionary, built one word at a time => Trie 
    """
    class TrieNode(object):
        def __init__(self, c):
            self.c = c
            self.end = 0
            self.word = ""
            self.children = {}

    def insert_to_trie(self, node, word):
        current = node 
        for w in word:
            if w not in current.children:
                current.children[w] = self.TrieNode(w)
            current = current.children[w]
        current.end = 1
        current.word = word

    def dfs_trie(self, node):
        max_word = node.word
        """dictionary iteration not in order """
        for key, child in sorted(node.children.items()):
            if child.end:
                temp_word = self.dfs_trie(child)
                max_word = temp_word if len(temp_word) > len(max_word) else max_word
        return max_word

    def longestWord(self, words: List[str]) -> str:
        root = self.TrieNode('root')
        for word in words:
            self.insert_to_trie(root, word)

        return self.dfs_trie(root)

class TestSolution(unittest.TestCase):
    def test_function(self):
        s = Solution()


if __name__ == '__main__':
    unittest.main()
