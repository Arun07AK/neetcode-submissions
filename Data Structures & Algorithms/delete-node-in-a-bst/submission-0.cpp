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
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        if(!root)
        {
            return nullptr;
        }
        if(root->val == key)
        {
            // Case 1: no children
            if(!root->left && !root->right) 
            {
                return nullptr;
            }
            // Case 2: one child
            if(!root->left)
            {
                return root->right;
            }
            if(!root->right)
            {
                return root->left;
            }
            // Case 3: two children
            // Step 1: Find successor (go right once, then left all the way)
            TreeNode* successor = root->right;
            while(successor->left)
            {
                successor=successor->left;
            }
            // Step 2: Copy value
            root->val = successor->val;
            root->right = deleteNode(root->right,successor->val);
            return root;
            
        }
        if(key>root->val)
        {
            root->right=deleteNode(root->right,key);
            return root;
        }
        else {
            root->left=deleteNode(root->left,key);
            return root;
        }
    }
};