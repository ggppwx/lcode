# Problem
We are given two arrays A and B of words.  Each word is a string of lowercase letters.
Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".
Now say a word a from A is universal if for every b in B, b is a subset of a. 
Return a list of all universal words in A.  You can return the words in any order.


Example 1:
```
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]
```

Example 2:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]

Example 3:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]

Example 4:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]

Example 5:
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]
# Analysis
## Solution 1
Naive solution time O(N^3)

## Solution 2
time O(N^2)

# Thoughts

# Solution
Solution 1: exceeding time 
```python
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        import collections
        def isSubset(b, a):
            char_counter = collections.Counter()
            for c in a:
                char_counter[c] += 1
            for c in b:
                if char_counter.get(c, 0) == 0:
                    return False
                else:
                    char_counter[c] -= 1

            return True

        result = []
        for a in A:
            isUniversal = True
            for b in B:
                if not isSubset(b, a):
                    isUniversal = False
                    break
            if isUniversal:
                result.append(a)
        return result

```

Better solution 
```python
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
    

```

# Info
## Tags


## Marks

[comment]: <timestamp:2019-05-02>
