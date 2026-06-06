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
    vector<vector<int>> verticalOrder(TreeNode* root) {
        if(!root)return {};
        map <int,vector<int>> colMap;
        queue<pair<TreeNode*, int>> q;
        q.push({root,0});
        //simple bfs
        while(!q.empty())
        {
            auto [tempNode,col] = q.front();
            q.pop();
            colMap[col].push_back(tempNode->val);
            if(tempNode->left)
            {
                q.push({tempNode->left,col-1});
            }
            if(tempNode->right)
            {
                q.push({tempNode->right,col+1});
            }  
        }
        vector<vector<int>> result ;
        for (auto& [col, values] : colMap) {
            result.push_back(values);
        }
        return result;
    }
};