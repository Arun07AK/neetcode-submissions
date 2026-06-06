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
    int maxD;
public:
    int diameterOfBinaryTree(TreeNode* root) {
        maxD=0;
        getHeight(root);
        return maxD;
    }
    int getHeight(TreeNode* root)
    {
        if(!root)
        {
            return 0;
        }
        int leftHeight=getHeight(root->left);
        int rightHeight=getHeight(root->right);
        int sum = leftHeight+rightHeight;
        if(sum>maxD)
        {
            maxD=sum;
        }
        return max(leftHeight,rightHeight)+1;
    }
};
