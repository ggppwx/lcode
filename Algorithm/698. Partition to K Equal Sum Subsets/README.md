# Problem
[Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets)

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 
Example 1:
```
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
```

## Thoughts
- finding the subsets whose sum is total/k
  - the problem converts to **if we can find sub-sets whose sum=target**
- the problem is NP-hard
- for each number in the arrary, we could pick that number first 
  - until the the current == 0, then we reset 
  - Don't forget to **add the number you pick** back after the recursion 


## Solution
```python
class Solution:
    """
    Calculate the Target value ( sum(nums)/k ), then make up for the value 
    """
    def canPartitionKSubsets(self, nums, k):

        def find(array, current, target, subnum):
            if subnum > k:
                return False

            if len(array) == 0:
                if current == 0:
                    return True
                else:
                    return False


            if current == 0:
                print(array)
                return find(array, target, target, subnum + 1)

            i = 0 
            while i < len(array):
                # pick i
                if array[i] <= current:
                    tmp = array[i]
                    array = array[:i] + array[i+1:]
                    if find(array, current - tmp, target, subnum):
                        return True
                    array.insert(i, tmp)

                i += 1

            return False

        target = sum(nums)/k
        if int(target) != target:
            return False

        return find(nums, target, target, 0)

```

## Tags
|Recursion|Backtracking|

[comment]: <timestamp:2019-06-20>
