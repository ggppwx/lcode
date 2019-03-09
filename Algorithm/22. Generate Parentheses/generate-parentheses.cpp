// Problem:
// Generate Parentheses
// (https://leetcode.com/problems/generate-parentheses)


/************** Description *******************

 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

***********************************************/
#include <iostream>
#include <memory>
#include <vector>

using namespace std;

class Solution {
public:
    /** Note
        The key to this problem is to pass down the state of left/right parentheses( number of left/right left)
                 root
               /      \
             (         )[X]
           /    \
          ((      ()
        /  \    /    \
       ((( (() ())[X] ()(
    **/
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


int main ( int argc, char * argv [] ) {
    shared_ptr<Solution> s(new Solution());
    // s->solution_funtion()
    vector<string> result = s->generateParenthesis(3);
    return 0;
}

