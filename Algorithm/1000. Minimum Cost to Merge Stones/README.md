# Problem
[Minimum Cost to Merge Stones](https://leetcode.com/problems/minimum-cost-to-merge-stones)

There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.

Example 1:
```
Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation: 
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
```
Example 2:
```
Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
```
Example 3:
```
Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation: 
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.
 ```

Note:
```
1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100
```
## Analysis

## Thoughts
- Brute force 
- DP 


## Solution    
Brute force: exceeding time limit 
```python
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        if len(stones) == 1:
            return 0
        if len(stones) < K:
            return -1
        sum_k_stone = sum(stones[:K])
        min_cost = 10000000000
        for i in range(len(stones)-K+1):
            # starting from [0, K-1]        
            temp = self.mergeStones(stones[:i] + [sum_k_stone] + stones [i+K:], K) 
            if temp == -1:
                return -1       
            min_cost = min(min_cost, sum_k_stone + temp)
            if i+K >= len(stones):
                break
            sum_k_stone = sum_k_stone - stones[i] + stones[i+K]

        return min_cost 
```
DP:
```python

```
## Tags

## Marks
Help

[comment]: <timestamp:2019-05-15>