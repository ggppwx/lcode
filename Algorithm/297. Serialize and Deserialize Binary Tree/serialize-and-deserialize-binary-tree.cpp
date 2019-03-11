// Problem:
// Serialize and Deserialize Binary Tree
// (https://leetcode.com/problems/serialize-and-deserialize-binary-tree)


/************** Description *******************

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"


***********************************************/
#include <iostream>
#include <vector>
#include <memory>
#include <queue>
#include <sstream>
#include <string>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    /** Note
        This should be a BFS
        When deserializing, put new node to the queue too, and use an INDEX to track node value
        serializing to string => adding delimit, otherwise this will not work
        ALWAYS adding special case check, that won't go wrong 
    **/
    // Encodes a tree to a single string.
    
    vector<string> split(const string& data) {
        // c++ split by delimit 
        stringstream ss(data);
        string item;
        vector<string> result;
        while (getline(ss, item, '|' )) {
            if (item != "")
                result.push_back(item);
        }
        return result;
    }


    string serialize(TreeNode* root) {
        if (!root) {
            // thinking about special case first 
            return "";
        }
        queue<TreeNode*> q;
        q.push(root);
        string result;
        while (!q.empty()){
            TreeNode *current = q.front();
            q.pop();
            if (current) {
                result += "|" + to_string(current->val);
                q.push(current->left);
                q.push(current->right);
            }else {
                result += "|X";
            }
        }
        return result;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        if (data == ""){
            return NULL;
        }
        vector<string> node_vals = split(data); // string to array
        queue<TreeNode*> q;
        TreeNode *root = new TreeNode(stoi(node_vals[0]));
        q.push(root);
        int idx = 1;
        while(!q.empty() && idx < node_vals.size() ){
            TreeNode *current = q.front();
            q.pop();
            string val_left = node_vals[idx++];
            if (idx >= node_vals.size()){
                // defensive programming
                break;
            };
            if (val_left != "X" ) {
                current->left = new TreeNode(stoi(val_left));
                q.push(current->left); // HEY! don't forget to push 
            }
            string val_right = node_vals[idx++];
            if (idx >= node_vals.size()){
                break;
            }
            if (val_right != "X" ) {
                current->right = new TreeNode(stoi(val_right));
                q.push(current->right);
            }
        }
        return root;

    }

    
};


int main ( int argc, char * argv [] ) {
    shared_ptr<Solution> s(new Solution());
    // s->solution_funtion()


}

