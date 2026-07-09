# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,node):
        if not node:
            return 0
        L=max(self.dfs(node.left),0)
        R=max(self.dfs(node.right),0)
        M=node.val+L+R
        self.globalmax=max(M,self.globalmax)
        return node.val+max(L,R)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.globalmax = float("-inf")
        self.dfs(root)
        return self.globalmax
        


