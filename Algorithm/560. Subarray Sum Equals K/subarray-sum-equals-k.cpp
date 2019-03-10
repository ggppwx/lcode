// Problem:
// Subarray Sum Equals K
// (https://leetcode.com/problems/subarray-sum-equals-k)


/************** Description *******************
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Note:

    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

***********************************************/
#include <iostream>
#include <vector>
#include <memory>
#include <unordered_map>
using namespace std;

class Solution {
public:
    /** Note
        the sum of continuous subarray  = [0, right] - [0, left]
        special case:
        (1), 0 => acc: 1
        (1,0,0), 1 => acc (1, 1, 1) map: 0:1 1:1 1:2
        BE aware of when to add the result to acc_map, it's after calculating current 
    **/
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> acc_map;
        vector<int> num_acc;
        int acc = 0;
        for (int num : nums) {
            acc = acc + num;
            num_acc.push_back(acc);
        }

        int result = 0;
        acc_map[0] = 1;
        for (int acc : num_acc) {
            // number ending with index i. 
            int target = acc - k;
            if (acc_map.find(target) != acc_map.end()){
                result += acc_map[target];
            }
            // DO NOT adding current value to map before checking it 
            if (acc_map.find(acc) != acc_map.end()){
                acc_map[acc] ++;
            } else {
                acc_map[acc] = 1;
            }
            
        }
        return result; 


    }
};


int main ( int argc, char * argv [] ) {
    shared_ptr<Solution> s(new Solution());
    // s->solution_funtion()


}

