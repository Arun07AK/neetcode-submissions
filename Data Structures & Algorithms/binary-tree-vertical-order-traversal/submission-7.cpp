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
    vector<tuple<int,int,int>> nodes;
public:
    void bfs(TreeNode* node)
    {
        queue<tuple<int , int,TreeNode*>> q;
        if(node)
        {
            q.push({0,0,node});
        }
        while(!q.empty())
        {
            int levelSize = q.size();
            for(int i = 0;i<levelSize;i++)
            {
                auto [ col, row, temp] = q.front();
                q.pop();
                nodes.push_back({col,row,temp->val});
                if(temp->left)
                {
                    q.push({col-1,row+1,temp->left});
                }
                if(temp->right)
                {
                    q.push({col+1,row+1,temp->right});
                }
            }
        }
    }
    vector<vector<int>> verticalOrder(TreeNode* root) {
        if(!root)
        {
            return {};
        }
        bfs(root);
        map <int,vector<int>> colMap;
        vector<vector<int>> result;
        for (const auto& [col, row, val] : nodes) {
            colMap[col].push_back(val);  // ✓ Clean and readable
        }
        for (auto& [col, values] : colMap) {
            result.push_back(values);
        }
        return result;
    }
};