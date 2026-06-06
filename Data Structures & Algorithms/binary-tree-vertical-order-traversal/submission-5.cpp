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
    vector<vector<int>> nodes;
public:
    void dfs(int column , int row , TreeNode* node)
    {
        if(!node)
        {
            return;
        }
        nodes.push_back({column,row, node->val});
        if(node->left)
        {
            dfs(column-1,row+1,node->left);
        }
        if(node->right)
        {
            dfs(column+1,row+1,node->right);
        }
    }
    vector<vector<int>> verticalOrder(TreeNode* root) {
        nodes.clear();
        if(!root)
        {
            return {};
        }
        dfs(0,0,root);
        stable_sort(nodes.begin(), nodes.end(), [](const vector<int>& a, const vector<int>& b) {
            if (a[0] != b[0]) return a[0] < b[0];   // column (left → right)
            return a[1] < b[1];                     // row (top → bottom)
        });
        map <int,vector<int>> colMap;
        for (const auto& node :nodes )
        {
            colMap[node[0]].push_back(node[2]);
        }
        vector<vector<int>> result;
        for (auto& [col, values] : colMap) {
            result.push_back(values);
        }
        return result;
    }
};