# Problem
[Can I Win](https://leetcode.com/problems/can-i-win)

In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.
What if we change the game so that players cannot re-use integers?
For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.
## Thoughts
- The problem is talking about you/opponent, could be a minMax algorithm
  - Minmax => looking at next step vs current step 
- corner case: unable to reach the target, both loose
  - __So lesson learned: it's no harm to always write special case first__
- minmax(current) = True **UNLESS** all of minmax(next) succeeds

## Solution
```python
class Solution:
    """ Notes:
    MinMax recursion
    Note: if can't reach the target, both loose, don't even need to consider the minmax. this is a special case.
    Memorization: adding cache, DP recursive solution
    Minmax(optimal chose): only when player 2 always win, then player 1 will loose, as long as player 2 lose on one choice, player 1 will select that
    """    
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def minmax(integers, target, cache):
            key = '#'.join([str(integer) for integer in integers])
            if key in cache:
                return cache[key]

            # exit condition
            for integer in integers:
                if integer >= target:
                    cache[key] = True
                    return True

            result = True
            for i, integer in enumerate(integers):
                # pick integer
                result = result and minmax(integers[:i] + integers[i+1:], target - integer, cache)

            
            if result:
                cache[key] = False
                return False
            cache[key] = True
            return True

        # corner case
        if (1+ maxChoosableInteger) * maxChoosableInteger/2 < desiredTotal:
            return False 
        cache = {}
        return minmax([i for i in range(1, maxChoosableInteger+1)], desiredTotal, cache)
```
## Tags
Minmax|DP
## Marks
[comment]: <timestamp:2019-06-09>
