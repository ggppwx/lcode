# Problem
[Jump Game](https://leetcode.com/problems/jump-game)

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:
```
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

Example 2:
```
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
```
## Thoughts
DP state funtion
```
max_can_reach(i) = max(max_can_reach(i-1), i + nums[i])
```

## Solution
```python
class Solution:
    """ Notes:
    Although it is a true or false, convert it to max_index_it_can_reach_before_and_equal_current_index
    think i as a scan to a step 
    """
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums) - 1
        def max_jump_to(n):
            dp = [0] * (n + 1)
            for i in range(len(dp)):
                if i == 0:
                    dp[i] = 0 + nums[i]
                    continue

                if dp[i-1] < i:
                    dp[i] = dp[i-1]
                else:
                    dp[i] = max(dp[i-1], i + nums[i])

            return dp[n]
        return max_jump_to(N) >= N


```
## Tags
DP

[comment]: <timestamp:2019-07-13>
