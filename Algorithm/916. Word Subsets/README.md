# Problem
[916 Word Subsets](https://leetcode.com/problems/word-subsets/)

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
```
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]
```

Example 3:
```
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]
```

Example 4:
```
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]
```

Example 5:
```
Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]
```
## Analysis
### Solution 1
Naive solution time O(N^3)

### Solution 2
time O(N^2)

## Thoughts
* Use the right variable in the loop


## Solution
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
        import collections
        char_counter_B = collections.Counter()
        for b in B:
            temp = collections.Counter()
            for c_in_b in b:
                temp[c_in_b] += 1
            for c_in_b in temp:
                # be ware, use the right variable 
                if temp.get(c_in_b) > char_counter_B.get(c_in_b, 0):
                    char_counter_B[c_in_b] = temp.get(c_in_b)
        result = []
        for a in A:
            a_counter = collections.Counter()
            for c in a:
                a_counter[c] += 1
            match = True
            for c in char_counter_B:
                if char_counter_B[c] > a_counter.get(c, 0):
                    match = False
            if match:
                result.append(a)
        return result

    
```

## Tags
String

## Marks
Help

[comment]: <timestamp:2019-05-04>
