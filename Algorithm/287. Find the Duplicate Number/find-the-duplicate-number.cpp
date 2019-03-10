// Problem:
// Find the Duplicate Number
// (https://leetcode.com/problems/find-the-duplicate-number)


/************** Description *******************
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2

Example 2:

Input: [3,1,3,4,2]
Output: 3

Note:
    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.


***********************************************/
#include <iostream>
#include <vector>
#include <memory>
#include <algorithm>
using namespace std;
class Solution {
public:
    /** Note
        no modifying: can't use the fake hashing solution, No sorting too !
        no extra space: no map
        so thinking about binary search, but here instead search the index, you should search the actual value.
        
        for example: 1 2 4 4 4
        given a TARGET let's say 3, we only have 2 numbers <= 3, which is NOT NORMAL
        but given 2, we have 2 numbers <= 2, which is NORMAL.
        The binary search is to find the TARGET! so we don't have to do O(N) * n (try every number)
    **/
    int findDuplicate(vector<int>& nums) {
        // special cases first 
        if (nums.size() == 1) {
            return 0;
        }
        if (nums.size() == 2) {
            return 1;
        }

        int low = 1;
        int high = nums.size() - 1; // n 
        // binary search

        while (low < high) {
            int mid = (low + high) / 2;
            int count = 0;
            for (int num : nums) {
                if (num <= mid) {
                    count ++;
                }
            }
            // 1 2 2 -> count = 1; 1 1 2 -> count = 2
            // target is in [low, high]
            if (count <= mid) {
                low = mid + 1;
                // on the left side
            } else {
                high = mid;
            }
        }
        return high;

    }
};


int main ( int argc, char * argv [] ) {
    shared_ptr<Solution> s(new Solution());
    // s->solution_funtion()

}

