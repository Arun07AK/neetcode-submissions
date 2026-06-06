/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
private:
    bool isBalancedFlag;
    int getHeight(TreeNode* root)
    {
        if(!root)
        {
            return 0;
        }
        int left_height=getHeight(root->left);
        int right_height=getHeight(root->right);
        if(abs(left_height-right_height)>1)
        {
            isBalancedFlag=false;
        }
        return max(left_height,right_height)+1;
    }

public:
    bool isBalanced(TreeNode* root) {
        isBalancedFlag=true;
        getHeight(root);
        return isBalancedFlag;
    }
};
