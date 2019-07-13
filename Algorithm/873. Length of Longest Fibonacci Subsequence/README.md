# Problem
[Length of Longest Fibonacci Subsequence](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence)

A sequence X_1, X_2, ..., X_n is fibonacci-like if:
n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence, find the length of the longest fibonacci-like subsequence of A.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)

Example 1:
```
Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].
```

Example 2:
```
Input: [1,3,7,11,12,14,18]
Output: 3
Explanation:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].
 ```

Note:
```
3 <= A.length <= 1000
1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
(The time limit has been reduced by 50% for submissions in Java, C, and C++.)
```

## Analysis
Time: O(N^2)

## Thoughts
- Be aware of how fab constructed
    - Ak = A_i - A_j, not calculating the diff !!
- Once you get (i,j), you can calulate (j,k)
    - state function => the max length for picking i, j 
- `0 --> False` Be careful when checking index
    - always explicitly check `if k is not None` !
-  `Ak, ..... Aj, ..... Ai` => `DP(j, i) => length contains j, i `
    - the final result will consider all combinations of (i,j)


## Solution
```python
class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        # DP(i, j ) =  max(DP (j, k) + 1) if A[i] - A[j] == A[k]
        index_map = { a : idx for idx, a in enumerate(A)}
        DP = [[1 for _ in range(len(A))] for _ in range(len(A))]
        for i, a in enumerate(A, start=0):
            for j in range(i): # [0, i-1]  
                DP[i][j] = 2
                A_k = A[i] - A[j]
                k = index_map.get(A_k)
                if k != None :  # shit happens here !!
                    DP[i][j] = DP[j][k] + 1
        

        result =  0
        for i in range(len(DP)):
            for j in range(i):
                #print (DP[i][j])
                result  = max(result, DP[i][j])

        return result if result > 2 else 0
```


## Tags
DP

## Marks
Help

[comment]: <timestamp:2019-07-13>
