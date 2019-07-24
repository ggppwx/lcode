# Problem
[Permutation Sequence](https://leetcode.com/problems/permutation-sequence)

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:
Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

Example 1:
```
Input: n = 3, k = 3
Output: "213"
```
Example 2:
```
Input: n = 4, k = 9
Output: "2314"
```
## Analysis

## Thoughts
- At first, thinking it is a similar problem as **Next Permutation**
- But it seems it could be simpler, when looking at the examples
- for each digit, chose which digit is determined by
    - digit_count_left
    - steps_left 
    - when calculating next steps_left, be aware if mod == 0, which means it's 
      in the **END** of the next level 

## Solution
```python
class Solution:
    def getPermutation(self, n: int, k: int) -> str:        
        if n == 0:
            return ""
        
        digits = [i for i in range(1, n+1)]
        steps_left = k
        digit_left = n - 1
        result = ""
        while digit_left >= 0:
            if digit_left == 0:
                result = result + str(digits[0])
                break

            nc = math.factorial(digit_left)
            
            # chose current
            chose = int((steps_left - 1)/ nc)            
            result = result + str(digits[chose])
            
            # for the next 
            steps_left = (steps_left )  % nc
            steps_left = nc if steps_left == 0 else steps_left
            
            del digits[chose]
            digit_left -= 1
            
        return result 
```

## Tags
Math

## Marks
Overtime

[comment]: <timestamp:2019-07-23>
