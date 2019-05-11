# Problem
[Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree)

Implement a trie with insert, search, and startsWith methods.

Example:
```
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
```

Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

## Analysis
Time: O(N)

## Thoughts
- Simple Trie problem, Create a **helper data structure**
  - It's very useful, for example `linkList` data structure has private class `Node`
- Thinking to create your own API ?

## Solution
```python
class Trie:

    class Node():
        def __init__(self):
            self.children = {}
            self.isWord = False 

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for w in word:
            if w not in node.children:
                # not exist, create a new node 
                node.children[w] = self.Node()            
            node = node.children[w]
        
        # end of word, the node ends here
        node.isWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        if node.isWord:
            return True        
        return False

        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for w in prefix:
            if w not in node.children:
                return False
            node = node.children[w]
        
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

```


## Tags
Trie

## Marks

[comment]: <timestamp:2019-05-11>