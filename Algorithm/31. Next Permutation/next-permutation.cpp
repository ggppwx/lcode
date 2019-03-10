// Problem:
// Next Permutation
// (https://leetcode.com/problems/next-permutation)


/************** Description *******************
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

***********************************************/
#include <iostream>
#include <vector>
#include <memory>
#include <algorithm>
using namespace std;

class Solution {
public:
    /** Note
        if using brute force: finding all permutations possible. 
        Solving problem by example.
           3
         /  \
        2    \
              1
        =>
        3,  1, 2, we still need to swap and reverse

        there's Only one exception: 3, 2, 1
    **/
    void nextPermutation(vector<int>& nums) {
        // find the pviot
        int pivot = -1;
        for (int i = nums.size() - 1; i > 0; i--){
            if (nums[i-1] < nums[i]) {
                pivot = i;
                for (int j = nums.size() - 1; j >= pivot; j--) {
                    if(nums[j] > nums[pivot-1]) {
                        // swap
                        swap(nums[j], nums[pivot-1]);
                        // reverse [pivot + 1, end ]

                        reverse(nums.begin() + pivot, nums.end());
                        return;
                    }
                }
            }
        }
        if (pivot == -1) { // already max
            reverse(nums.begin(), nums.end());
            return;
        }
        
    }
};


int main ( int argc, char * argv [] ) {
    shared_ptr<Solution> s(new Solution());
    // s->solution_funtion()


}

