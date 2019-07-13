# Problem
[House Robber II](https://leetcode.com/problems/house-robber-ii)

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at
this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
```
Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
```
Example 2:
```
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```
## Thoughts
- __Dynamic programming: first step is to get state function__
- Similar to House Robber I, the difference is it's a cycle 
- dealing with cycle ? check `[0,n-1]` and `[1,n]`, compare 2 arrays (without head and without tail)
- state funciton `dp`: max value <= index 
  `dp[i] = max(dp[i-2] + house[i], dp[i-1])`
    - why not `dp[i] = ending with i ` ? because it only has state function:
      `dp[i] = dp[i-2] + house[i]`, it's obviously not as good as the previous dp function 

## Solution
```python
class Solution:    
    def rob(self, nums: List[int]) -> int:
        def rob_max(houses):            
            if not houses:
                return 0
            dp = [0] * len(houses)
            for i, d in enumerate(dp):
                if i == 0:
                    dp[i] = houses[0]
                elif i == 1:
                    dp[i] = max(houses[0], houses[1])
                else:
                    """only 2 conditions"""
                    dp[i] = max(dp[i-2] + houses[i], dp[i-1])
    
            return dp[len(dp)-1]

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(rob_max(nums[:-1]), rob_max(nums[1:]))
```

## Tags
DP

[comment]: <timestamp:2019-07-13>
