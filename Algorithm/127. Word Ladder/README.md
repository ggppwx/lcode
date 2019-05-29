# Problem
Problem
Word Ladder
(https://leetcode.com/problems/word-ladder)

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence
from beginWord to endWord, such that:
    Only one letter can be changed at a time.
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:
    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
```
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
```
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:
```
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0
```
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

## Thoughts 
- It's a Graph search problem, genering a graph from word to word costs O(N^2)
- Let's think if the length is very small, it could take O(N*L) to generate a graph of (generic word) to word 
    - `cog` can be convert to `*og` `c*g` `co*`
    - BFS the neigobor of `cog`

## Solution
```python
class Solution:    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        import collections

        word_graph = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                word_graph[word[:i] + '*' + word[i+1:]].append(word)

        if beginWord == endWord:
            return 0

        visited  = {}
        queue = collections.deque([(beginWord, 0 )])
        while queue:
            current, depth = queue.popleft()

            if current == endWord:
                return depth + 1
            
            # THIS IS NOT THE RIGHT BFS, IT will causes repeated visit
            visited[current] = 1

            # add its neighbor
            for i in range(len(beginWord)):
                temp_current = current[:i] + '*' + current[i+1:]
                for word in word_graph.get(temp_current, []):
                    if word not in visited:
                        queue.append((word, depth + 1))

        return 0
```

## Tags
BFS
## Marks
Help

[comment]: <timestamp:2019-05-28>
