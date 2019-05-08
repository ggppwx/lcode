# Problem
[Jump Game II](https://leetcode.com/problems/jump-game-ii)

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

Example:
```
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
```
Note:
You can assume that you can always reach the last index.

## Analysis
Time
- BFS: worst case O(n^2)
- Greey: O(n)

## Thoughts
- BFS should be easier to think about. 
- given a hard problem, first thinking the brute force solution, in this case
  BFS is the brute force 
- Greedy solution is to update the farthest positon, but only increase the step when 
  reaching the farthest position it sets before 

## Solution
BFS: time limit exceeded 
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        queue = [(0, 0)]
        while queue:
            front, depth = queue.pop(0)
            if front >= len(nums) - 1:
                return depth 
            # front: current position
            # nums[front]: jump distance 
            for pos in range(front + 1, front+nums[front] + 1):
                queue.append((pos, depth + 1))
        return None        
```
Greedy: this is another BFS
```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        farthest = 0 
        steps = 0
        for idx in range(len(nums) - 1):
            farthest = max(farthest, idx + nums[idx] )
            if idx == end: # end < len(nums) - 1
                steps += 1
                end = farthest
        return steps 
```

## Tags
|BFS|Greedy|

## Marks
Help

[comment]: <timestamp:2019-05-08>