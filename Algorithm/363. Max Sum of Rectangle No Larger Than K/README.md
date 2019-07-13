# Problem
[Max Sum of Rectangle No Larger Than K](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k)

Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:
```
Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2 
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
```
Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?

## Analysis
- brute force: time = O(M*N*M*N)

## Thoughts
- even brute force used DP thinking 
- Or we can only brute force the column, [j0, j1].
  - for each (j0, j1) combination, get the sum_j0_to_j1[i]

## Solution
```python
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        M = len(matrix)
        N = len(matrix[0])

        sum = [[0 for _ in range(N)] for _ in range(M)]
        # get space[0, (x,y)]
        for i in range(0, M):
            for j in range(0, N):
                if i == 0 and j == 0:
                    sum[i][j] = matrix[0][0]
                elif i == 0:
                    sum[i][j] = sum[i][j-1] + matrix[i][j]
                elif j == 0: 
                    sum[i][j] = sum[i-1][j] + matrix[i][j]
                else:
                    sum[i][j] = sum[i][j-1] + sum[i-1][j] + matrix[i][j] - sum[i-1][j-1]

                if sum[i][j] == k:
                    return k

        result = -10000000
        for i0 in range(0, M):
            for j0 in range(0, N): 
                # (i0, j0) = up-left point                
                for i1 in range(i0, M):
                    for j1 in range(j0, N):
                        # (i1, j1) = bottom-down point 
                        s  = 0
                        if i0 == 0 and j0 == 0:
                            s = sum[i1][j1]
                        elif i0 == 0:
                            s = sum[i1][j1] - sum[i1][j0-1]
                        elif j0 == 0:
                            s = sum[i1][j1] - sum[i0-1][j1]
                        else:
                            # this is the key 
                            s = sum[i1][j1] - sum[i0-1][j1] - sum[i1][j0-1] + sum[i0-1][j0-1]
                        if s == k: 
                            return s
                        if s < k:
                            result = max(result, s)
        return result
```
better solution:
```python

```

## Tags
DP

## Marks
Hard

[comment]: <timestamp:2019-07-13>
