# Problem
[K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar)

On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, 
and each occurrence of 1 with 10.
Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
```
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1
```
Explanation:
```
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
```
## Thoughts
- the result only depends on the previous row. 
- DP solution: recursive solution
  ```
  DP(N, k) <=  DP(N-1, K/2)
  ```
- Always think recursive solution first.

## Solution
```python
class Solution:
    """
    Simple recursion: only need to think about previous row.
    I think this also could be done with Dynamic programming, but coming up with a space-saving algorithm is harder 
    TAKES: The first step for DP problem is to find the state equation. then use recursion/bottom-up approach 
    """
    def kthGrammar(self, N, K):
        if N == 1: return 0

        previous = self.kthGrammar(N-1, math.ceil( K/2))
        if previous == 0:
            if K % 2 == 1:
                return 0
            else:
                return 1
        else:
            if K % 2 == 1:
                return 1
            else:
                return 0

```

## Tags
|Recursion|

[comment]: <timestamp:2019-06-20>
