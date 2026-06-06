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

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string result = "";
        help_serialize(root,result);
        return result;
        
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        vector<string> tokens = split(data,',');
        int index = 0;
        return help_deserialize(tokens,index);
        
    }

    vector<string> split(string data,char delimiter)
    {
        stringstream ss(data);
        vector<string> tokens;
        string token;
        while(getline(ss,token,delimiter))
        {
            tokens.push_back(token);
        }
        return tokens;

    }

    void help_serialize(TreeNode* node,string& result)
    {
        if(!node)
        {
            result+="N,";
            return;
        }
        result+=to_string(node->val)+',';
        help_serialize(node->left,result);
        help_serialize(node->right,result);
    }
    TreeNode* help_deserialize(vector<string>& tokens,int& index)
    {
        if(tokens[index]=="N")
        {
            index++;
            return nullptr;
        }
        TreeNode* node = new TreeNode(stoi(tokens[index]));
        index++;
        node->left=help_deserialize(tokens,index);
        node->right=help_deserialize(tokens,index);
        return node;
    }
};
