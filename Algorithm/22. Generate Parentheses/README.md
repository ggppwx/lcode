# Problem
[Generate Parentheses](https://leetcode.com/problems/generate-parentheses)

 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```
## Thoughts 
- Typical combination problem, Use Graph(tree) traverse to simplify the problem 
    ```
                 root
               /      \
             (         )[X]
           /    \
          ((      ()
        /  \    /    \
       ((( (() ())[X] ()(

    ```
- Putting the choice into recursive function 
    ```python
    gen('(') # go left
    gen(')') # right 
    ```
- The constrain of going rihgt `left > right`

## Solution
```cpp
class Solution {
public:    
    void gen(string current, int left, int right, vector<string> &result) {
        if (left == 0 && right == 0){
            result.push_back(current);
            return;
        }

        if ( left > 0 ) {
            gen(current + "(", left - 1, right, result);
        }

        if (right > 0 && right > left ) {
            gen(current + ")", left, right - 1, result);
        }
    }

    vector<string> generateParenthesis(int n) {
        vector<string> result;
        this->gen("", n, n, result);
        return result;
    }
};
```

## Tags
|Backtracking|String|
## Marks
[comment]: <timestamp:2019-05-28>



