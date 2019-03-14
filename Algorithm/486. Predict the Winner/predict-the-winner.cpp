// Problem:
// Predict the Winner
// (https://leetcode.com/problems/predict-the-winner)


/************** Description *******************
Given an array of scores that are non-negative integers. Player 1 picks one
of the numbers from either end of the array followed by the player 2 and
then player 1 and so on. Each time a player picks a number, that number will
not be available for the next player. This continues until all the scores
have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.

***********************************************/
#include <iostream>
#include <vector>
#include <memory>
using namespace std;

class Solution {
public:
    /** Note
        This is a minmax probelm:
        every time you have 2 choices: pick left, pick right
        Minmax(i, j) = Max(nums[i] - Minmax(i+1, j),
                           nums[j] - Minmax(i, j -1))
        Minmax => the max diff (player 1 - player 2), this is because player 2
        will chose the optimal move, player 1's move (i or j) will be offset by player 2's max score move 

    **/
    // copy the functions here
    bool PredictTheWinner(vector<int>& nums) {
        int minmax[nums.size()][nums.size()] = {{0}};
        int k = 0;
        while(k < nums.size()){
            for ( int i = 0; i < nums.size(); i ++) {
                for (int j = i + k; j < nums.size(); j ++){
                    if (i == j) {
                        minmax[i][j] = nums[i];
                    } else {
                        minmax[i][j] = max(nums[i] - minmax[i+1][j],
                                           nums[j] - minmax[i][j-1]);
                    }
                }
            }
            k ++; 
        }
        return minmax[0][nums.size()-1] >= 0;
    }
};


int main ( int argc, char * argv [] ) {
    shared_ptr<Solution> s(new Solution());
    // s->solution_funtion()


}

