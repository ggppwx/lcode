# Problem
[Minimum Score Triangulation of Polygon](https://leetcode.com/problems/minimum-score-triangulation-of-polygon)

Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i], ..., A[N-1] in clockwise order.
Suppose you triangulate the polygon into N-2 triangles.  For each triangle, the value of that triangle is the product of the labels of the vertices, and the total score of the triangulation is the sum of these values over all N-2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.

Example 1:
```
Input: [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.
```

Example 2:
```
Input: [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.  The minimum score is 144.
```
## Analysis
- solution 1: time O(n!) this definitely looks aweful !

## Thoughts
- Convert the problem to sub-problem 
- DO NOT look this as a graph problem. 
    - keyword: min, and it is a list, thinking about sub-problem 
- In solution 2, we pick triangle instead of a point
    - a triangle will split the polygon into 2 pieces 
    - for point 0 and N-1, it always constructs a triangle 

## Solution
Solution 1: exceeding time limit 
```python
class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        cache = {}
        return minScoreTriangulation(A, cache)

    def minScoreTriangulation(self, A: List[int], cache) -> int:
        if len(A) < 3:
            return 0

        key = '#'.join(sorted(A))
        if key in cache:
            return cache[key]

        result = 2**31 - 1
        for i, a in enumerate(A):
            # pick a and its closest neighbor 
            A_right = A[(i+1)%len(A)]
            A_left = A[i - 1]
            triangle = a * A_left * A_right

            leftover = A[:i] + A[i+1:]
            result = min( result, triangle + self.minScoreTriangulation(leftover, cache) ) 

        cache[key] = result         
        return result 
```
Solution 2: pick triangle, DP solution
```python

```


## Tags
|DP|

## Marks
Help

[comment]: <timestamp:2019-05-09>
